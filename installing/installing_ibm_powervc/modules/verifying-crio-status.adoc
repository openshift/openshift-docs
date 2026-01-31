// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-crio-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="verifying-crio-status_{context}"]
= Verifying CRI-O runtime engine status

You can verify CRI-O container runtime engine status on each cluster node.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Review CRI-O status by querying the `crio` systemd service on a node, within a debug pod.
.. Start a debug pod for a node:
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
.. Check whether the `crio` systemd service is active on the node:
+
[source,terminal]
----
# systemctl is-active crio
----
+
.. Output a more detailed `crio.service` status summary:
+
[source,terminal]
----
# systemctl status crio.service
----
