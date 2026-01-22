////
This module included in the following assemblies:
*service_mesh_/v2x/ossm-extensions.adoc
////
:_mod-docs-content-type: PROCEDURE
[id="ossm-smextensions-deploy_{context}"]
= Deploying `ServiceMeshExtension` resources

You can enable {SMProductName} extensions using the `ServiceMeshExtension` resource. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.

[NOTE]
====
When creating new WebAssembly extensions, use the `WasmPlugin` API. The `ServiceMeshExtension` API was deprecated in {SMProductName} version 2.2 and removed in {SMProductName} version 2.3.
====

For a complete example that was built using the Rust SDK, take a look at the link:https://github.com/maistra/header-append-filter[header-append-filter]. It is a simple filter that appends one or more headers to the HTTP responses, with their names and values taken out from the `config` field of the extension. See a sample configuration in the snippet below.

.Procedure

. Create the following example resource:
+
.Example ServiceMeshExtension resource extension.yaml
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
  image: quay.io/maistra-dev/header-append-filter:2.1
  phase: PostAuthZ
  priority: 100
----

. Apply your `extension.yaml` file with the following command:
+
[source,terminal]
----
$ oc apply -f <extension>.yaml
----
