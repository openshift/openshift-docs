// This module is included in the following assemblies:
//
// nodes/edge/nodes-edge-remote-workers.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-rwn_con_adding-remote-worker-nodes_{context}"]
= Adding remote worker nodes

Adding remote worker nodes to a cluster involves some additional considerations.

* You must ensure that a route or a default gateway is in place to route traffic between the control plane and every remote worker node.

* You must place the Ingress VIP on the control plane.

* Adding remote worker nodes with user-provisioned infrastructure is identical to adding other worker nodes.

* To add remote worker nodes to an installer-provisioned cluster at install time, specify the subnet for each worker node in the `install-config.yaml` file before installation. There are no additional settings required for the DHCP server. You must use virtual media, because the remote worker nodes will not have access to the local provisioning network.

* To add remote worker nodes to an installer-provisioned cluster deployed with a provisioning network, ensure that `virtualMediaViaExternalNetwork` flag is set to `true` in the `install-config.yaml` file so that it will add the nodes using virtual media. Remote worker nodes will not have access to the local provisioning network. They must be deployed with virtual media rather than PXE. Additionally, specify each subnet for each group of remote worker nodes and the control plane nodes in the DHCP server.