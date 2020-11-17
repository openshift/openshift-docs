// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="olm-webhook-considerations_{context}"]
= Webhook considerations for OLM

When deploying an Operator with webhooks using Operator Lifecycle Manager (OLM), you must define the following:

* The `type` field must be set to either `ValidatingAdmissionWebhook`, `MutatingAdmissionWebhook`, or `ConversionWebhook`, or the CSV will be placed in a failed phase.

* The CSV must contain a deployment whose name is equivalent to the value supplied in the `deploymentName` field of the `webhookdefinition`.

When the webhook is created, OLM ensures that the webhook only acts upon namespaces that match the Operator group that the Operator is deployed in.

[discrete]
[id="olm-webhook-ca_{context}"]
=== Certificate authority constraints

OLM is configured to provide each deployment with a single certificate authority (CA). The logic that generates and mounts the CA into the deployment was originally used by the API service lifecycle logic. As a result:

* The TLS certificate file is mounted to the deployment at `/apiserver.local.config/certificates/apiserver.crt`.
* The TLS key file is mounted to the deployment at `/apiserver.local.config/certificates/apiserver.key`.

[discrete]
[id="olm-admission-webhook-constraints_{context}"]
=== Admission webhook rules constraints

To prevent an Operator from configuring the cluster into an unrecoverable state, OLM places the CSV in the failed phase if the rules defined in an admission webhook intercept any of the following requests:

* Requests that target all groups
* Requests that target the `operators.coreos.com` group
* Requests that target the `ValidatingWebhookConfigurations` or `MutatingWebhookConfigurations` resources

[discrete]
[id="olm-conversion-webhook-constraints_{context}"]
=== Conversion webhook constraints

OLM places the CSV in the failed phase if a conversion webhook definition does not adhere to the following constraints:

* CSVs featuring a conversion webhook can only support the `AllNamespaces` install mode.
* The CRD targeted by the conversion webhook must have its
`spec.preserveUnknownFields` field set to `false` or `nil`.
* The conversion webhook defined in the CSV must target an owned CRD.
* There can only be one conversion webhook on the entire cluster for a given CRD.
