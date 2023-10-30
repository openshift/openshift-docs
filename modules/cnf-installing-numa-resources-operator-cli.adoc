// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_mod-docs-content-type: PROCEDURE
[id="cnf-installing-numa-resources-operator-cli_{context}"]
= Installing the NUMA Resources Operator using the CLI

As a cluster administrator, you can install the Operator using the CLI.

.Prerequisites

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a namespace for the NUMA Resources Operator:

.. Save the following YAML in the `nro-namespace.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-numaresources
----

.. Create the `Namespace` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-namespace.yaml
----

. Create the Operator group for the NUMA Resources Operator:

.. Save the following YAML in the `nro-operatorgroup.yaml` file:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: numaresources-operator
  namespace: openshift-numaresources
spec:
  targetNamespaces:
  - openshift-numaresources
----

.. Create the `OperatorGroup` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-operatorgroup.yaml
----

. Create the subscription for the NUMA Resources Operator:

.. Save the following YAML in the `nro-sub.yaml` file:
+
[source,yaml,subs="attributes+"]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: numaresources-operator
  namespace: openshift-numaresources
spec:
  channel: "{product-version}"
  name: numaresources-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

.. Create the `Subscription` CR by running the following command:
+
[source,terminal]
----
$ oc create -f nro-sub.yaml
----

.Verification

. Verify that the installation succeeded by inspecting the CSV resource in the `openshift-numaresources` namespace. Run the following command:
+
[source,terminal]
----
$ oc get csv -n openshift-numaresources
----
+
.Example output

[source,terminal,subs="attributes+"]
----
NAME                             DISPLAY                  VERSION   REPLACES   PHASE
numaresources-operator.v{product-version}.2   numaresources-operator   {product-version}.2               Succeeded
----
