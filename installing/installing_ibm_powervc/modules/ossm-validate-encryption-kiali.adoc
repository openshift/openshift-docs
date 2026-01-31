////
This module included in the following assemblies:
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc
////
:_mod-docs-content-type: CONCEPT
[id="ossm-validating-sidecar_{context}"]
= Validating encryption with Kiali

The Kiali console offers several ways to validate whether or not your applications, services, and workloads have mTLS encryption enabled.

.Masthead icon mesh-wide mTLS enabled
image::ossm-kiali-masthead-mtls-enabled.png[mTLS enabled]

At the right side of the masthead, Kiali shows a lock icon when the mesh has strictly enabled mTLS for the whole service mesh. It means that all communications in the mesh use mTLS.

.Masthead icon mesh-wide mTLS partially enabled
image::ossm-kiali-masthead-mtls-partial.png[mTLS partially enabled]

Kiali displays a hollow lock icon when either the mesh is configured in `PERMISSIVE` mode or there is a error in the mesh-wide mTLS configuration.

.Security badge
image::ossm-kiali-graph-badge-security.png[Security badge]

The *Graph* page has the option to display a *Security* badge on the graph edges to indicate that mTLS is enabled.  To enable security badges on the graph, from the *Display* menu, under *Show Badges*, select the *Security* checkbox.  When an edge shows a lock icon, it means at least one request with mTLS enabled is present.  In case there are both mTLS and non-mTLS requests, the side-panel will show the percentage of requests that use mTLS.

The *Applications Detail Overview* page displays a *Security* icon on the graph edges where at least one request with mTLS enabled is present.

The *Workloads Detail Overview* page displays a *Security* icon on the graph edges where at least one request with mTLS enabled is present.

The *Services Detail Overview* page displays a *Security* icon on the graph edges where at least one request with mTLS enabled is present.  Also note that Kiali displays a lock icon in the *Network* section next to ports that are configured for mTLS.
