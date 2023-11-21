////
This CONCEPT module included in the following assemblies:
-service_mesh/v1x/ossm-architecture.adoc
-service_mesh/v2x/ossm-architecture.adoc
////

:_mod-docs-content-type: CONCEPT
[id="ossm-kiali-architecture_{context}"]
= Kiali architecture

Kiali is based on the open source link:https://kiali.io/[Kiali project]. Kiali is composed of two components: the Kiali application and the Kiali console.

* *Kiali application* (back end) – This component runs in the container application platform and communicates with the service mesh components, retrieves and processes data, and exposes this data to the console. The Kiali application does not need storage. When deploying the application to a cluster, configurations are set in ConfigMaps and secrets.

* *Kiali console* (front end) – The Kiali console is a web application. 	The Kiali application serves the Kiali console, which then queries the back end for data to present it to the user.

In addition, Kiali depends on external services and components provided by the container application platform and Istio.

* *Red Hat Service Mesh* (Istio) - Istio is a Kiali requirement. Istio is the component that provides and controls the service mesh. Although Kiali and Istio can be installed separately, Kiali depends on Istio and will not work if it is not present. Kiali needs to retrieve Istio data and configurations, which are exposed through Prometheus and the cluster API.

* *Prometheus* - A dedicated Prometheus instance is included as part of the {SMProductName} installation. When Istio telemetry is enabled, metrics data are stored in Prometheus. Kiali uses this Prometheus data to determine the mesh topology, display metrics, calculate health, show possible problems, and so on. Kiali communicates directly with Prometheus and assumes the data schema used by Istio Telemetry. Prometheus is an Istio dependency and a hard dependency for Kiali, and many of Kiali's features will not work without Prometheus.

* *Cluster API* - Kiali uses the API of the {product-title} (cluster API) to fetch and resolve service mesh configurations. Kiali queries the cluster API to retrieve, for example, definitions for namespaces, services, deployments, pods, and other entities. Kiali also makes queries to resolve relationships between the different cluster entities. The cluster API is also queried to retrieve Istio configurations like virtual services, destination rules, route rules, gateways, quotas, and so on.

* *Jaeger* - Jaeger is optional, but is installed by default as part of the {SMProductName} installation. When you install the {JaegerShortName} as part of the default {SMProductName} installation, the Kiali console includes a tab to display distributed tracing data. Note that tracing data will not be available if you disable Istio's distributed tracing feature. Also note that user must have access to the namespace where the {SMProductShortName} control plane is installed to view tracing data.

* *Grafana* - Grafana is optional, but is installed by default as part of the {SMProductName} installation. When available, the metrics pages of Kiali display links to direct the user to the same metric in Grafana. Note that user must have access to the namespace where the {SMProductShortName} control plane is installed to view links to the Grafana dashboard and view Grafana data.
