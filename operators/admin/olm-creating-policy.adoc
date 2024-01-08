:_mod-docs-content-type: ASSEMBLY
[id="olm-creating-policy"]
= Allowing non-cluster administrators to install Operators
include::_attributes/common-attributes.adoc[]
:context: olm-creating-policy

toc::[]

Cluster administrators can use _Operator groups_ to allow regular users to install Operators.

[role="_additional-resources"]
.Additional resources

* xref:../../operators/understanding/olm/olm-understanding-operatorgroups.adoc#olm-understanding-operatorgroups[Operator groups]

include::modules/olm-policy-understanding.adoc[leveloffset=+1]
include::modules/olm-policy-scenarios.adoc[leveloffset=+2]
include::modules/olm-policy-workflow.adoc[leveloffset=+2]

include::modules/olm-policy-scoping-operator-install.adoc[leveloffset=+1]
include::modules/olm-policy-fine-grained-permissions.adoc[leveloffset=+2]

include::modules/olm-policy-catalog-access.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources

* xref:../../operators/admin/olm-managing-custom-catalogs.adoc#olm-restricted-networks-operatorhub_olm-managing-custom-catalogs[Disabling the default OperatorHub catalog sources]
* xref:../../operators/admin/olm-managing-custom-catalogs.adoc#olm-creating-catalog-from-index_olm-managing-custom-catalogs[Adding a catalog source to a cluster]

include::modules/olm-policy-troubleshooting.adoc[leveloffset=+1]
