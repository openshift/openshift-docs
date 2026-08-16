// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-upgrade-22-23-changes_{context}"]
= Upgrade changes from version 2.2 to version 2.3

Upgrading the {SMProductShortName} control plane from version 2.2 to 2.3 introduces the following behavioral changes:

* This release requires use of the `WasmPlugin` API. Support for the `ServiceMeshExtension` API, which was deprecated in 2.2, has now been removed. If you attempt to upgrade while using the `ServiceMeshExtension` API, then the upgrade fails.
