:_mod-docs-content-type: ASSEMBLY
:_mod-docs-content-type: ASSEMBLY
[id="crd-extending-api-with-crds"]
= Extending the Kubernetes API with custom resource definitions
include::_attributes/common-attributes.adoc[]
:context: crd-extending-api-with-crds

toc::[]

Operators use the Kubernetes extension mechanism, custom resource definitions (CRDs), so that custom objects managed by the Operator look and act just like the built-in, native Kubernetes objects. This guide describes how cluster administrators can extend their {product-title} cluster by creating and managing CRDs.

include::modules/crd-custom-resource-definitions.adoc[leveloffset=+1]
include::modules/crd-creating-crds.adoc[leveloffset=+1]
include::modules/crd-creating-aggregated-cluster-roles.adoc[leveloffset=+1]
include::modules/crd-creating-custom-resources-from-file.adoc[leveloffset=+1]
include::modules/crd-inspecting-custom-resources.adoc[leveloffset=+1]
