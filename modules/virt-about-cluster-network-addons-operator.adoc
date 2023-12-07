// Module included in the following assemblies:
//
// * virt/virt-architecture.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-cluster-network-addons-operator_{context}"]
= About the Cluster Network Addons Operator

The Cluster Network Addons Operator, `cluster-network-addons-operator`, deploys networking components on a cluster and manages the related resources for extended network functionality.

image::cnv_components_cluster-network-addons-operator.png[cluster-network-addons-operator components]

.Cluster Network Addons Operator components
[cols="1,1"]
|===
|*Component* |*Description*

|`deployment/kubemacpool-cert-manager`
|Manages TLS certificates of Kubemacpool’s webhooks.

|`deployment/kubemacpool-mac-controller-manager`
|Provides a MAC address pooling service for virtual machine (VM) network interface cards (NICs).

|`daemonset/bridge-marker`
|Marks network bridges available on nodes as node resources.

|`daemonset/kube-cni-linux-bridge-plugin`
|Installs Container Network Interface (CNI) plugins on cluster nodes, enabling the attachment of VMs to Linux bridges through network attachment definitions.
|===
