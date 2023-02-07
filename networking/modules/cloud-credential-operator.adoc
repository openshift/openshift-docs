// Module included in the following assemblies:
//
// * operators/operator-reference.adoc

[id="cloud-credential-operator_{context}"]
= Cloud Credential Operator

[discrete]
== Purpose

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow {product-title} components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

[discrete]
== Project

link:https://github.com/openshift/cloud-credential-operator[openshift-cloud-credential-operator]

[discrete]
== CRDs

* `credentialsrequests.cloudcredential.openshift.io`
** Scope: Namespaced
** CR: `CredentialsRequest`
** Validation: Yes

[discrete]
== Configuration objects

No configuration required.
