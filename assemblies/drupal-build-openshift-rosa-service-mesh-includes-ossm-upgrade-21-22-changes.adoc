// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-upgrade-21-22-changes_{context}"]
= Upgrade changes from version 2.1 to version 2.2

Upgrading the {SMProductShortName} control plane from version 2.1 to 2.2 introduces the following behavioral changes:

* The `istio-node` DaemonSet is renamed to `istio-cni-node` to match the name in upstream Istio.

* Istio 1.10 updated Envoy to send traffic to the application container using `eth0` rather than `lo` by default.

* This release adds support for the `WasmPlugin` API and deprecates the `ServiceMeshExtension` API.
