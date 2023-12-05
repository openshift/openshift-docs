:_mod-docs-content-type: ASSEMBLY
:context: nodes-scheduler-taints-tolerations
[id="nodes-scheduler-taints-tolerations"]
= Controlling pod placement using node taints
include::_attributes/common-attributes.adoc[]

toc::[]



Taints and tolerations allow the node to control which pods should (or should not) be scheduled on them.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-scheduler-taints-tolerations-about.adoc[leveloffset=+1]

include::modules/nodes-scheduler-taints-tolerations-adding.adoc[leveloffset=+1]

include::modules/nodes-scheduler-taints-tolerations-adding-machineset.adoc[leveloffset=+2]

include::modules/nodes-scheduler-taints-tolerations-binding.adoc[leveloffset=+2]

include::modules/nodes-scheduler-taints-tolerations-projects.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* Adding taints and tolerations xref:../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations-adding_nodes-scheduler-taints-tolerations[manually to nodes] or xref:../../nodes/scheduling/nodes-scheduler-taints-tolerations.adoc#nodes-scheduler-taints-tolerations-adding-machineset_nodes-scheduler-taints-tolerations[with compute machine sets]
ifndef::openshift-rosa,openshift-dedicated[]
* xref:../../nodes/scheduling/nodes-scheduler-node-selectors.adoc#nodes-scheduler-node-selectors-project_nodes-scheduler-node-selectors[Creating project-wide node selectors]
* xref:../../operators/admin/olm-adding-operators-to-cluster.adoc#olm-pod-placement_olm-adding-operators-to-a-cluster[Pod placement of Operator workloads]
endif::openshift-rosa,openshift-dedicated[]

include::modules/nodes-scheduler-taints-tolerations-special.adoc[leveloffset=+2]

include::modules/nodes-scheduler-taints-tolerations-removing.adoc[leveloffset=+1]

//Removed per upstream docs modules/nodes-scheduler-taints-tolerations-evictions.adoc[leveloffset=+1]
