// Module included in the following assemblies:
//
// * networking/hardware_networks/using-dpdk-and-rdma.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-sriov-create-object_{context}"]
= Example SR-IOV network operator

The following is an example definition of an `sriovNetwork` object. In this case, Intel and Mellanox configurations are identical:
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-1
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.1.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}' <1>
  networkNamespace: dpdk-test <2>
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_1 <3>
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-2
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.2.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_2
----
<1> You can use a different IP Address Management (IPAM) implementation, such as Whereabouts. For more information, see _Dynamic IP address assignment configuration with Whereabouts_.
<2> You must request the `networkNamespace` where the network attachment definition will be created. You must create the `sriovNetwork` CR under the `openshift-sriov-network-operator` namespace.
<3> The `resourceName` value must match that of the `resourceName` created under the `sriovNetworkNodePolicy`.
