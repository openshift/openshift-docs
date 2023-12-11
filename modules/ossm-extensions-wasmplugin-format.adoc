////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: REFERENCE
[id="ossm-extensions-wasmplugin-format_{context}"]
= `WasmPlugin` container format

Istio supports Open Container Initiative (OCI) images in its Wasm Plugin mechanism. You can distribute your Wasm Plugins as a container image, and you can use the `spec.url` field to refer to a container registry location.  For example, `quay.io/my-username/my-plugin:latest`.

Because each execution environment (runtime) for a WASM module can have runtime-specific configuration parameters, a WASM image can be composed of two layers:

* *plugin.wasm* (Required) - Content layer. This layer consists of a `.wasm` binary containing the bytecode of your WebAssembly module, to be loaded by the runtime.  You must name this file `plugin.wasm`.

* *runtime-config.json* (Optional) - Configuration layer. This layer consists of a JSON-formatted string that describes metadata about the module for the target runtime. The config layer might also contain additional data, depending on the target runtime. For example, the config for a WASM Envoy Filter contains root_ids available on the filter.
