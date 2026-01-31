// Module included in the following assemblies:
//
// * networking/hardware_networks/configuring-interface-sysctl-sriov-device.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-labeling-sriov-enabled-nodes_{context}"]
= Labeling nodes with an SR-IOV enabled NIC

If you want to enable SR-IOV on only SR-IOV capable nodes there are a couple of ways to do this:

. Install the Node Feature Discovery (NFD) Operator. NFD detects the presence of SR-IOV enabled NICs and labels the nodes with `node.alpha.kubernetes-incubator.io/nfd-network-sriov.capable = true`.

. Examine the `SriovNetworkNodeState` CR for each node. The `interfaces` stanza includes a list of all of the SR-IOV devices discovered by the SR-IOV Network Operator on the worker node. Label each node with `feature.node.kubernetes.io/network-sriov.capable: "true"` by using the following command:
+
[source,yaml]
----
$ oc label node <node_name> feature.node.kubernetes.io/network-sriov.capable="true"
----
+
[NOTE]
====
You can label the nodes with whatever name you want.
====
