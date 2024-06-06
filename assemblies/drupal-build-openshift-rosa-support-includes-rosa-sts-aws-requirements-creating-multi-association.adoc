// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-iam-resources.adoc
// * rosa_planning/rosa-sts-ocm-role.adoc
// * rosa_planning/rosa-sts-aws-prereqs.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-associating-multiple-account_{context}"]
= Associating multiple AWS accounts with your Red Hat organization

You can associate multiple AWS accounts with your Red Hat organization. Associating multiple accounts lets you create {product-title} (ROSA) clusters on any of the associated AWS accounts from your Red Hat organization.

With this feature, you can create clusters in different AWS regions by using multiple AWS profiles as region-bound environments.

.Prerequisites

* You have an AWS account.
* You are using {cluster-manager-url} to create clusters.
* You have the permissions required to install AWS account-wide roles.
* You have installed and configured the latest AWS (`aws`) and ROSA (`rosa`) CLIs on your installation host.
* You have created your `ocm-role` and `user-role` IAM roles.

.Procedure

To associate an additional AWS account, first create a profile in your local AWS configuration. Then, associate the account with your Red Hat organization by creating the `ocm-role`, user, and account roles in the additional AWS account.

To create the roles in an additional region, specify the `--profile <aws-profile>` parameter when running the `rosa create` commands and replace `<aws_profile>` with the additional account profile name:

* To specify an AWS account profile when creating an {cluster-manager} role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> ocm-role
----

* To specify an AWS account profile when creating a user role:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> user-role
----

* To specify an AWS account profile when creating the account roles:
+
[source,terminal]
----
$ rosa create --profile <aws_profile> account-roles
----

[NOTE]
====
If you do not specify a profile, the default AWS profile is used.
====
