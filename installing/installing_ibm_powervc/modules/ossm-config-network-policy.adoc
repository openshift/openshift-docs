////
This CONCEPT module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc
////

:_mod-docs-content-type: CONCEPT
[id="ossm-config-network-policy_{context}"]

== Setting the correct network policy

{SMProductShortName} creates network policies in the {SMProductShortName} control plane and member namespaces to allow traffic between them. Before you deploy, consider the following conditions to ensure the services in your service mesh that were previously exposed through an {product-title} route.

* Traffic into the service mesh must always go through the ingress-gateway for Istio to work properly.
* Deploy services external to the service mesh in separate namespaces that are not in any service mesh.
* Non-mesh services that need to be deployed within a service mesh enlisted namespace should label their deployments `maistra.io/expose-route: "true"`, which ensures {product-title} routes to these services still work.
