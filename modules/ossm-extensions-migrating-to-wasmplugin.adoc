////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: PROCEDURE
[id="ossm-extensions-migrating-to-wasmplugin_{context}"]
= Migrating to `WasmPlugin` resources

To upgrade your WebAssembly extensions from the `ServiceMeshExtension` API to the `WasmPlugin` API, you rename your plugin file.

.Prerequisites

* `ServiceMeshControlPlane` is upgraded to version 2.2 or later.

.Procedure

. Update your container image. If the plugin is already in `/plugin.wasm` inside the container, skip to the next step.  If not:

.. Ensure the plugin file is named `plugin.wasm`. You must name the extension file `plugin.wasm`.

.. Ensure the plugin file is located in the root (/) directory. You must store extension files in the root of the container filesystem..

.. Rebuild your container image and push it to a container registry.

. Remove the `ServiceMeshExtension` resource and create a `WasmPlugin` resource that refers to the new container image you built.
