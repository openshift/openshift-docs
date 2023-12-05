// Module included in the following assemblies:
//
// * nodes/nodes/node-health-check-operator-installation.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-node-health-check-operator-using-cli_{context}"]
= Installing the Node Health Check Operator by using the CLI
You can use the OpenShift CLI (`oc`) to install the Node Health Check Operator.

To install the Operator in your own namespace, follow the steps in the procedure.

To install the Operator in the `openshift-operators` namespace, skip to step 3 of the procedure because the steps to create a new `Namespace` custom resource (CR) and an `OperatorGroup` CR are not required.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a `Namespace` custom resource (CR) for the Node Health Check Operator:
.. Define the `Namespace` CR and save the YAML file, for example, `node-health-check-namespace.yaml`:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: node-health-check
----
.. To create the `Namespace` CR, run the following command:
+
[source,terminal]
----
$ oc create -f node-health-check-namespace.yaml
----

. Create an `OperatorGroup` CR:
.. Define the `OperatorGroup` CR and save the YAML file, for example, `node-health-check-operator-group.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: node-health-check-operator
  namespace: node-health-check
----
.. To create the `OperatorGroup` CR, run the following command:
+
[source,terminal]
----
$ oc create -f node-health-check-operator-group.yaml
----

. Create a `Subscription` CR:
.. Define the `Subscription` CR and save the YAML file, for example, `node-health-check-subscription.yaml`:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
    name: node-health-check-operator
    namespace: node-health-check <1>
spec:
    channel: stable <2>
    installPlanApproval: Manual <3>
    name: node-healthcheck-operator
    source: redhat-operators
    sourceNamespace: openshift-marketplace
    package: node-healthcheck-operator
----
<1> Specify the `Namespace` where you want to install the Node Health Check Operator. To install the Node Health Check Operator in the `openshift-operators` namespace, specify `openshift-operators` in the `Subscription` CR.
<2> Specify the channel name for your subscription. To upgrade to the latest version of the Node Health Check Operator, you must manually change the channel name for your subscription from `candidate` to `stable`.
<3> Set the approval strategy to Manual in case your specified version is superseded by a later version in the catalog. This plan prevents an automatic upgrade to a later version and requires manual approval before the starting CSV can complete the installation.

.. To create the `Subscription` CR, run the following command:
+
[source,terminal]
----
$ oc create -f node-health-check-subscription.yaml
----

.Verification

. Verify that the installation succeeded by inspecting the CSV resource:
+
[source,terminal]
----
$ oc get csv -n openshift-operators
----
+
.Example output

[source,terminal]
----
NAME                              DISPLAY                     VERSION  REPLACES PHASE
node-healthcheck-operator.v0.2.0. Node Health Check Operator  0.2.0             Succeeded
----
. Verify that the Node Health Check Operator is up and running:
+
[source,terminal]
----
$ oc get deploy -n openshift-operators
----
+
.Example output

[source,terminal]
----
NAME                                           READY   UP-TO-DATE   AVAILABLE   AGE
node-health-check-operator-controller-manager  1/1     1            1           10d
----
