////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: REFERENCE
[id="ossm-wasm-ref-smextension_{context}"]
= ServiceMeshExtension reference

The ServiceMeshExtension API provides a mechanism to extend the functionality provided by the Istio proxy through WebAssembly filters. There are two parts to writing a WebAssembly extension:

. Write your extension using an SDK that exposes the proxy-wasm API and compile it to a WebAssembly module.
. Package it into a container.

[NOTE]
====
When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API, which was deprecated in {SMProductName} version 2.2, was removed in {SMProductName} version 2.3.
====

.ServiceMeshExtension Field Reference
[options="header"]
[cols="a, a"]
|===
| Field | Description

|metadata.namespace
|The `metadata.namespace` field of a `ServiceMeshExtension` source has a special semantic: if it equals the Control Plane Namespace, the extension will be applied to all workloads in the Service Mesh that match its `workloadSelector` value. When deployed to any other Mesh Namespace, it will only be applied to workloads in that same Namespace.

|spec.workloadSelector
|The `spec.workloadSelector` field has the same semantic as the `spec.selector` field of the link:https://istio.io/v1.6/docs/reference/config/networking/gateway/#Gateway[Istio Gateway resource]. It will match a workload based on its Pod labels. If no `workloadSelector` value is specified, the extension will be applied to all workloads in the namespace.

|spec.config
|This is a structured field that will be handed over to the extension, with the semantics dependent on the extension you are deploying.

|spec.image
|A container image URI pointing to the image that holds the extension.

|spec.phase
|The phase determines where in the filter chain the extension is injected, in relation to existing Istio functionality like Authentication, Authorization and metrics generation. Valid values are: PreAuthN, PostAuthN, PreAuthZ, PostAuthZ, PreStats, PostStats. This field defaults to the value set in the `manifest.yaml` file of the extension, but can be overwritten by the user.

|spec.priority
|If multiple extensions with the same `spec.phase` value are applied to the same workload instance, the `spec.priority` value determines the ordering of execution. Extensions with higher priority will be executed first. This allows for inter-dependent extensions. This field defaults to the value set in the `manifest.yaml` file of the extension, but can be overwritten by the user.
|===
