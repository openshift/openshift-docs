// Module included in the following assemblies:
//
// * architecture/admission-plug-ins.adoc

[id="admission-webhook-types_{context}"]
= Types of webhook admission plugins

Cluster administrators can call out to webhook servers through the mutating admission plugin or the validating admission plugin in the API server admission chain.

[id="mutating-admission-plug-in_{context}"]
== Mutating admission plugin

The mutating admission plugin is invoked during the mutation phase of the admission process, which allows modification of resource content before it is persisted. One example webhook that can be called through the mutating admission plugin is the Pod Node Selector feature, which uses an annotation on a namespace to find a label selector and add it to the pod specification.

[id="mutating-admission-plug-in-config_{context}"]
.Sample mutating admission plugin configuration

[source,yaml]
----
apiVersion: admissionregistration.k8s.io/v1beta1
kind: MutatingWebhookConfiguration <1>
metadata:
  name: <webhook_name> <2>
webhooks:
- name: <webhook_name> <3>
  clientConfig: <4>
    service:
      namespace: default <5>
      name: kubernetes <6>
      path: <webhook_url> <7>
    caBundle: <ca_signing_certificate> <8>
  rules: <9>
  - operations: <10>
    - <operation>
    apiGroups:
    - ""
    apiVersions:
    - "*"
    resources:
    - <resource>
  failurePolicy: <policy> <11>
  sideEffects: None
----

<1> Specifies a mutating admission plugin configuration.
<2> The name for the `MutatingWebhookConfiguration` object. Replace `<webhook_name>` with the appropriate value.
<3> The name of the webhook to call. Replace `<webhook_name>` with the appropriate value.
<4> Information about how to connect to, trust, and send data to the webhook server.
<5> The namespace where the front-end service is created.
<6> The name of the front-end service.
<7> The webhook URL used for admission requests. Replace `<webhook_url>` with the appropriate value.
<8> A PEM-encoded CA certificate that signs the server certificate that is used by the webhook server.  Replace `<ca_signing_certificate>` with the appropriate certificate in base64 format.
<9> Rules that define when the API server should use this webhook admission plugin.
<10> One or more operations that trigger the API server to call this webhook admission plugin. Possible values are `create`, `update`, `delete` or `connect`. Replace `<operation>` and `<resource>` with the appropriate values.
<11> Specifies how the policy should proceed if the webhook server is unavailable.
Replace `<policy>` with either `Ignore` (to unconditionally accept the request in the event of a failure) or `Fail` (to deny the failed request). Using `Ignore` can result in unpredictable behavior for all clients.

[IMPORTANT]
====
In {product-title} {product-version}, objects created by users or control loops through a mutating admission plugin might return unexpected results, especially if values set in an initial request are overwritten, which is not recommended.
====

[id="validating-admission-plug-in_{context}"]
== Validating admission plugin

A validating admission plugin is invoked during the validation phase of the admission process. This phase allows the enforcement of invariants on particular API resources to ensure that the resource does not change again. The Pod Node Selector is also an example of a webhook which is called by the validating admission plugin, to ensure that all `nodeSelector` fields are constrained by the node selector restrictions on the namespace.

[id="validating-admission-plug-in-config_{context}"]
//http://blog.kubernetes.io/2018/01/extensible-admission-is-beta.html
.Sample validating admission plugin configuration

[source,yaml]
----
apiVersion: admissionregistration.k8s.io/v1beta1
kind: ValidatingWebhookConfiguration <1>
metadata:
  name: <webhook_name> <2>
webhooks:
- name: <webhook_name> <3>
  clientConfig: <4>
    service:
      namespace: default  <5>
      name: kubernetes <6>
      path: <webhook_url> <7>
    caBundle: <ca_signing_certificate> <8>
  rules: <9>
  - operations: <10>
    - <operation>
    apiGroups:
    - ""
    apiVersions:
    - "*"
    resources:
    - <resource>
  failurePolicy: <policy> <11>
  sideEffects: Unknown
----

<1> Specifies a validating admission plugin configuration.
<2> The name for the `ValidatingWebhookConfiguration` object. Replace `<webhook_name>` with the appropriate value.
<3> The name of the webhook to call. Replace `<webhook_name>` with the appropriate value.
<4> Information about how to connect to, trust, and send data to the webhook server.
<5> The namespace where the front-end service is created.
<6> The name of the front-end service.
<7> The webhook URL used for admission requests. Replace `<webhook_url>` with the appropriate value.
<8> A PEM-encoded CA certificate that signs the server certificate that is used by the webhook server.  Replace `<ca_signing_certificate>` with the appropriate certificate in base64 format.
<9> Rules that define when the API server should use this webhook admission plugin.
<10> One or more operations that trigger the API server to call this webhook admission plugin. Possible values are `create`, `update`, `delete` or `connect`. Replace `<operation>` and `<resource>` with the appropriate values.
<11> Specifies how the policy should proceed if the webhook server is unavailable.
Replace `<policy>` with either `Ignore` (to unconditionally accept the request in the event of a failure) or `Fail` (to deny the failed request). Using `Ignore` can result in unpredictable behavior for all clients.
