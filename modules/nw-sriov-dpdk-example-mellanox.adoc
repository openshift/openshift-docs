// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: PROCEDURE
[id="example-vf-use-in-dpdk-mode-mellanox_{context}"]
= Using a virtual function in DPDK mode with a Mellanox NIC

You can create a network node policy and create a Data Plane Development Kit (DPDK) pod using a virtual function in DPDK mode with a Mellanox NIC.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have installed the Single Root I/O Virtualization (SR-IOV) Network Operator.
* You have logged in as a user with `cluster-admin` privileges.

.Procedure

. Save the following `SriovNetworkNodePolicy` YAML configuration to an `mlx-dpdk-node-policy.yaml` file:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: mlx-dpdk-node-policy
  namespace: openshift-sriov-network-operator
spec:
  resourceName: mlxnics
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  priority: <priority>
  numVfs: <num>
  nicSelector:
    vendor: "15b3"
    deviceID: "1015" <1>
    pfNames: ["<pf_name>", ...]
    rootDevices: ["<pci_bus_id>", "..."]
  deviceType: netdevice <2>
  isRdma: true <3>
----
<1> Specify the device hex code of the SR-IOV network device.
<2> Specify the driver type for the virtual functions to `netdevice`. A Mellanox SR-IOV Virtual Function (VF) can work in DPDK mode without using the `vfio-pci` device type. The VF device appears as a kernel network interface inside a container.
<3> Enable Remote Direct Memory Access (RDMA) mode. This is required for Mellanox cards to work in DPDK mode.
+
[NOTE]
=====
See _Configuring an SR-IOV network device_ for a detailed explanation of each option in the `SriovNetworkNodePolicy` object.

When applying the configuration specified in an `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes.
It might take several minutes for a configuration change to apply.
Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.

After the configuration update is applied, all the pods in the `openshift-sriov-network-operator` namespace will change to a `Running` status.
=====

. Create the `SriovNetworkNodePolicy` object by running the following command:
+
[source,terminal]
----
$ oc create -f mlx-dpdk-node-policy.yaml
----

. Save the following `SriovNetwork` YAML configuration to an `mlx-dpdk-network.yaml` file:
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: mlx-dpdk-network
  namespace: openshift-sriov-network-operator
spec:
  networkNamespace: <target_namespace>
  ipam: |- <1>
...
  vlan: <vlan>
  resourceName: mlxnics
----
<1> Specify a configuration object for the IP Address Management (IPAM) Container Network Interface (CNI) plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.
+
[NOTE]
=====
See _Configuring an SR-IOV network device_ for a detailed explanation on each option in the `SriovNetwork` object.
=====
+
The `app-netutil` option library provides several API methods for gathering network information about the parent pod of a container.

. Create the `SriovNetwork` object by running the following command:
+
[source,terminal]
----
$ oc create -f mlx-dpdk-network.yaml
----
. Save the following `Pod` YAML configuration to an `mlx-dpdk-pod.yaml` file:

+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-app
  namespace: <target_namespace> <1>
  annotations:
    k8s.v1.cni.cncf.io/networks: mlx-dpdk-network
spec:
  containers:
  - name: testpmd
    image: <DPDK_image> <2>
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"] <3>
    volumeMounts:
    - mountPath: /mnt/huge <4>
      name: hugepage
    resources:
      limits:
        openshift.io/mlxnics: "1" <5>
        memory: "1Gi"
        cpu: "4" <6>
        hugepages-1Gi: "4Gi" <7>
      requests:
        openshift.io/mlxnics: "1"
        memory: "1Gi"
        cpu: "4"
        hugepages-1Gi: "4Gi"
    command: ["sleep", "infinity"]
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
----
<1> Specify the same `target_namespace` where `SriovNetwork` object `mlx-dpdk-network` is created. To create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and `SriovNetwork` object.
<2> Specify the DPDK image which includes your application and the DPDK library used by the application.
<3> Specify additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.
<4> Mount the hugepage volume to the DPDK pod under `/mnt/huge`. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.
<5> Optional: Specify the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.
<6> Specify the number of CPUs. The DPDK pod usually requires that exclusive CPUs be allocated from the kubelet. To do this, set the CPU Manager policy to `static` and create a pod with `Guaranteed` Quality of Service (QoS).
<7> Specify hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepages requires adding kernel arguments to Nodes.

. Create the DPDK pod by running the following command:
+
[source,terminal]
----
$ oc create -f mlx-dpdk-pod.yaml
----
