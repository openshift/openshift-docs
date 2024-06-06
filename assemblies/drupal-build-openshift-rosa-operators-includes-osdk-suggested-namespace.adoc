// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-suggested-namespace_{context}"]
= Setting a suggested namespace

Some Operators must be deployed in a specific namespace, or with ancillary resources in specific namespaces, to work properly. If resolved from a subscription, Operator Lifecycle Manager (OLM) defaults the namespaced resources of an Operator to the namespace of its subscription.

As an Operator author, you can instead express a desired target namespace as part of your cluster service version (CSV) to maintain control over the final namespaces of the resources installed for their Operators. When adding the Operator to a cluster using OperatorHub, this enables the web console to autopopulate the suggested namespace for the
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrator
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
installer
endif::openshift-dedicated,openshift-rosa[]
during the installation process.

.Procedure

* In your CSV, set the `operatorframework.io/suggested-namespace` annotation to your suggested namespace:
+
[source,yaml]
----
metadata:
  annotations:
    operatorframework.io/suggested-namespace: <namespace> <1>
----
<1> Set your suggested namespace.
