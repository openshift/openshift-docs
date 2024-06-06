// Module included in the following assemblies:
//
// * support/troubleshooting/verifying-node-health.adoc

:_mod-docs-content-type: PROCEDURE
[id="reviewing-node-status-use-and-configuration_{context}"]
= Reviewing node status, resource usage, and configuration

Review cluster node health status, resource consumption statistics, and node logs. Additionally, query `kubelet` status on individual nodes.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* You have installed the OpenShift CLI (`oc`).

.Procedure

* List the name, status, and role for all nodes in the cluster:
+
[source,terminal]
----
$ oc get nodes
----

* Summarize CPU and memory usage for each node within the cluster:
+
[source,terminal]
----
$ oc adm top nodes
----

* Summarize CPU and memory usage for a specific node:
+
[source,terminal]
----
$ oc adm top node my-node
----
