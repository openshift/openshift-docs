////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: REFERENCE
[id="ossm-wasm-ref-wasmplugin_{context}"]
= WasmPlugin API reference

The WasmPlugins API provides a mechanism to extend the functionality provided by the Istio proxy through WebAssembly filters.

You can deploy multiple WasmPlugins. The `phase` and `priority` settings determine the order of execution (as part of Envoy's filter chain), allowing the configuration of complex interactions between user-supplied WasmPlugins and Istio’s internal filters.

In the following example, an authentication filter implements an OpenID flow and populates the Authorization header with a JSON Web Token (JWT). Istio authentication consumes this token and deploys it to the ingress gateway. The WasmPlugin file lives in the proxy sidecar filesystem. Note the field `url`.

[source,yaml]
----
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: openid-connect
  namespace: istio-ingress
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: file:///opt/filters/openid.wasm
  sha256: 1ef0c9a92b0420cf25f7fe5d481b231464bc88f486ca3b9c83ed5cc21d2f6210
  phase: AUTHN
  pluginConfig:
    openid_server: authn
    openid_realm: ingress
----

Below is the same example, but this time an Open Container Initiative (OCI) image is used instead of a file in the filesystem. Note the fields `url`, `imagePullPolicy`, and `imagePullSecret`.

[source,yaml]
----
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: openid-connect
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://private-registry:5000/openid-connect/openid:latest
  imagePullPolicy: IfNotPresent
  imagePullSecret: private-registry-pull-secret
  phase: AUTHN
  pluginConfig:
    openid_server: authn
    openid_realm: ingress
----

.WasmPlugin Field Reference
[options="header"]
[cols="a, a, a, a"]
|===
| Field | Type | Description | Required

|spec.selector
|WorkloadSelector
|Criteria used to select the specific set of pods/VMs on which this plugin configuration should be applied. If omitted, this configuration will be applied to all workload instances in the same namespace. If the `WasmPlugin` field is present in the config root namespace, it will be applied to all applicable workloads in any namespace.
|No

|spec.url
|string
|URL of a Wasm module or OCI container. If no scheme is present, defaults to `oci://`, referencing an OCI image. Other valid schemes are `file://` for referencing .wasm module files present locally within the proxy container, and `http[s]://` for .wasm module files hosted remotely.
|No

|spec.sha256
|string
|SHA256 checksum that will be used to verify the Wasm module or OCI container. If the `url` field already references a SHA256 (using the `@sha256:` notation), it must match the value of this field. If an OCI image is referenced by tag and this field is set, its checksum will be verified against the contents of this field after pulling.
|No

|spec.imagePullPolicy
|PullPolicy
|The pull behavior to be applied when fetching an OCI image. Only relevant when images are referenced by tag instead of SHA. Defaults to the value `IfNotPresent`, except when an OCI image is referenced in the `url` field and the `latest` tag is used, in which case the value `Always` is the default, mirroring K8s behavior. Setting is ignored if the `url` field is referencing a Wasm module directly using `file://` or `http[s]://`.
|No

|spec.imagePullSecret
|string
|Credentials to use for OCI image pulling. The name of a secret in the same namespace as the `WasmPlugin` object that contains a pull secret for authenticating against the registry when pulling the image.
|No

|spec.phase
|PluginPhase
|Determines where in the filter chain this `WasmPlugin` object is injected.
|No

|spec.priority
|`int64`
|Determines the ordering of `WasmPlugins` objects that have the same `phase` value. When multiple `WasmPlugins` objects are applied to the same workload in the same phase, they will be applied by priority and in descending order. If the `priority` field is not set, or two `WasmPlugins` objects with the same value, the ordering will be determined from the name and namespace of the `WasmPlugins` objects. Defaults to the value `0`.
|No

|spec.pluginName
|string
|The plugin name used in the Envoy configuration. Some Wasm modules might require this value to select the Wasm plugin to execute.
|No

|spec.pluginConfig
|Struct
|The configuration that will be passed on to the plugin.
|No

|spec.pluginConfig.verificationKey
|string
|The public key used to verify signatures of signed OCI images or Wasm modules. Must be supplied in PEM format.
|No
|===

The `WorkloadSelector` object specifies the criteria used to determine if a filter can be applied to a proxy. The matching criteria includes the metadata associated with a proxy, workload instance information such as labels attached to the pod/VM, or any other information that the proxy provides to Istio during the initial handshake. If multiple conditions are specified, all conditions need to match in order for the workload instance to be selected. Currently, only label based selection mechanism is supported.

.WorkloadSelector
[options="header"]
[cols="a, a, a, a"]
|===
| Field | Type | Description | Required
|matchLabels
|map<string, string>
|One or more labels that indicate a specific set of pods/VMs on which a policy should be applied. The scope of label search is restricted to the configuration namespace in which the resource is present.
|Yes
|===

The `PullPolicy` object specifies the pull behavior to be applied when fetching an OCI image.

.PullPolicy
[options="header"]
[cols="a, a"]
|===
| Value | Description
|<empty>
|Defaults to the value `IfNotPresent`, except for OCI images with tag latest, for which the default will be the value `Always`.

|IfNotPresent
|If an existing version of the image has been pulled before, that will be used. If no version of the image is present locally, we will pull the latest version.

|Always
|Always pull the latest version of an image when applying this plugin.
|===

`Struct` represents a structured data value, consisting of fields which map to dynamically typed values. In some languages, Struct might be supported by a native representation. For example, in scripting languages like JavaScript a struct is represented as an object.

.Struct
[options="header"]
[cols="a, a, a"]
|===
| Field | Type | Description
|fields
|map<string, Value>
|Map of dynamically typed values.
|===

`PluginPhase` specifies the phase in the filter chain where the plugin will be injected.

.PluginPhase
[options="header"]
[cols="a, a"]
|===
| Field | Description
|<empty>
|Control plane decides where to insert the plugin. This will generally be at the end of the filter chain, right before the Router. Do not specify PluginPhase if the plugin is independent of others.

|AUTHN
|Insert plugin before Istio authentication filters.

|AUTHZ
|Insert plugin before Istio authorization filters and after Istio authentication filters.

|STATS
|Insert plugin before Istio stats filters and after Istio authorization filters.
|===
