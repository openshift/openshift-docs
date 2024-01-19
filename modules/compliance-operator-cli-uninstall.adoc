// Module included in the following assemblies:
//
// security/compliance_operator/co-management/compliance-operator-uninstallation.adoc

:_mod-docs-content-type: PROCEDURE
[id="compliance-operator-uninstall-cli_{context}"]
= Uninstalling the OpenShift Compliance Operator from {product-title} using the CLI

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the *openshift-compliance* project.

.Prerequisites

* Access to an {product-title} cluster using an account with `cluster-admin` permissions.
* The OpenShift Compliance Operator must be installed.

.Procedure

. Delete all objects in the namespace.

.. Delete the `ScanSettingBinding` objects:
+
[source,terminal]
----
$ oc delete ssb --all -n openshift-compliance
----

.. Delete the `ScanSetting` objects:
+
[source,terminal]
----
$ oc delete ss --all -n openshift-compliance
----

.. Delete the `ComplianceSuite` objects:
+
[source,terminal]
----
$ oc delete suite --all -n openshift-compliance
----

.. Delete the `ComplianceScan` objects:
+
[source,terminal]
----
$ oc delete scan --all -n openshift-compliance
----

.. Delete the `ProfileBundle` objects:
+
[source,terminal]
----
$ oc delete profilebundle.compliance --all -n openshift-compliance
----

. Delete the Subscription object:
+
[source,terminal]
----
$ oc delete sub --all -n openshift-compliance
----

. Delete the CSV object:
+
[source,terminal]
----
$ oc delete csv --all -n openshift-compliance
----

. Delete the project:
+
[source,terminal]
----
$ oc delete project openshift-compliance
----
+
.Example output
[source,terminal]
----
project.project.openshift.io "openshift-compliance" deleted
----

.Verification

. Confirm the namespace is deleted:
+
[source,terminal]
----
$ oc get project/openshift-compliance
----
+
.Example output
[source,terminal]
----
Error from server (NotFound): namespaces "openshift-compliance" not found
----
