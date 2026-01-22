// Module included in the following assemblies:
//
// scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-lvms-installing-using-cli_{context}"]
= Installing {lvms} by using the CLI

You can use the OpenShift CLI (`oc`) to install {lvms}.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Install the latest version of the {rh-rhacm} Operator.
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create the `openshift-storage` namespace by running the following command:
+
[source,terminal]
----
$ oc create ns openshift-storage
----

. Create an `OperatorGroup` CR.

.. Define the `OperatorGroup` CR and save the YAML file, for example, `lmvs-operatorgroup.yaml`:
+
.Example OperatorGroup CR
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: lvms-operator-operatorgroup
  namespace: openshift-storage
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  targetNamespaces:
  - openshift-storage
----

.. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f lmvs-operatorgroup.yaml
----

. Create a `Subscription` CR.

.. Define the `Subscription` CR and save the YAML file, for example, `lvms-subscription.yaml`:
+
.Example Subscription CR
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: lvms-operator
  namespace: openshift-storage
  annotations:
    ran.openshift.io/ztp-deploy-wave: "2"
spec:
  channel: "stable-{product-version}"
  name: lvms-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Manual
----

.. Create the `Subscription` CR by running the following command:
+
[source,terminal]
----
$ oc create -f lvms-subscription.yaml
----

.Verification

. Verify that the installation succeeded by inspecting the CSV resource:
+
[source,terminal]
----
$ oc get csv -n openshift-storage
----
+
.Example output
[source,terminal,subs="attributes+"]
----
NAME                                                   DISPLAY                            VERSION               REPLACES                           PHASE
lvms-operator.{product-version}.x                                   LVM Storage                        {product-version}x                                                   Succeeded
----

. Verify that {lvms} is up and running:
+
[source,terminal]
----
$ oc get deploy -n openshift-storage
----
+
.Example output
[source,terminal]
----
NAMESPACE                                          NAME                                             READY   UP-TO-DATE   AVAILABLE   AGE
openshift-storage                                  lvms-operator                                    1/1     1            1           14s
----