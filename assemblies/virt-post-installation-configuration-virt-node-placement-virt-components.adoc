:_mod-docs-content-type: ASSEMBLY
[id="virt-node-placement-virt-components"]
= Specifying nodes for {VirtProductName} components
include::_attributes/common-attributes.adoc[]
:context: virt-node-placement-virt-components

toc::[]

The default scheduling for virtual machines (VMs) on bare metal nodes is appropriate. Optionally, you can specify the nodes where you want to deploy {VirtProductName} Operators, workloads, and controllers by configuring node placement rules.

[NOTE]
====
You can configure node placement rules for some components after installing {VirtProductName}, but virtual machines cannot be present if you want to configure node placement rules for workloads.
====

include::modules/virt-about-node-placement-virt-components.adoc[leveloffset=+1]

include::modules/virt-applying-node-placement-rules.adoc[leveloffset=+1]

include::modules/virt-node-placement-rule-examples.adoc[leveloffset=+1]

[id="additional-resources_virt-node-placement-virt-components"]
[role="_additional-resources"]
== Additional resources
* xref:../../virt/virtual_machines/advanced_vm_management/virt-specifying-nodes-for-vms.adoc#virt-specifying-nodes-for-vms[Specifying nodes for virtual machines]
* xref:../../nodes/scheduling/nodes-scheduler-node-selectors.adoc#nodes-scheduler-node-selectors[Placing pods on specific nodes using node selectors]
* xref:../../nodes/scheduling/nodes-scheduler-node-affinity.adoc#nodes-scheduler-node-affinity[Controlling pod placement on nodes using node affinity rules]
* xref:../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations[Controlling pod placement using node taints]