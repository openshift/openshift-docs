// Module included in the following assemblies:
//
// * nodes/pods/run_once_duration_override/run-once-duration-override-uninstall.adoc

:_mod-docs-content-type: PROCEDURE
[id="rodoo-uninstall-resources_{context}"]
= Uninstalling {run-once-operator} resources

Optionally, after uninstalling the {run-once-operator}, you can remove its related resources from your cluster.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {product-title} web console.
* You have uninstalled the {run-once-operator}.

.Procedure

. Log in to the {product-title} web console.

. Remove CRDs that were created when the {run-once-operator} was installed:
.. Navigate to *Administration* -> *CustomResourceDefinitions*.
.. Enter `RunOnceDurationOverride` in the *Name* field to filter the CRDs.
.. Click the Options menu {kebab} next to the *RunOnceDurationOverride* CRD and select *Delete CustomResourceDefinition*.
.. In the confirmation dialog, click *Delete*.

. Delete the `openshift-run-once-duration-override-operator` namespace.
.. Navigate to *Administration* -> *Namespaces*.
.. Enter `openshift-run-once-duration-override-operator` into the filter box.
.. Click the Options menu {kebab} next to the *openshift-run-once-duration-override-operator* entry and select *Delete Namespace*.
.. In the confirmation dialog, enter `openshift-run-once-duration-override-operator` and click *Delete*.

. Remove the run-once duration override label from the namespaces that it was enabled on.

.. Navigate to *Administration* -> *Namespaces*.
.. Select your namespace.
.. Click *Edit* next to the *Labels* field.
.. Remove the *runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true* label and click *Save*.
