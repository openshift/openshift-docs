// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc


:_mod-docs-content-type: PROCEDURE
[id="rosa-delete-cluster-admins_{context}"]
= Revoking `cluster-admin` access using the ROSA CLI
Only the user who created the cluster can revoke access for `cluster-admin` users.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to the cluster.

.Procedure

. Enter the following command to revoke the `cluster-admin` access of a user:
+
[source,terminal]
----
$ rosa revoke user cluster-admins --user=myusername --cluster=mycluster
----
+
. Enter the following command to verify that the user no longer has `cluster-admin` access. The output does not list the revoked user.
+
[source,terminal]
----
$ oc get groups cluster-admins
----
