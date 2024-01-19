:_mod-docs-content-type: ASSEMBLY
[id="nodes-nodes-resources-configuring"]
= Allocating resources for nodes in an {product-title} cluster
include::_attributes/common-attributes.adoc[]
:context: nodes-nodes-resources-configuring

toc::[]

To provide more reliable scheduling and minimize node resource overcommitment, reserve a portion of the CPU and memory resources for use by the underlying node components, such as `kubelet` and `kube-proxy`, and the remaining system components, such as `sshd` and `NetworkManager`. By specifying the resources to reserve, you provide the scheduler with more information about the remaining CPU and memory resources that a node has available for use by pods. You can allow {product-title} to xref:../../nodes/nodes/nodes-nodes-resources-configuring.adoc#nodes-nodes-resources-configuring-auto_nodes-nodes-resources-configuring[automatically determine the optimal `system-reserved` CPU and memory resources] for your nodes or you can xref:../../nodes/nodes/nodes-nodes-resources-configuring.adoc#nodes-nodes-resources-configuring-setting_nodes-nodes-resources-configuring[manually determine and set the best resources] for your nodes.

[IMPORTANT]
====
To manually set resource values, you must use a kubelet config CR. You cannot use a machine config CR.
====

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

include::modules/nodes-nodes-resources-configuring-about.adoc[leveloffset=+1]

include::modules/nodes-nodes-resources-configuring-auto.adoc[leveloffset=+1]

include::modules/nodes-nodes-resources-configuring-setting.adoc[leveloffset=+1]

////
[role="_additional-resources"]
== Additional resources

The ephemeral storage management feature is disabled by default. To enable this
feature,

See /install_config/configuring_ephemeral.adoc#install-config-configuring-ephemeral-storage[configuring for
ephemeral storage].

See /dev_guide/compute_resources.adoc#dev-guide-compute-resources[Compute Resources] for more
details.

#update these links when the links become available#

////
