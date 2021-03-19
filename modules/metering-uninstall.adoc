// Module included in the following assemblies:
//
// * metering/metering-uninstall.adoc

[id="metering-uninstall_{context}"]
= Uninstalling a metering namespace

Uninstall your metering namespace, for example the `openshift-metering` namespace, by removing the `MeteringConfig` resource and deleting the `openshift-metering` namespace.

.Prerequisites

* The Metering Operator is removed from your cluster.

.Procedure

.  Remove all resources created by the Metering Operator:
+
[source,terminal]
----
$ oc --namespace openshift-metering delete meteringconfig --all
----

.  After the previous step is complete, verify that all pods in the `openshift-metering` namespace are deleted or are reporting a terminating state:
+
[source,terminal]
----
$ oc --namespace openshift-metering get pods
----

.  Delete the `openshift-metering` namespace:
+
[source,terminal]
----
$ oc delete namespace openshift-metering
----
