// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="gathering-operator-logs_{context}"]
= Gathering Operator logs

If you experience Operator issues, you can gather detailed diagnostic information from Operator pod logs.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).
* You have the fully qualified domain names of the control plane or control plane machines.

.Procedure

. List the Operator pods that are running in the Operator's namespace, plus the pod status, restarts, and age:
+
[source,terminal]
----
$ oc get pods -n <operator_namespace>
----

. Review logs for an Operator pod:
+
[source,terminal]
----
$ oc logs pod/<pod_name> -n <operator_namespace>
----
+
If an Operator pod has multiple containers, the preceding command will produce an error that includes the name of each container. Query logs from an individual container:
+
[source,terminal]
----
$ oc logs pod/<operator_pod_name> -c <container_name> -n <operator_namespace>
----

. If the API is not functional, review Operator pod and container logs on each control plane node by using SSH instead. Replace `<master-node>.<cluster_name>.<base_domain>` with appropriate values.
.. List pods on each control plane node:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl pods
----
+
.. For any Operator pods not showing a `Ready` status, inspect the pod's status in detail. Replace `<operator_pod_id>` with the Operator pod's ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl inspectp <operator_pod_id>
----
+
.. List containers related to an Operator pod:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl ps --pod=<operator_pod_id>
----
+
.. For any Operator container not showing a `Ready` status, inspect the container's status in detail. Replace `<container_id>` with a container ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl inspect <container_id>
----
+
.. Review the logs for any Operator containers not showing a `Ready` status. Replace `<container_id>` with a container ID listed in the output of the preceding command:
+
[source,terminal]
----
$ ssh core@<master-node>.<cluster_name>.<base_domain> sudo crictl logs -f <container_id>
----
+
[NOTE]
====
{product-title} {product-version} cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the {product-title} API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.
====
