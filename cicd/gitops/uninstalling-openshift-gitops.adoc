:_mod-docs-content-type: ASSEMBLY
[id="uninstalling-openshift-gitops"]
= Uninstalling OpenShift GitOps
include::_attributes/common-attributes.adoc[]
:context: uninstalling-openshift-gitops

toc::[]

Uninstalling the {gitops-title} Operator is a two-step process:

. Delete the Argo CD instances that were added under the default namespace of the {gitops-title} Operator.
. Uninstall the {gitops-title} Operator.

Uninstalling only the Operator will not remove the Argo CD instances created.

include::modules/go-deleting-argocd-instance.adoc[leveloffset=+1]

include::modules/go-uninstalling-gitops-operator.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* You can learn more about uninstalling Operators on {product-title} in the xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster] section.
