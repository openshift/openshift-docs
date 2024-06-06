// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc


:_mod-docs-content-type: PROCEDURE
[id="rosa-delete-dedicated-admins_{context}"]
= Revoking `dedicated-admin` access using the ROSA CLI
You can revoke access for a `dedicated-admin` user if you are the user who created the cluster, the organization administrator user, or the super administrator user.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to the cluster.

.Procedure

. Enter the following command to revoke the `dedicated-admin` access of a user:
+
[source,terminal]
----
$ rosa revoke user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
. Enter the following command to verify that your user no longer has `dedicated-admin` access. The output does not list the revoked user.
+
[source,terminal]
----
$ oc get groups dedicated-admins
----
