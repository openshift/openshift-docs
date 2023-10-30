:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="configuring-service-routes"]
= Configuring routes for Knative services
:context: configuring-service-routes


If you want to configure a Knative service to use your TLS certificate on {product-title}, you must disable the automatic creation of a route for the service by the {ServerlessOperatorName} and instead manually create a route for the service.

[NOTE]
====
When you complete the following procedure, the default {product-title} route in the `knative-serving-ingress` namespace is not created. However, the Knative route for the application is still created in this namespace.
====

include::modules/serverless-openshift-routes.adoc[leveloffset=+1]