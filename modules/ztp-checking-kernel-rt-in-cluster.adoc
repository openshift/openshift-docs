// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-vdu-validating-cluster-tuning.adoc

:_module-type: PROCEDURE
[id="ztp-checking-kernel-rt-in-cluster_{context}"]
= Checking the realtime kernel version

Always use the latest version of the realtime kernel in your {product-title} clusters. If you are unsure about the kernel version that is in use in the cluster, you can compare the current realtime kernel version to the release version with the following procedure.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You are logged in as a user with `cluster-admin` privileges.

* You have installed `podman`.

.Procedure

. Run the following command to get the cluster version:
+
[source,terminal]
----
$ OCP_VERSION=$(oc get clusterversion version -o jsonpath='{.status.desired.version}{"\n"}')
----

. Get the release image SHA number:
+
[source,terminal]
----
$ DTK_IMAGE=$(oc adm release info --image-for=driver-toolkit quay.io/openshift-release-dev/ocp-release:$OCP_VERSION-x86_64)
----

. Run the release image container and extract the kernel version that is packaged with cluster's current release:
+
[source,terminal]
----
$ podman run --rm $DTK_IMAGE rpm -qa | grep 'kernel-rt-core-' | sed 's#kernel-rt-core-##'
----
+
.Example output
[source,terminal]
----
4.18.0-305.49.1.rt7.121.el8_4.x86_64
----
+
This is the default realtime kernel version that ships with the release.
+
[NOTE]
====
The realtime kernel is denoted by the string `.rt` in the kernel version.
====

.Verification

Check that the kernel version listed for the cluster's current release matches actual realtime kernel that is running in the cluster. Run the following commands to check the running realtime kernel version:

. Open a remote shell connection to the cluster node:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Check the realtime kernel version:
+
[source,terminal]
----
sh-4.4# uname -r
----
+
.Example output
[source,terminal]
----
4.18.0-305.49.1.rt7.121.el8_4.x86_64
----
