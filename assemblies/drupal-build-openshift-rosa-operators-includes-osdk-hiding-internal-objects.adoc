// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-hiding-internal-objects_{context}"]
= Hiding internal objects

It is common practice for Operators to use custom resource definitions (CRDs) internally to accomplish a task. These objects are not meant for users to manipulate and can be confusing to users of the Operator. For example, a database Operator might have a `Replication` CRD that is created whenever a user creates a Database object with `replication: true`.

As an Operator author, you can hide any CRDs in the user interface that are not meant for user manipulation by adding the `operators.operatorframework.io/internal-objects` annotation to the cluster service version (CSV) of your Operator.

.Procedure

. Before marking one of your CRDs as internal, ensure that any debugging information or configuration that might be required to manage the application is reflected on the status or `spec` block of your CR, if applicable to your Operator.

. Add the `operators.operatorframework.io/internal-objects` annotation to the CSV of your Operator to specify any internal objects to hide in the user interface:
+
.Internal object annotation
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  name: my-operator-v1.2.3
  annotations:
    operators.operatorframework.io/internal-objects: '["my.internal.crd1.io","my.internal.crd2.io"]' <1>
...
----
<1> Set any internal CRDs as an array of strings.
