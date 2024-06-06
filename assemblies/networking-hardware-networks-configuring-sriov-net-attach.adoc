:_mod-docs-content-type: ASSEMBLY
[id="configuring-sriov-net-attach"]
= Configuring an SR-IOV Ethernet network attachment
include::_attributes/common-attributes.adoc[]
:context: configuring-sriov-net-attach

toc::[]

You can configure an Ethernet network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

include::modules/nw-sriov-network-object.adoc[leveloffset=+1]
include::modules/nw-multus-ipam-object.adoc[leveloffset=+2]
include::modules/nw-multus-configure-dualstack-ip-address.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../networking/multiple_networks/attaching-pod.html#nw-multus-add-pod_attaching-pod[Attaching a pod to an additional network]

include::modules/nw-sriov-network-attachment.adoc[leveloffset=+1]

[id="configuring-sriov-net-attach-next-steps"]
== Next steps

* xref:../../networking/hardware_networks/add-pod.adoc#add-pod[Adding a pod to an SR-IOV additional network]

[role="_additional-resources"]
[id="configuring-sriov-net-attach-additional-resources"]
== Additional resources

 * xref:../../networking/hardware_networks/configuring-sriov-device.adoc#configuring-sriov-device[Configuring an SR-IOV network device]
