// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-troubleshooting-cluster-deletion_{context}"]
= Repairing a cluster that cannot be deleted

In specific cases, the following error appears in {cluster-manager-url} if you attempt to delete your cluster.

[source,terminal]
----
Error deleting cluster
CLUSTERS-MGMT-400: Failed to delete cluster <hash>: sts_user_role is not linked to your account. sts_ocm_role is linked to your organization <org number> which requires sts_user_role to be linked to your Red Hat account <account ID>.Please create a user role and link it to the account: User Account <account ID> is not authorized to perform STS cluster operations

Operation ID: b0572d6e-fe54-499b-8c97-46bf6890011c
----

If you try to delete your cluster from the CLI, the following error appears.

[source,terminal]
----
E: Failed to delete cluster <hash>: sts_user_role is not linked to your account. sts_ocm_role is linked to your organization <org_number> which requires sts_user_role to be linked to your Red Hat account <account_id>.Please create a user role and link it to the account: User Account <account ID> is not authorized to perform STS cluster operations
----

This error occurs when the `user-role` is unlinked or deleted.

.Procedure

. Run the following command to create the `user-role` IAM resource:
+
[source,terminal]
----
$ rosa create user-role
----
+
. After you see that the role has been created, you can delete the cluster. The following confirms that the role was created and linked:
+
[source,terminal]
----
I: Successfully linked role ARN <user role ARN> with account <account ID>
----