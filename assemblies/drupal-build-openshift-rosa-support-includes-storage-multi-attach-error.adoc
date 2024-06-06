// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-storage-issues.adoc

:_mod-docs-content-type: PROCEDURE
[id="storage-multi-attach-error_{context}"]
= Resolving multi-attach errors

When a node crashes or shuts down abruptly, the attached ReadWriteOnce (RWO) volume is expected to be unmounted from the node so that it can be used by a pod scheduled on another node.

However, mounting on a new node is not possible because the failed node is unable to unmount the attached volume.

A multi-attach error is reported:

[source,terminal]
.Example output
--
Unable to attach or mount volumes: unmounted volumes=[sso-mysql-pvol], unattached volumes=[sso-mysql-pvol default-token-x4rzc]: timed out waiting for the condition
Multi-Attach error for volume "pvc-8837384d-69d7-40b2-b2e6-5df86943eef9" Volume is already used by pod(s) sso-mysql-1-ns6b4
--

.Procedure

To resolve the multi-attach issue, use one of the following solutions:

* Enable multiple attachments by using RWX volumes.
+
For most storage solutions, you can use ReadWriteMany (RWX) volumes to prevent multi-attach errors.
+
* Recover or delete the failed node when using an RWO volume.
+
For storage that does not support RWX, such as VMware vSphere, RWO volumes must be used instead. However, RWO volumes cannot be mounted on multiple nodes.
+
If you encounter a multi-attach error message with an RWO volume, force delete the pod on a shutdown or crashed node to avoid data loss in critical workloads, such as when dynamic persistent volumes are attached.
+
[source,terminal]
----
$ oc delete pod <old_pod> --force=true --grace-period=0
----
+
This command deletes the volumes stuck on shutdown or crashed nodes after six minutes.
