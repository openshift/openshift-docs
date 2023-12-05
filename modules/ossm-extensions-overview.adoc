////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: CONCEPT
[id="ossm-extensions-overview_{context}"]
= WebAssembly modules overview

WebAssembly modules can be run on many platforms, including proxies, and have broad language support, fast execution, and a sandboxed-by-default security model.

{SMProductName} extensions are link:https://www.envoyproxy.io/docs/envoy/v1.20.0/intro/arch_overview/http/http_filters#arch-overview-http-filters[Envoy HTTP Filters], giving them a wide range of capabilities:

* Manipulating the body and headers of requests and responses.
* Out-of-band HTTP requests to services not in the request path, such as authentication or policy checking.
* Side-channel data storage and queues for filters to communicate with each other.

[NOTE]
====
When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in {SMProductName} version 2.2 and was removed in {SMProductName} version 2.3.
====

There are two parts to writing a {SMProductName} extension:

. You must write your extension using an SDK that exposes the link:https://github.com/proxy-wasm/spec[proxy-wasm API] and compile it to a WebAssembly module.
. You must then package the module into a container.

.Supported languages

You can use any language that compiles to WebAssembly bytecode to write a {SMProductName} extension, but the following languages have existing SDKs that expose the proxy-wasm API so that it can be consumed directly.

.Supported languages
|===
| Language | Maintainer | Repository

| AssemblyScript
| solo.io
| link:https://github.com/solo-io/proxy-runtime[solo-io/proxy-runtime]

| C++
| proxy-wasm team (Istio Community)
| link:https://github.com/proxy-wasm/proxy-wasm-cpp-sdk[proxy-wasm/proxy-wasm-cpp-sdk]

| Go
| tetrate.io
| link:https://github.com/tetratelabs/proxy-wasm-go-sdk[tetratelabs/proxy-wasm-go-sdk]

| Rust
| proxy-wasm team (Istio Community)
| link:https://github.com/proxy-wasm/proxy-wasm-rust-sdk[proxy-wasm/proxy-wasm-rust-sdk]
|===
