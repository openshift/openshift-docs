:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-pipelines"]
= Uninstalling {pipelines-shortname}
include::_attributes/common-attributes.adoc[]
:context: uninstalling-pipelines

toc::[]

Cluster administrators can uninstall the {pipelines-title} Operator by performing the following steps:

. Delete the Custom Resources (CRs) that were added by default when you installed the {pipelines-title} Operator.
. Delete the CRs of the optional components such as {tekton-hub} that depend on the Operator.
+
[CAUTION]
====
If you uninstall the Operator without removing the CRs of optional components, you cannot remove them later.
====
. Uninstall the {pipelines-title} Operator.

Uninstalling only the Operator will not remove the {pipelines-title} components created by default when the Operator is installed.

include::modules/op-deleting-the-pipelines-component-and-custom-resources.adoc[leveloffset=+1]

include::modules/op-uninstalling-the-pipelines-operator.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* You can learn more about uninstalling Operators on {product-title} in the xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[deleting Operators from a cluster] section.
