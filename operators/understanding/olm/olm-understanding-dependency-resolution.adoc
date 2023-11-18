:_mod-docs-content-type: ASSEMBLY
[id="olm-understanding-dependency-resolution"]
= Operator Lifecycle Manager dependency resolution
include::_attributes/common-attributes.adoc[]
:context: olm-understanding-dependency-resolution

toc::[]

This guide outlines dependency resolution and custom resource definition (CRD) upgrade lifecycles with Operator Lifecycle Manager (OLM) in {product-title}.

include::modules/olm-dependency-resolution-about.adoc[leveloffset=+1]
include::modules/olm-properties.adoc[leveloffset=+1]
.Additional resources
* xref:../../../operators/understanding/olm/olm-understanding-dependency-resolution.adoc#olm-cel_olm-understanding-dependency-resolution[Common Expression Language (CEL) constraints]

include::modules/olm-dependencies.adoc[leveloffset=+1]
include::modules/olm-generic-constraints.adoc[leveloffset=+1]
include::modules/olm-dependency-resolution-preferences.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_dependency-resolution-preferences"]
=== Additional resources

* xref:../../../operators/understanding/olm/olm-understanding-olm.adoc#olm-cs-health_olm-understanding-olm[Catalog health requirements]

include::modules/olm-dependency-resolution-crd-upgrades.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../../operators/operator_sdk/osdk-generating-csvs.adoc#olm-dependency-resolution-adding-new-crd-version_osdk-generating-csvs[Adding a new CRD version]
* xref:../../../operators/operator_sdk/osdk-generating-csvs.adoc#olm-dependency-resolution-removing-crd-version_osdk-generating-csvs[Deprecating or removing a CRD version]

include::modules/olm-dependencies-best-practices.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* Kubernetes documentation: link:https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api_changes.md#readme[Changing the API]

include::modules/olm-dependencies-caveats.adoc[leveloffset=+1]
include::modules/olm-dependency-resolution-examples.adoc[leveloffset=+1]