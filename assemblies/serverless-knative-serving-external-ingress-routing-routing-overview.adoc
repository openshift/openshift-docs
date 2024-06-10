:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="routing-overview"]
= Routing overview
:context: routing-overview

Knative leverages {product-title} TLS termination to provide routing for Knative services. When a Knative service is created, an {product-title} route is automatically created for the service. This route is managed by the {ServerlessOperatorName}. The {product-title} route exposes the Knative service through the same domain as the {product-title} cluster.

You can disable Operator control of {product-title} routing so that you can configure a Knative route to directly use your TLS certificates instead.

Knative routes can also be used alongside the {product-title} route to provide additional fine-grained routing capabilities, such as traffic splitting.


ifdef::openshift-enterprise[]
[id="additional-resources_serverless-configuring-routes"]
[role="_additional-resources"]
== Additional resources
* xref:../../../networking/routes/route-configuration.adoc#nw-route-specific-annotations_route-configuration[Route-specific annotations]
endif::[]
