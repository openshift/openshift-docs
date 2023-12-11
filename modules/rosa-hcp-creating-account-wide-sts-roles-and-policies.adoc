// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-sts-creating-account-wide-sts-roles-and-policies_{context}"]
= Creating the account-wide STS roles and policies

Before using the {product-title} (ROSA) CLI (`rosa`) to create {hcp-title-first} clusters, create the required account-wide roles and policies, including the Operator policies.

[NOTE]
====
{hcp-title} clusters require account and Operator roles with AWS managed policies attached. Customer managed policies are not supported. For more information regarding AWS managed policies for {hcp-title} clusters, see link:https://docs.aws.amazon.com/ROSA/latest/userguide/security-iam-awsmanpol-account-policies.html[AWS managed policies for ROSA account roles].
====

.Prerequisites

* You have completed the AWS prerequisites for {hcp-title}.
* You have available AWS service quotas.
* You have enabled the ROSA service in the AWS Console.
* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.
* You have logged in to your Red Hat account by using the ROSA CLI.

.Procedure

* If they do not exist in your AWS account, create the required account-wide STS roles and attach the policies by running the following command:
+
[source,terminal]
----
$ rosa create account-roles --hosted-cp
----
+
[source,terminal]
----
$ ACCOUNT_ROLES_PREFIX="${ACCOUNT_ROLES_PREFIX}"
----
+
[source,terminal]
----
$ rosa create account-roles --hosted-cp --prefix $ACCOUNT_ROLES_PREFIX
----
+
For more information regarding AWS managed IAM policies for ROSA, see link:https://docs.aws.amazon.com/ROSA/latest/userguide/security-iam-awsmanpol.html[AWS managed IAM policies for ROSA].
