// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-iam-resources.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-sts-ocm-roles-and-permissions-troubleshooting_{context}"]
= Resolving issues with ocm-roles and user-role IAM resources

You may receive an error when trying to create a cluster using the {product-title} (ROSA) CLI, `rosa`.

.Sample output
[source,terminal]
----
E: Failed to create cluster: The sts_user_role is not linked to account '1oNl'. Please create a user role and link it to the account.
----

This error means that the `user-role` IAM role is not linked to your AWS account. The most likely cause of this error is that another user in your Red Hat organization created the `ocm-role` IAM role. Your `user-role` IAM role needs to be created.

[NOTE]
====
After any user sets up an `ocm-role` IAM resource linked to a Red Hat account, any subsequent users wishing to create a cluster in that Red Hat organization must have a `user-role` IAM role to provision a cluster.
====

.Procedure
* Assess the status of your `ocm-role` and `user-role` IAM roles with the following commands:
+
[source,terminal]
----
$ rosa list ocm-role
----
+
.Sample output
+
[source,terminal]
----
I: Fetching ocm roles
ROLE NAME                           ROLE ARN                                          LINKED  ADMIN
ManagedOpenShift-OCM-Role-1158  arn:aws:iam::2066:role/ManagedOpenShift-OCM-Role-1158   No      No
----
+
[source,terminal]
----
$ rosa list user-role
----
+
.Sample output
+
[source,terminal]
----
I: Fetching user roles
ROLE NAME                                   ROLE ARN                                        LINKED
ManagedOpenShift-User.osdocs-Role  arn:aws:iam::2066:role/ManagedOpenShift-User.osdocs-Role  Yes
----

With the results of these commands, you can create and link the missing IAM resources.
