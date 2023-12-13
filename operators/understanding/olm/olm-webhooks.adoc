:_mod-docs-content-type: ASSEMBLY
[id="olm-webhooks"]
= Webhook management in Operator Lifecycle Manager
include::_attributes/common-attributes.adoc[]
:context: olm-webhooks

toc::[]

Webhooks allow Operator authors to intercept, modify, and accept or reject resources before they are saved to the object store and handled by the Operator controller. Operator Lifecycle Manager (OLM) can manage the lifecycle of these webhooks when they are shipped alongside your Operator.

See xref:../../../operators/operator_sdk/osdk-generating-csvs.adoc#olm-defining-csv-webhook_osdk-generating-csvs[Defining cluster service versions (CSVs)] for details on how an Operator developer can define webhooks for their Operator, as well as considerations when running on OLM.

[id="olm-webhooks-additional-resources"]
[role="_additional-resources"]
== Additional resources

ifndef::openshift-dedicated,openshift-rosa[]
* xref:../../../architecture/admission-plug-ins.adoc#admission-webhook-types_admission-plug-ins[Types of webhook admission plugins]
endif::openshift-dedicated,openshift-rosa[]
* Kubernetes documentation:
** link:https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook[Validating admission webhooks]
** link:https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook[Mutating admission webhooks]
** link:https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion[Conversion webhooks]
