:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="customize-labels-annotations-routes"]
= Customizing labels and annotations
:context: customize-labels-annotations-routes


toc::[]

{product-title} routes support the use of custom labels and annotations, which you can configure by modifying the `metadata` spec of a Knative service. Custom labels and annotations are propagated from the service to the Knative route, then to the Knative ingress, and finally to the {product-title} route.

include::modules/serverless-customize-labels-annotations-routes.adoc[leveloffset=+1]

