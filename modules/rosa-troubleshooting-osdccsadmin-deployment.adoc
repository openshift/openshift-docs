// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-troubleshooting-deployment-failure-osdccsadmin_{context}"]
= Failing to create a cluster with an `osdCcsAdmin` error

If a cluster creation action fails, you can receive the following error message.

.Example output
[source,terminal]
----
Failed to create cluster: Unable to create cluster spec: Failed to get access keys for user 'osdCcsAdmin': NoSuchEntity: The user with name osdCcsAdmin cannot be found.
----

.Procedure
To fix this issue:

. Delete the stack:
+
[source,terminal]
----
$ rosa init --delete
----

. Reinitialize your account:
+
[source,terminal]
----
$ rosa init
----
