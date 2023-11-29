// Module included in the following assemblies:
//
// * support/troubleshooting/investigating-pod-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="accessing-running-pods_{context}"]
= Accessing running pods

You can review running pods dynamically by opening a shell inside a pod or by gaining network access through port forwarding.

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

. Switch into the project that contains the pod you would like to access. This is necessary because the `oc rsh` command does not accept the `-n` namespace option:
+
[source,terminal]
----
$ oc project <namespace>
----

. Start a remote shell into a pod:
+
[source,terminal]
----
$ oc rsh <pod_name>  <1>
----
<1> If a pod has multiple containers, `oc rsh` defaults to the first container unless `-c <container_name>` is specified.

. Start a remote shell into a specific container within a pod:
+
[source,terminal]
----
$ oc rsh -c <container_name> pod/<pod_name>
----

. Create a port forwarding session to a port on a pod:
+
[source,terminal]
----
$ oc port-forward <pod_name> <host_port>:<pod_port>  <1>
----
<1> Enter `Ctrl+C` to cancel the port forwarding session.
