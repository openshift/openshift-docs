:_mod-docs-content-type: ASSEMBLY
[id="olm-status"]
= Viewing Operator status
include::_attributes/common-attributes.adoc[]
:context: olm-status

toc::[]

Understanding the state of the system in Operator Lifecycle Manager (OLM) is important for making decisions about and debugging problems with installed Operators. OLM provides insight into subscriptions and related catalog sources regarding their state and actions performed. This helps users better understand the healthiness of their Operators.

include::modules/olm-status-conditions.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-refresh-subs_olm-deleting-operators-from-a-cluster[Refreshing failing subscriptions]

include::modules/olm-status-viewing-cli.adoc[leveloffset=+1]
include::modules/olm-cs-status-cli.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../operators/understanding/olm/olm-understanding-olm.adoc#olm-catalogsource_olm-understanding-olm[Operator Lifecycle Manager concepts and resources -> Catalog source]
* gRPC documentation: link:https://grpc.github.io/grpc/core/md_doc_connectivity-semantics-and-api.html[States of Connectivity]
ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../operators/admin/olm-managing-custom-catalogs.adoc#olm-accessing-images-private-registries_olm-managing-custom-catalogs[Accessing images for Operators from private registries]
endif::openshift-dedicated,openshift-rosa[]
