// Module included in the following assemblies:
//
// * support/troubleshooting/investigating-pod-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="starting-debug-pods-with-root-access_{context}"]
= Starting debug pods with root access

You can start a debug pod with root access, based on a problematic pod's deployment or deployment configuration. Pod users typically run with non-root privileges, but running troubleshooting pods with temporary root privileges can be useful during issue investigation.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Start a debug pod with root access, based on a deployment.
.. Obtain a project's deployment name:
+
[source,terminal]
----
$ oc get deployment -n <project_name>
----

.. Start a debug pod with root privileges, based on the deployment:
+
[source,terminal]
----
$ oc debug deployment/my-deployment --as-root -n <project_name>
----

. Start a debug pod with root access, based on a deployment configuration.
.. Obtain a project's deployment configuration name:
+
[source,terminal]
----
$ oc get deploymentconfigs -n <project_name>
----

.. Start a debug pod with root privileges, based on the deployment configuration:
+
[source,terminal]
----
$ oc debug deploymentconfig/my-deployment-configuration --as-root -n <project_name>
----

[NOTE]
====
You can append `-- <command>` to the preceding `oc debug` commands to run individual commands within a debug pod, instead of running an interactive shell.
====
