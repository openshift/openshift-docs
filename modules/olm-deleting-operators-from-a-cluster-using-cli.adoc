// Module included in the following assemblies:
//
// * operators/admin/olm-deleting-operators-from-a-cluster.adoc
// * serverless/install/removing-openshift-serverless.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-deleting-operator-from-a-cluster-using-cli_{context}"]
= Deleting Operators from a cluster using the CLI

Cluster administrators can delete installed Operators from a selected namespace by using the CLI.

.Prerequisites

- You have access to an {product-title} cluster using an account with
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
`cluster-admin` permissions.
endif::[]
ifdef::openshift-dedicated,openshift-rosa[]
`dedicated-admin` permissions.
endif::openshift-dedicated,openshift-rosa[]
- The OpenShift CLI (`oc`) is installed on your workstation.

.Procedure

. Ensure the latest version of the subscribed operator (for example, `serverless-operator`) is identified in the `currentCSV` field.
+
[source,terminal]
----
$ oc get subscription.operators.coreos.com serverless-operator -n openshift-serverless -o yaml | grep currentCSV
----
+
.Example output
[source,terminal]
----
  currentCSV: serverless-operator.v1.28.0
----

. Delete the subscription (for example, `serverless-operator`):
+
[source,terminal]
----
$ oc delete subscription.operators.coreos.com serverless-operator -n openshift-serverless
----
+
.Example output
[source,terminal]
----
subscription.operators.coreos.com "serverless-operator" deleted
----

. Delete the CSV for the Operator in the target namespace using the `currentCSV` value from the previous step:
+
[source,terminal]
----
$ oc delete clusterserviceversion serverless-operator.v1.28.0 -n openshift-serverless
----
+
.Example output
[source,terminal]
----
clusterserviceversion.operators.coreos.com "serverless-operator.v1.28.0" deleted
----
