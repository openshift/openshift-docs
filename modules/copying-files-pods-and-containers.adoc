// Module included in the following assemblies:
//
// * support/troubleshooting/investigating-pod-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="copying-files-pods-and-containers_{context}"]
= Copying files to and from pods and containers

You can copy files to and from a pod to test configuration changes or gather diagnostic information.

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

. Copy a file to a pod:
+
[source,terminal]
----
$ oc cp <local_path> <pod_name>:/<path> -c <container_name>  <1>
----
<1> The first container in a pod is selected if the `-c` option is not specified.

. Copy a file from a pod:
+
[source,terminal]
----
$ oc cp <pod_name>:/<path>  -c <container_name> <local_path>  <1>
----
<1> The first container in a pod is selected if the `-c` option is not specified.
+
[NOTE]
====
For `oc cp` to function, the `tar` binary must be available within the container.
====
