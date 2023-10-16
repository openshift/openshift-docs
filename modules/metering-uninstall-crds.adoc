// Module included in the following assemblies:
//
// * metering/metering-uninstall.adoc

[id="metering-uninstall-crds_{context}"]
= Uninstalling metering custom resource definitions

The metering custom resource definitions (CRDs) remain in the cluster after the Metering Operator is uninstalled and the `openshift-metering` namespace is deleted.

[IMPORTANT]
====
Deleting the metering CRDs disrupts any additional metering installations in other namespaces in your cluster. Ensure that there are no other metering installations before proceeding.
====

.Prerequisites

*  The `MeteringConfig` custom resource in the `openshift-metering` namespace is deleted.
*  The `openshift-metering` namespace is deleted.

.Procedure

*  Delete the remaining metering CRDs:
+
[source,terminal]
----
$ oc get crd -o name | grep "metering.openshift.io" | xargs oc delete
----
