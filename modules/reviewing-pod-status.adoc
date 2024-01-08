// Module included in the following assemblies:
//
// * support/troubleshooting/investigating-pod-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="reviewing-pod-status_{context}"]
= Reviewing pod status

You can query pod status and error states. You can also query a pod's associated deployment configuration and review base image availability.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* You have installed the OpenShift CLI (`oc`).
* `skopeo` is installed.

.Procedure

. Switch into a project:
+
[source,terminal]
----
$ oc project <project_name>
----

. List pods running within the namespace, as well as pod status, error states, restarts, and age:
+
[source,terminal]
----
$ oc get pods
----

. Determine whether the namespace is managed by a deployment configuration:
+
[source,terminal]
----
$ oc status
----
+
If the namespace is managed by a deployment configuration, the output includes the deployment configuration name and a base image reference.

. Inspect the base image referenced in the preceding command's output:
+
[source,terminal]
----
$ skopeo inspect docker://<image_reference>
----

. If the base image reference is not correct, update the reference in the deployment configuration:
+
[source,terminal]
----
$ oc edit deployment/my-deployment
----

. When deployment configuration changes on exit, the configuration will automatically redeploy. Watch pod status as the deployment progresses, to determine whether the issue has been resolved:
+
[source,terminal]
----
$ oc get pods -w
----

. Review events within the namespace for diagnostic information relating to pod failures:
+
[source,terminal]
----
$ oc get events
----
