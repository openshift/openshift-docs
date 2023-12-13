:_mod-docs-content-type: ASSEMBLY
[id="olm-understanding-operatorgroups"]
= Operator groups
include::_attributes/common-attributes.adoc[]
:context: olm-understanding-operatorgroups

toc::[]

This guide outlines the use of Operator groups with Operator Lifecycle Manager (OLM) in {product-title}.

include::modules/olm-operatorgroups-about.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-membership.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-target-namespace.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-csv-annotations.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-provided-apis-annotations.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-rbac.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-copied-csvs.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-static.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-intersections.adoc[leveloffset=+1]
include::modules/olm-operatorgroups-limitations.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/understanding/olm/olm-colocation.adoc#olm-colocation[Operator Lifecycle Manager (OLM) -> Multitenancy and Operator colocation]
endif::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/understanding/olm-multitenancy.adoc#olm-multitenancy[Operators in multitenant clusters]
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/admin/olm-creating-policy.adoc#olm-creating-policy[Allowing non-cluster administrators to install Operators]
endif::openshift-dedicated,openshift-rosa[]

include::modules/olm-operatorgroups-troubleshooting.adoc[leveloffset=+1]
