// Module included in the following assemblies:
//
// * vvirt/post_installation_configuration/virt-node-placement-virt-components.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-node-placement-virt-components_{context}"]
= About node placement rules for {VirtProductName} components

You can use node placement rules for the following tasks:

* Deploy virtual machines only on nodes intended for virtualization workloads.
* Deploy Operators only on infrastructure nodes.
* Maintain separation between workloads.

Depending on the object, you can use one or more of the following rule types:

`nodeSelector`:: Allows pods to be scheduled on nodes that are labeled with the key-value pair or pairs that you specify in this field. The node must have labels that exactly match all listed pairs.
`affinity`:: Enables you to use more expressive syntax to set rules that match nodes with pods. Affinity also allows for more nuance in how the rules are applied. For example, you can specify that a rule is a preference, not a requirement. If a rule is a preference, pods are still scheduled when the rule is not satisfied.
`tolerations`:: Allows pods to be scheduled on nodes that have matching taints. If a taint is applied to a node, that
node only accepts pods that tolerate the taint.
