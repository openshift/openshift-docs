////
This CONCEPT module included in the following assemblies:
-service_mesh/v1x/ossm-vs-community.adoc
-service_mesh/v2x/ossm-vs-community.adoc
////

[id="ossm-jaeger-service-mesh_{context}"]
= Distributed tracing and service mesh

Installing the {JaegerShortName} with the Service Mesh on {product-title} differs from community Jaeger installations in multiple ways. These modifications are sometimes necessary to resolve issues, provide additional features, or to handle differences when deploying on {product-title}.

* Distributed tracing has been enabled by default for {SMProductShortName}.
* Ingress has been enabled by default for {SMProductShortName}.
* The name for the Zipkin port name has changed to `jaeger-collector-zipkin` (from `http`)
* Jaeger uses Elasticsearch for storage by default when you select either the `production` or `streaming` deployment option.
* The community version of Istio provides a generic "tracing" route. {SMProductName} uses a "jaeger" route that is installed by the {JaegerName} Operator and is already protected by OAuth.
* {SMProductName} uses a sidecar for the Envoy proxy, and Jaeger also uses a sidecar, for the Jaeger agent.
These two sidecars are configured separately and should not be confused with each other. The proxy sidecar creates spans related to the pod's ingress and egress traffic. The agent sidecar receives the spans emitted by the application and sends them to the Jaeger Collector.
