// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-operator-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="querying-operator-pod-status_{context}"]
= Querying Operator pod status

You can list Operator pods within a cluster and their status. You can also collect a detailed Operator pod summary.

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

. List Operators running in the cluster. The output includes Operator version, availability, and up-time information:
+
[source,terminal]
----
$ oc get clusteroperators
----

. List Operator pods running in the Operator's namespace, plus pod status, restarts, and age:
+
[source,terminal]
----
$ oc get pod -n <operator_namespace>
----

. Output a detailed Operator pod summary:
+
[source,terminal]
----
$ oc describe pod <operator_pod_name> -n <operator_namespace>
----

ifndef::openshift-rosa,openshift-dedicated[]
. If an Operator issue is node-specific, query Operator container status on that node.
.. Start a debug pod for the node:
+
[source,terminal]
----
$ oc debug node/my-node
----
+
.. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----
+
[NOTE]
====
{product-title} {product-version} cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the {product-title} API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====
+
.. List details about the node's containers, including state and associated pod IDs:
+
[source,terminal]
----
# crictl ps
----
+
.. List information about a specific Operator container on the node. The following example lists information about the `network-operator` container:
+
[source,terminal]
----
# crictl ps --name network-operator
----
+
.. Exit from the debug shell.
endif::openshift-rosa,openshift-dedicated[]
