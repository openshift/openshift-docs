// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-running-dpdk-rootless-tap_{context}"]
= Using the TAP CNI to run a rootless DPDK workload with kernel access

DPDK applications can use `virtio-user` as an exception path to inject certain types of packets, such as log messages, into the kernel for processing. For more information about this feature, see link:https://doc.dpdk.org/guides/howto/virtio_user_as_exception_path.html[Virtio_user as Exception Path].

In OpenShift Container Platform version 4.14 and later, you can use non-privileged pods to run DPDK applications alongside the tap CNI plugin. To enable this functionality, you need to mount the `vhost-net` device by setting the `needVhostNet` parameter to `true` within the `SriovNetworkNodePolicy` object.

.DPDK and TAP example configuration
image::348_OpenShift_rootless_DPDK_0923.png[DPDK and TAP plugin]

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have installed the SR-IOV Network Operator.
* You are logged in as a user with `cluster-admin` privileges.
* Ensure that `setsebools container_use_devices=on` is set as root on all nodes.
+
[NOTE]
====
Use the Machine Config Operator to set this SELinux boolean.
====

.Procedure

. Create a file, such as `test-namespace.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: test-namespace
  labels:
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
    security.openshift.io/scc.podSecurityLabelSync: "false"
----

. Create the new `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f test-namespace.yaml
----

. Create a file, such as `sriov-node-network-policy.yaml`, with content like the following example::
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
 name: sriovnic
 namespace: openshift-sriov-network-operator
spec:
 deviceType: netdevice <1>
 isRdma: true <2>
 needVhostNet: true <3>
 nicSelector:
   vendor: "15b3" <4>
   deviceID: "101b" <5>
   rootDevices: ["00:05.0"]
 numVfs: 10
 priority: 99
 resourceName: sriovnic
 nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
----
<1> This indicates that the profile is tailored specifically for Mellanox Network Interface Controllers (NICs).
<2> Setting `isRdma` to `true` is only required for a Mellanox NIC.
<3> This mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload.
<4> The vendor hexadecimal code of the SR-IOV network device. The value 15b3 is associated with a Mellanox NIC.
<5> The device hexadecimal code of the SR-IOV network device.

. Create the `SriovNetworkNodePolicy` object by running the following command:
+
[source,terminal]
----
$ oc create -f sriov-node-network-policy.yaml
----

. Create the following `SriovNetwork` object, and then save the YAML in the `sriov-network-attachment.yaml` file:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
 name: sriov-network
 namespace: openshift-sriov-network-operator
spec:
 networkNamespace: test-namespace
 resourceName: sriovnic
 spoofChk: "off"
 trust: "on"
----
+
[NOTE]
=====
See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.
=====
+
An optional library, `app-netutil`, provides several API methods for gathering network information about a container's parent pod.

. Create the `SriovNetwork` object by running the following command:
+
[source,terminal]
----
$ oc create -f sriov-network-attachment.yaml
----

. Create a file, such as `tap-example.yaml`, that defines a network attachment definition, with content like the following example:
+
[source,yaml]
----
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
 name: tap-one
 namespace: test-namespace <1>
spec:
 config: '{
   "cniVersion": "0.4.0",
   "name": "tap",
   "plugins": [
     {
        "type": "tap",
        "multiQueue": true,
        "selinuxcontext": "system_u:system_r:container_t:s0"
     },
     {
       "type":"tuning",
       "capabilities":{
         "mac":true
       }
     }
   ]
 }'
----
<1> Specify the same `target_namespace` where the `SriovNetwork` object is created.

. Create the `NetworkAttachmentDefinition` object by running the following command:
+
[source,terminal]
----
$ oc apply -f tap-example.yaml
----

. Create a file, such as `dpdk-pod-rootless.yaml`, with content like the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-app
  namespace: test-namespace <1>
  annotations:
    k8s.v1.cni.cncf.io/networks: '[
      {"name": "sriov-network", "namespace": "test-namespace"},
      {"name": "tap-one", "interface": "ext0", "namespace": "test-namespace"}]'
spec:
  nodeSelector:
    kubernetes.io/hostname: "worker-0"
  securityContext:
      fsGroup: 1001 <2>
      runAsGroup: 1001 <3>
      seccompProfile:
        type: RuntimeDefault
  containers:
  - name: testpmd
    image: <DPDK_image> <4>
    securityContext:
      capabilities:
        drop: ["ALL"] <5>
        add: <6>
          - IPC_LOCK
          - NET_RAW #for mlx only <7>
      runAsUser: 1001 <8>
      privileged: false <9>
      allowPrivilegeEscalation: true <10>
      runAsNonRoot: true <11>
    volumeMounts:
    - mountPath: /mnt/huge <12>
      name: hugepages
    resources:
      limits:
        openshift.io/sriovnic: "1" <13>
        memory: "1Gi"
        cpu: "4" <14>
        hugepages-1Gi: "4Gi" <15>
      requests:
        openshift.io/sriovnic: "1"
        memory: "1Gi"
        cpu: "4"
        hugepages-1Gi: "4Gi"
    command: ["sleep", "infinity"]
  runtimeClassName: performance-cnf-performanceprofile <16>
  volumes:
  - name: hugepages
    emptyDir:
      medium: HugePages
----
+
--
<1> Specify the same `target_namespace` in which the `SriovNetwork` object is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.
<2> Sets the group ownership of volume-mounted directories and files created in those volumes.
<3> Specify the primary group ID used for running the container.
<4> Specify the DPDK image that contains your application and the DPDK library used by application.
<5> Removing all capabilities (`ALL`) from the container's securityContext means that the container has no special privileges beyond what is necessary for normal operation.
<6> Specify additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access. These capabilities must also be set in the binary file by using the `setcap` command.
<7> Mellanox network interface controller (NIC) requires the `NET_RAW` capability.
<8> Specify the user ID used for running the container.
<9> This setting indicates that the container or containers within the pod should not be granted privileged access to the host system.
<10>  This setting allows a container to escalate its privileges beyond the initial non-root privileges it might have been assigned.
<11> This setting ensures that the container runs with a non-root user. This helps enforce the principle of least privilege, limiting the potential impact of compromising the container and reducing the attack surface.
<12> Mount a hugepage volume to the DPDK pod under `/mnt/huge`. The hugepage volume is backed by the emptyDir volume type with the medium being `Hugepages`.
<13> Optional: Specify the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.
<14> Specify the number of CPUs. The DPDK pod usually requires exclusive CPUs to be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.
<15> Specify hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes. For example, adding kernel arguments `default_hugepagesz=1GB`, `hugepagesz=1G` and `hugepages=16` will result in `16*1Gi` hugepages be allocated during system boot.
<16> If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.
--
+
. Create the DPDK pod by running the following command:
+
[source,terminal]
----
$ oc create -f dpdk-pod-rootless.yaml
----