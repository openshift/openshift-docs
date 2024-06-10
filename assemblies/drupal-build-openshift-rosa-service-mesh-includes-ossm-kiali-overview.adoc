////
This CONCEPT module included in the following assemblies:
-service_mesh/v1x/ossm-architecture.adoc
-service_mesh/v2x/ossm-architecture.adoc
////

:_mod-docs-content-type: CONCEPT
[id="ossm-kiali-overview_{context}"]
= Kiali overview

Kiali provides observability into the {SMProductShortName} running on {product-title}. Kiali helps you define, validate, and observe your Istio service mesh. It helps you to understand the structure of your service mesh by inferring the topology, and also provides information about the health of your service mesh.

Kiali provides an interactive graph view of your namespace in real time that provides visibility into features like circuit breakers, request rates, latency, and even graphs of traffic flows. Kiali offers insights about components at different levels, from Applications to Services and Workloads, and can display the interactions with contextual information and charts on the selected graph node or edge. Kiali also provides the ability to validate your Istio configurations, such as gateways, destination rules, virtual services, mesh policies, and more. Kiali provides detailed metrics, and a basic Grafana integration is available for advanced queries. Distributed tracing is provided by integrating Jaeger into the Kiali console.

Kiali is installed by default as part of the {SMProductName}.
