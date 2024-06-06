:_mod-docs-content-type: ASSEMBLY
[id="configuring-sriov-ib-attach"]
= Configuring an SR-IOV InfiniBand network attachment
include::_attributes/common-attributes.adoc[]
:context: configuring-sriov-ib-attach

toc::[]

You can configure an InfiniBand (IB) network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

include::modules/nw-sriov-ibnetwork-object.adoc[leveloffset=+1]
include::modules/nw-multus-ipam-object.adoc[leveloffset=+2]

include::modules/nw-multus-configure-dualstack-ip-address.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../networking/multiple_networks/attaching-pod.html#nw-multus-add-pod_attaching-pod[Attaching a pod to an additional network]

include::modules/nw-sriov-network-attachment.adoc[leveloffset=+1]

[id="configuring-sriov-ib-attach-next-steps"]
== Next steps

* xref:../../networking/hardware_networks/add-pod.adoc#add-pod[Adding a pod to an SR-IOV additional network]

[role="_additional-resources"]
[id="configuring-sriov-ib-attach-additional-resources"]
== Additional resources

 * xref:../../networking/hardware_networks/configuring-sriov-device.adoc#configuring-sriov-device[Configuring an SR-IOV network device]
