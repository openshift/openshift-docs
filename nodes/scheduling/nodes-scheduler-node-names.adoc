:_mod-docs-content-type: ASSEMBLY
:context: nodes-scheduler-node-names
[id="nodes-scheduler-node-names"]
= Placing a pod on a specific node by name
include::_attributes/common-attributes.adoc[]

toc::[]

Use the Pod Node Constraints admission controller to ensure a pod
is deployed onto only a specified node host by assigning it a label
and specifying this in the `nodeName` setting in a pod configuration.

The Pod Node Constraints admission controller ensures that pods
are deployed onto only specified node hosts using labels
and prevents users without a specific role from using the
`nodeSelector` field to schedule pods.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-scheduler-node-names-configuring.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="nodes-scheduler-node-names-addtl-resources_{context}"]
== Additional resources

* xref:../../nodes/nodes/nodes-nodes-working.adoc#nodes-nodes-working-updating_nodes-nodes-working[Understanding how to update labels on nodes].
