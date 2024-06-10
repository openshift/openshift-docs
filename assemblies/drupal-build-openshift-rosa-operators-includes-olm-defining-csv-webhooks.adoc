// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-defining-csv-webhook_{context}"]
= Defining webhooks

Webhooks allow Operator authors to intercept, modify, and accept or reject resources before they are saved to the object store and handled by the Operator controller. Operator Lifecycle Manager (OLM) can manage the lifecycle of these webhooks when they are shipped alongside your Operator.

The cluster service version (CSV) resource of an Operator can include a `webhookdefinitions` section to define the following types of webhooks:

* Admission webhooks (validating and mutating)
* Conversion webhooks

.Procedure

* Add a `webhookdefinitions` section to the `spec` section of the CSV of your Operator and include any webhook definitions using a `type` of `ValidatingAdmissionWebhook`, `MutatingAdmissionWebhook`, or `ConversionWebhook`. The following example contains all three types of webhooks:
+
.CSV containing webhooks
[source,yaml]
----
  apiVersion: operators.coreos.com/v1alpha1
  kind: ClusterServiceVersion
  metadata:
    name: webhook-operator.v0.0.1
  spec:
    customresourcedefinitions:
      owned:
      - kind: WebhookTest
        name: webhooktests.webhook.operators.coreos.io <1>
        version: v1
    install:
      spec:
        deployments:
        - name: webhook-operator-webhook
          ...
          ...
          ...
      strategy: deployment
    installModes:
    - supported: false
      type: OwnNamespace
    - supported: false
      type: SingleNamespace
    - supported: false
      type: MultiNamespace
    - supported: true
      type: AllNamespaces
    webhookdefinitions:
    - type: ValidatingAdmissionWebhook <2>
      admissionReviewVersions:
      - v1beta1
      - v1
      containerPort: 443
      targetPort: 4343
      deploymentName: webhook-operator-webhook
      failurePolicy: Fail
      generateName: vwebhooktest.kb.io
      rules:
      - apiGroups:
        - webhook.operators.coreos.io
        apiVersions:
        - v1
        operations:
        - CREATE
        - UPDATE
        resources:
        - webhooktests
      sideEffects: None
      webhookPath: /validate-webhook-operators-coreos-io-v1-webhooktest
    - type: MutatingAdmissionWebhook <3>
      admissionReviewVersions:
      - v1beta1
      - v1
      containerPort: 443
      targetPort: 4343
      deploymentName: webhook-operator-webhook
      failurePolicy: Fail
      generateName: mwebhooktest.kb.io
      rules:
      - apiGroups:
        - webhook.operators.coreos.io
        apiVersions:
        - v1
        operations:
        - CREATE
        - UPDATE
        resources:
        - webhooktests
      sideEffects: None
      webhookPath: /mutate-webhook-operators-coreos-io-v1-webhooktest
    - type: ConversionWebhook <4>
      admissionReviewVersions:
      - v1beta1
      - v1
      containerPort: 443
      targetPort: 4343
      deploymentName: webhook-operator-webhook
      generateName: cwebhooktest.kb.io
      sideEffects: None
      webhookPath: /convert
      conversionCRDs:
      - webhooktests.webhook.operators.coreos.io <5>
...
----
<1> The CRDs targeted by the conversion webhook must exist here.
<2> A validating admission webhook.
<3> A mutating admission webhook.
<4> A conversion webhook.
<5> The `spec.PreserveUnknownFields` property of each CRD must be set to `false` or `nil`.
