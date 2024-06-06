// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-csv-annotations-other_{context}"]
= Other optional annotations

The following Operator annotations are optional.

.Other optional annotations
[cols="5a,5a",options="header"]
|===
|Annotation |Description

|`alm-examples`
|Provide custom resource definition (CRD) templates with a minimum set of configuration. Compatible UIs pre-fill this template for users to further customize.

|`operatorframework.io/initialization-resource`
|Specify a single required custom resource by adding `operatorframework.io/initialization-resource` annotation to the cluster service version (CSV) during Operator installation. The user is then prompted to create the custom resource through a template provided in the CSV.  Must include a template that contains a complete YAML definition.

|`operatorframework.io/suggested-namespace`
|Set a suggested namespace where the Operator should be deployed.

|`operatorframework.io/suggested-namespace-template`
|Set a manifest for a `Namespace` object with the default node selector for the namespace specified.

|`operators.openshift.io/valid-subscription`
|Free-form array for listing any specific subscriptions that are required to use the Operator. For example, `'["3Scale Commercial License", "Red Hat Managed Integration"]'`.

|`operators.operatorframework.io/internal-objects`
|Hides CRDs in the UI that are not meant for user manipulation.

|===

.Example CSV with an {product-title} license requirement
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  annotations:
    operators.openshift.io/valid-subscription: '["OpenShift Container Platform"]'
----

.Example CSV with a 3scale license requirement
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  annotations:
    operators.openshift.io/valid-subscription: '["3Scale Commercial License", "Red Hat Managed Integration"]'
----