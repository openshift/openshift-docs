:_mod-docs-content-type: ASSEMBLY
[id="virt-specifying-nodes-for-vms"]
= Specifying nodes for virtual machines
include::_attributes/common-attributes.adoc[]
:context: virt-specifying-nodes-for-vms

toc::[]

You can place virtual machines (VMs) on specific nodes by using node placement rules.

include::modules/virt-about-node-placement-vms.adoc[leveloffset=+1]

[id="node-placement-examples_{context}"]
== Node placement examples

The following example YAML file snippets use `nodePlacement`, `affinity`, and `tolerations` fields to customize node placement for virtual machines.

include::modules/virt-example-vm-node-placement-node-selector.adoc[leveloffset=+2]
include::modules/virt-example-vm-node-placement-pod-affinity.adoc[leveloffset=+2]
include::modules/virt-example-vm-node-placement-node-affinity.adoc[leveloffset=+2]
include::modules/virt-example-vm-node-placement-tolerations.adoc[leveloffset=+2]

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* xref:../../../virt/post_installation_configuration/virt-node-placement-virt-components.adoc#virt-node-placement-virt-components[Specifying nodes for virtualization components]
* xref:../../../nodes/scheduling/nodes-scheduler-node-selectors.adoc#nodes-scheduler-node-selectors[Placing pods on specific nodes using node selectors]
* xref:../../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity[Controlling pod placement on nodes using node affinity rules]
* xref:../../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations[Controlling pod placement using node taints]
