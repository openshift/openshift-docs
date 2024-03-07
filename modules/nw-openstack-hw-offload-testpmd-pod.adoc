// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-openstack-hw-offload-testpmd-pod_{context}"]
= A test pod template for clusters that use OVS hardware offloading on OpenStack

The following `testpmd` pod demonstrates Open vSwitch (OVS) hardware offloading on {rh-openstack-first}.

.An example `testpmd` pod
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: testpmd-sriov
  namespace: mynamespace
  annotations:
    k8s.v1.cni.cncf.io/networks: hwoffload1
spec:
  runtimeClassName: performance-cnf-performanceprofile <1>
  containers:
  - name: testpmd
    command: ["sleep", "99999"]
    image: registry.redhat.io/openshift4/dpdk-base-rhel8:v4.9
    securityContext:
      capabilities:
        add: ["IPC_LOCK","SYS_ADMIN"]
      privileged: true
      runAsUser: 0
    resources:
      requests:
        memory: 1000Mi
        hugepages-1Gi: 1Gi
        cpu: '2'
      limits:
        hugepages-1Gi: 1Gi
        cpu: '2'
        memory: 1000Mi
    volumeMounts:
      - mountPath: /mnt/huge
        name: hugepage
        readOnly: False
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
----
<1> If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.
