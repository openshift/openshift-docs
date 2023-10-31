// Module included in the following assemblies:
//
// * operators/metallb/metallb-upgrading-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-updating-metallb-operatorgroup_{context}"]
= Editing the MetalLB Operator Operator group

When upgrading from any MetalLB Operator version up to and including 4.10 to 4.11 and later, remove `spec.targetNamespaces` from the Operator group custom resource (CR). You must remove the spec regardless of whether you used the web console or the CLI to delete the MetalLB Operator.
[NOTE]
====
The MetalLB Operator version 4.11 or later only supports the `AllNamespaces` install mode, whereas 4.10 or earlier versions support `OwnNamespace` or `SingleNamespace` modes.
====

.Prerequisites

- You have access to an {product-title} cluster with `cluster-admin` permissions.
- You have installed the OpenShift CLI (`oc`).

.Procedure

. List the Operator groups in the `metallb-system` namespace by running the following command:
+
[source,terminal]
----
$ oc get operatorgroup -n metallb-system
----
+
.Example output

[source,terminal]
----
NAME                   AGE
metallb-system-7jc66   85m
----

. Verify that the `spec.targetNamespaces` is present in the Operator group CR associated with the `metallb-system` namespace by running the following command:
+
[source,terminal]
----
$ oc get operatorgroup metallb-system-7jc66 -n metallb-system -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  annotations:
    olm.providedAPIs: ""
  creationTimestamp: "2023-10-25T09:42:49Z"
  generateName: metallb-system-
  generation: 1
  name: metallb-system-7jc66
  namespace: metallb-system
  resourceVersion: "25027"
  uid: f5f644a0-eef8-4e31-a306-e2bbcfaffab3
spec:
  targetNamespaces:
  - metallb-system
  upgradeStrategy: Default
status:
  lastUpdated: "2023-10-25T09:42:49Z"
  namespaces:
  - metallb-system
----

. Edit the Operator group and remove the `targetNamespaces` and `metallb-system` present under the `spec` section by running the following command:
+
[source,terminal]
----
$ oc edit n metallb-system
----
+
.Example output
+
[source,terminal]
----
operatorgroup.operators.coreos.com/metallb-system-7jc66 edited
----

. Verify the `spec.targetNamespaces` is removed from the Operator group custom resource associated with the `metallb-system` namespace by running the following command:
+
[source,terminal]
----
$ oc get operatorgroup metallb-system-7jc66 -n metallb-system -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  annotations:
    olm.providedAPIs: ""
  creationTimestamp: "2023-10-25T09:42:49Z"
  generateName: metallb-system-
  generation: 2
  name: metallb-system-7jc66
  namespace: metallb-system
  resourceVersion: "61658"
  uid: f5f644a0-eef8-4e31-a306-e2bbcfaffab3
spec:
  upgradeStrategy: Default
status:
  lastUpdated: "2023-10-25T14:31:30Z"
  namespaces:
  - ""
----


