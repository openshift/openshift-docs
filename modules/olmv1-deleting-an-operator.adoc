// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc

:_mod-docs-content-type: PROCEDURE

[id="olmv1-deleting-an-operator_{context}"]
= Deleting an Operator

You can delete an Operator and its custom resource definitions (CRDs) by deleting the Operator's custom resource (CR).

.Prerequisites

* You have a catalog installed.
* You have an Operator installed.

.Procedure

* Delete an Operator and its CRDs by running the following command:
+
[source,terminal]
----
$ oc delete operator.operators.operatorframework.io quay-example
----
+
.Example output
[source,text]
----
operator.operators.operatorframework.io "quay-example" deleted
----

.Verification

* Run the following commands to verify that your Operator and its resources were deleted:

** Verify the Operator is deleted by running the following command:
+
[source,terminal]
----
$ oc get operator.operators.operatorframework.io
----
+
.Example output
[source,text]
----
No resources found
----

** Verify that the Operator's system namespace is deleted by running the following command:
+
[source,terminal]
----
$ oc get ns quay-operator-system
----
+
.Example output
[source,text]
----
Error from server (NotFound): namespaces "quay-operator-system" not found
----
