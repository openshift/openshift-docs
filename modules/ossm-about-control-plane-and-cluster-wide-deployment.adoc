// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-smcp.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-about-control-plane-and-cluster-wide-deployment_{context}"]
= About control plane and cluster-wide deployments

A cluster-wide deployment contains a {SMProductShortName} Control Plane that monitors resources for an entire cluster. Monitoring resources for an entire cluster closely resembles Istio functionality in that the control plane uses a single query across all namespaces to monitor Istio and Kubernetes resources. As a result, cluster-wide deployments decrease the number of requests sent to the API server.

You can configure the {SMProductShortName} Control Plane for cluster-wide deployments using either the {product-title} web console or the CLI.