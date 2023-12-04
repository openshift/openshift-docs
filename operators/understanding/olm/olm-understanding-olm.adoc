:_mod-docs-content-type: ASSEMBLY
[id="olm-understanding-olm"]
= Operator Lifecycle Manager concepts and resources
include::_attributes/common-attributes.adoc[]
:context: olm-understanding-olm

toc::[]

This guide provides an overview of the concepts that drive Operator Lifecycle Manager (OLM) in {product-title}.

include::modules/olm-overview.adoc[leveloffset=+1]
include::modules/olm-crds.adoc[leveloffset=+1]
include::modules/olm-csv.adoc[leveloffset=+2]
include::modules/olm-catalogsource.adoc[leveloffset=+2]
[role="_additional-resources"]
.Additional resources

* xref:../../../operators/understanding/olm-understanding-operatorhub.adoc#olm-understanding-operatorhub[Understanding OperatorHub]
* xref:../../../operators/understanding/olm-rh-catalogs.adoc#olm-rh-catalogs[Red Hat-provided Operator catalogs]
* xref:../../../operators/admin/olm-managing-custom-catalogs.adoc#olm-creating-catalog-from-index_olm-managing-custom-catalogs[Adding a catalog source to a cluster]
* xref:../../../operators/understanding/olm/olm-understanding-dependency-resolution.adoc#olm-dependency-catalog-priority_olm-understanding-dependency-resolution[Catalog priority]
* xref:../../../operators/admin/olm-status.adoc#olm-cs-status-cli_olm-status[Viewing Operator catalog source status by using the CLI]
// This xref points to a topic that is not currently included in the OSD/ROSA docs.
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../authentication/understanding-and-managing-pod-security-admission.adoc#understanding-and-managing-pod-security-admission[Understanding and managing pod security admission]
endif::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/admin/olm-cs-podsched.adoc#olm-cs-podsched[Catalog source pod scheduling]

include::modules/olm-catalogsource-image-template.adoc[leveloffset=+3]
include::modules/olm-cs-health.adoc[leveloffset=+3]
ifndef::openshift-dedicated,openshift-rosa[]
[role="_additional-resources"]
.Additional resources

* xref:../../../operators/admin/olm-managing-custom-catalogs.adoc#olm-removing-catalogs_olm-managing-custom-catalogs[Removing custom catalogs]
* xref:../../../operators/admin/olm-managing-custom-catalogs.adoc#olm-restricted-networks-operatorhub_olm-managing-custom-catalogs[Disabling the default OperatorHub catalog sources]
endif::openshift-dedicated,openshift-rosa[]

include::modules/olm-subscription.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/understanding/olm/olm-colocation.adoc#olm-colocation[Multitenancy and Operator colocation]
endif::openshift-dedicated,openshift-rosa[]
* xref:../../../operators/admin/olm-status.adoc#olm-status-viewing-cli_olm-status[Viewing Operator subscription status by using the CLI]

include::modules/olm-installplan.adoc[leveloffset=+2]

ifndef::openshift-dedicated,openshift-rosa[]
[role="_additional-resources"]
.Additional resources

* xref:../../../operators/understanding/olm/olm-colocation.adoc#olm-colocation[Multitenancy and Operator colocation]
* xref:../../../operators/admin/olm-creating-policy.adoc#olm-creating-policy[Allowing non-cluster administrators to install Operators]
endif::openshift-dedicated,openshift-rosa[]

include::modules/olm-operatorgroups-about.adoc[leveloffset=+2]
.Additional resources

* xref:../../../operators/understanding/olm/olm-understanding-operatorgroups.adoc#olm-understanding-operatorgroups[Operator groups]

include::modules/olm-operatorconditions-about.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources

* xref:../../../operators/understanding/olm/olm-operatorconditions.adoc#olm-operatorconditions[Operator conditions]
