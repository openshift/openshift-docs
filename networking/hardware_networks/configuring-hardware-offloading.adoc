:_mod-docs-content-type: ASSEMBLY
[id="configuring-hardware-offloading"]
= Configuring hardware offloading
include::_attributes/common-attributes.adoc[]
:context: configuring-hardware-offloading

toc::[]

As a cluster administrator, you can configure hardware offloading on compatible nodes to increase data processing performance and reduce load on host CPUs.

//What is this feature, who needs it?

include::modules/nw-sriov-hwol-about-hardware-offloading.adoc[leveloffset=+1]

//Which NICs do we support?

include::modules/nw-sriov-hwol-supported-devices.adoc[leveloffset=+1]

[id="configuring-hardware-offloading-prerequisites"]
== Prerequisites

* Your cluster has at least one bare metal machine with a network interface controller that is supported for hardware offloading.
* You xref:../../networking/hardware_networks/installing-sriov-operator.adoc#installing-sr-iov-operator_installing-sriov-operator[installed the SR-IOV Network Operator].
* Your cluster uses the xref:../../networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.adoc#about-ovn-kubernetes[OVN-Kubernetes network plugin].
* In your xref:../../networking/cluster-network-operator.adoc#gatewayConfig-object_cluster-network-operator[OVN-Kubernetes network plugin configuration], the `gatewayConfig.routingViaHost` field is set to `false`.

//Configure a machine config pool for hardware offloading
include::modules/nw-sriov-hwol-configuring-machine-config-pool.adoc[leveloffset=+1]

//Configuring the SR-IOV network node policy
include::modules/nw-sriov-hwol-creating-sriov-policy.adoc[leveloffset=+1]

include::modules/nw-sriov-hwol-ref-openstack-sriov-policy.adoc[leveloffset=+2]

// Improving network traffic performance using a virtual function
include::modules/nw-sriov-hwol-improving-network-traffic-performance.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_using-vf-improve-network-traffic-performance"]
.Additional resources
* xref:../../networking/hardware_networks/configuring-sriov-device.adoc#nw-sriov-networknodepolicy-object_configuring-sriov-device[SR-IOV network node configuration object]

//Creating a Network Attachment Definition
include::modules/nw-sriov-hwol-creating-network-attachment-definition.adoc[leveloffset=+1]

//Adding the network attachment definition to your pods
include::modules/nw-sriov-hwol-adding-network-attachment-definitions-to-pods.adoc[leveloffset=+1]
