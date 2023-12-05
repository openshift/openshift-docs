// Module included in the following assemblies:
//
// * virt/virtual_machines/advanced_vm_management/virt-specifying-nodes-for-vms.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-node-placement-vms_{context}"]
= About node placement for virtual machines

To ensure that virtual machines (VMs) run on appropriate nodes, you can configure node placement rules. You might want to do this if:

* You have several VMs. To ensure fault tolerance, you want them to run on different nodes.
* You have two chatty VMs. To avoid redundant inter-node routing, you want the VMs to run on the same node.
* Your VMs require specific hardware features that are not present on all available nodes.
* You have a pod that adds capabilities to a node, and you want to place a VM on that node so that it can use those capabilities.

[NOTE]
====
Virtual machine placement relies on any existing node placement rules for workloads. If workloads are excluded from specific nodes on the component level, virtual machines cannot be placed on those nodes.
====

You can use the following rule types in the `spec` field of a `VirtualMachine` manifest:

`nodeSelector`:: Allows virtual machines to be scheduled on nodes that are labeled with the key-value pair or pairs that you specify in this field. The node must have labels that exactly match all listed pairs.
`affinity`:: Enables you to use more expressive syntax to set rules that match nodes with virtual machines. For example, you can specify that a rule is a preference, rather than a hard requirement, so that virtual machines are still scheduled if the rule is not satisfied. Pod affinity, pod anti-affinity, and node affinity are supported for virtual machine placement. Pod affinity works for virtual machines because the `VirtualMachine` workload type is based on the `Pod` object.
`tolerations`:: Allows virtual machines to be scheduled on nodes that have matching taints. If a taint is applied to a node, that node only accepts virtual machines that tolerate the taint.

+
[NOTE]
====
Affinity rules only apply during scheduling. {product-title} does not reschedule running workloads if the constraints are no longer met.
====
