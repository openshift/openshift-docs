:_mod-docs-content-type: ASSEMBLY
[id="securing-webhooks-with-event-listeners"]
= Securing webhooks with event listeners
include::_attributes/common-attributes.adoc[]
:context: securing-webhooks-with-event-listeners

toc::[]

As an administrator, you can secure webhooks with event listeners. After creating a namespace, you enable HTTPS for the `Eventlistener` resource by adding the `operator.tekton.dev/enable-annotation=enabled` label to the namespace. Then, you create a `Trigger` resource and a secured route using the re-encrypted TLS termination.

Triggers in {pipelines-title} support insecure HTTP and secure HTTPS connections to the `Eventlistener` resource. HTTPS secures connections within and outside the cluster.

{pipelines-title} runs a `tekton-operator-proxy-webhook` pod that watches for the labels in the namespace. When you add the label to the namespace, the webhook sets the `service.beta.openshift.io/serving-cert-secret-name=<secret_name>` annotation on the `EventListener` object. This, in turn, creates secrets and the required certificates.

[source,terminal,subs="attributes+"]
----
service.beta.openshift.io/serving-cert-secret-name=<secret_name>
----

In addition, you can mount the created secret into the `Eventlistener` pod to secure the request.

include::modules/op-providing-secure-connection.adoc[leveloffset=+1]

include::modules/op-sample-eventlistener-resource.adoc[leveloffset=+1]
