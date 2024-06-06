////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: REFERENCE
[id="ossm-extensions-smextension-format_{context}"]
= `ServiceMeshExtension` container format

You must have a `.wasm` file containing the bytecode of your WebAssembly module, and a `manifest.yaml` file in the root of the container filesystem to make your container image a valid extension image.

[NOTE]
====
When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in {SMProductName} version 2.2 and was removed in {SMProductName} version 2.3.
====

.manifest.yaml
[source,yaml]
----
schemaVersion: 1

name: <your-extension>
description: <description>
version: 1.0.0
phase: PreAuthZ
priority: 100
module: extension.wasm
----

.Field Reference for manifest.yml
[options="header"]
[cols="a, a, a"]
|===
| Field | Description |Required

|schemaVersion
|Used for versioning of the manifest schema. Currently the only possible value is `1`.
|This is a required field.

|name
|The name of your extension.
|This field is just metadata and currently unused.

|description
|The description of your extension.
|This field is just metadata and currently unused.

|version
|The version of your extension.
|This field is just metadata and currently unused.

|phase
|The default execution phase of your extension.
|This is a required field.

|priority
|The default priority of your extension.
|This is a required field.

|module
|The relative path from the container filesystem's root to your WebAssembly module.
|This is a required field.
|===
