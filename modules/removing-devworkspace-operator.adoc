// Module included in the following assemblies:
//
// * web_console/web_terminal/uninstalling-web-terminal.adoc

:_mod-docs-content-type: PROCEDURE
[id="removing-devworkspace-operator_{context}"]
= Removing the {devworkspace-op}

To completely uninstall the web terminal, you must also remove the {devworkspace-op} and custom resources used by the Operator.

[IMPORTANT]
====
The {devworkspace-op} is a standalone Operator and may be required as a dependency for other Operators installed in the cluster. Follow the steps below only if you are sure that the {devworkspace-op} is no longer needed.
====

.Prerequisites

* You have access to an {product-title} cluster with cluster administrator permissions.
* You have installed the `oc` CLI.

// Hide step 2, cannot delete resource "customresourcedefinitions" in ROSA/OSD
// Hide step 4, cannot delete resource "mutatingwebhookconfigurations" in ROSA/OSD, do not delete deployment/devworkspace-webhook-server, see NOTE 


.Procedure

. Remove the `DevWorkspace` custom resources used by the Operator, along with any related Kubernetes objects:
+
[source,terminal]
----
$ oc delete devworkspaces.workspace.devfile.io --all-namespaces --all --wait
----
+
[source,terminal]
----
$ oc delete devworkspaceroutings.controller.devfile.io --all-namespaces --all --wait
----
+
[WARNING]
====
If this step is not complete, finalizers make it difficult to fully uninstall the Operator.
====

ifndef::openshift-rosa,openshift-dedicated[]
. Remove the CRDs used by the Operator:
+
[WARNING]
====
The DevWorkspace Operator provides custom resource definitions (CRDs) that use conversion webhooks. Failing to remove these CRDs can cause issues in the cluster.
====
+
[source,terminal]
----
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaceroutings.controller.devfile.io
----
+
[source,terminal]
----
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaces.workspace.devfile.io
----
+
[source,terminal]
----
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspacetemplates.workspace.devfile.io
----
+
[source,terminal]
----
$ oc delete customresourcedefinitions.apiextensions.k8s.io devworkspaceoperatorconfigs.controller.devfile.io
----

. Verify that all involved custom resource definitions are removed. The following command should not display any output:
+
[source,terminal]
----
$ oc get customresourcedefinitions.apiextensions.k8s.io | grep "devfile.io"
----

. Remove the `devworkspace-webhook-server` deployment, mutating, and validating webhooks:
+
[source,terminal]
----
$ oc delete deployment/devworkspace-webhook-server -n openshift-operators
----
+
[source,terminal]
----
$ oc delete mutatingwebhookconfigurations controller.devfile.io
----
+
[source,terminal]
----
$ oc delete validatingwebhookconfigurations controller.devfile.io
----
+
[NOTE]
====
If you remove the `devworkspace-webhook-server` deployment without removing the mutating and validating webhooks, you can not use `oc exec` commands to run commands in a container in the cluster. After you remove the webhooks you can use the `oc exec` commands again.
====
endif::openshift-rosa,openshift-dedicated[]

. Remove any remaining services, secrets, and config maps. Depending on the installation, some resources included in the following commands may not exist in the cluster.
+
[source,terminal]
----
$ oc delete all --selector app.kubernetes.io/part-of=devworkspace-operator,app.kubernetes.io/name=devworkspace-webhook-server -n openshift-operators
----
+
[source,terminal]
----
$ oc delete serviceaccounts devworkspace-webhook-server -n openshift-operators
----
+
[source,terminal]
----
$ oc delete clusterrole devworkspace-webhook-server
----
+
[source,terminal]
----
$ oc delete clusterrolebinding devworkspace-webhook-server
----

. Uninstall the {devworkspace-op}:
.. In the *Administrator* perspective of the web console, navigate to *Operators -> Installed Operators*.
.. Scroll the filter list or type a keyword into the *Filter by name* box to find the {devworkspace-op}.
.. Click the Options menu {kebab} for the Operator, and then select *Uninstall Operator*.
.. In the *Uninstall Operator* confirmation dialog box, click *Uninstall* to remove the Operator, Operator deployments, and pods from the cluster. The Operator stops running and no longer receives updates.

