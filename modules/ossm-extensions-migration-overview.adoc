////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: CONCEPT
[id="ossm-extensions-migration-overview_{context}"]
= Migrating from `ServiceMeshExtension` to `WasmPlugin` resources

The `ServiceMeshExtension` API, which was deprecated in {SMProductName} version 2.2, was removed in {SMProductName} version 2.3. If you are using the `ServiceMeshExtension` API, you must migrate to the `WasmPlugin` API to continue using your WebAssembly extensions.

The APIs are very similar. The migration consists of two steps:

. Renaming your plugin file and updating the module packaging.

. Creating a `WasmPlugin` resource that references the updated container image.

[id="ossm-extensions-migration-api-changes_{context}"]
== API changes

The new `WasmPlugin` API is similar to the `ServiceMeshExtension`, but with a few differences, especially in the field names:


.Field changes between `ServiceMeshExtensions` and `WasmPlugin`
[options="header"]
[cols="a, a"]
|===
|ServiceMeshExtension |WasmPlugin
|`spec.config`
|`spec.pluginConfig`

|`spec.workloadSelector`
|`spec.selector`

|`spec.image`
|`spec.url`

//Question about the case here, is WasmPlugin app caps?
|`spec.phase` valid values: PreAuthN, PostAuthN, PreAuthZ, PostAuthZ, PreStats, PostStats
|`spec.phase` valid values: <empty>, AUTHN, AUTHZ, STATS
|===

The following is an example of how a `ServiceMeshExtension` resource could be converted into a `WasmPlugin` resource.

.ServiceMeshExtension resource
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshExtension
metadata:
  name: header-append
  namespace: istio-system
spec:
  workloadSelector:
    labels:
      app: httpbin
  config:
    first-header: some-value
    another-header: another-value
  image: quay.io/maistra-dev/header-append-filter:2.2
  phase: PostAuthZ
  priority: 100
----

.New WasmPlugin resource equivalent to the ServiceMeshExtension above
[source,yaml]
----
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: header-append
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: httpbin
  url: oci://quay.io/maistra-dev/header-append-filter:2.2
  phase: STATS
  pluginConfig:
    first-header: some-value
    another-header: another-value
----

[id="ossm-extensions-migration-format-changes_{context}"]
== Container image format changes

The new `WasmPlugin` container image format is similar to the `ServiceMeshExtensions`, with the following differences:

* The `ServiceMeshExtension` container format required a metadata file named `manifest.yaml` in the root directory of the container filesystem. The `WasmPlugin` container format does not require a `manifest.yaml` file.

* The `.wasm` file (the actual plugin) that previously could have any filename now must be named `plugin.wasm` and must be located in the root directory of the container filesystem.
