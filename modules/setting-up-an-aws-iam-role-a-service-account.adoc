// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: PROCEDURE
[id="setting-up-an-aws-iam-role-a-service-account_{context}"]
= Setting up an AWS IAM role for a service account

Create an AWS Identity and Access Management (IAM) role to be assumed by a service account in your {product-title} cluster. Attach the permissions that are required by your service account to run AWS SDK operations in a pod.

.Prerequisites

* You have the permissions required to install and configure IAM roles in your AWS account.
* You have access to a {product-title} cluster that uses the AWS Security Token Service (STS). Admin-level user privileges are not required.
* You have the Amazon Resource Name (ARN) for the OpenID Connect (OIDC) provider that is configured as the service account issuer in your {product-title} with STS cluster.
+
[NOTE]
====
In {product-title} with STS clusters, the OIDC provider is created during install and set as the service account issuer by default. If you do not know the OIDC provider ARN, contact your cluster administrator.
====
* You have installed the AWS CLI (`aws`).

.Procedure

. Create a file named `trust-policy.json` with the following JSON configuration:
+
--
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "<oidc_provider_arn>" <1>
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "<oidc_provider_name>:sub": "system:serviceaccount:<project_name>:<service_account_name>" <2>
                }
            }
        }
    ]
}
----
<1> Replace `<oidc_provider_arn>` with the ARN of your OIDC provider, for example `arn:aws:iam::<aws_account_id>:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/1v3r0n44npxu4g58so46aeohduomfres`.
<2> Limits the role to the specified project and service account. Replace `<oidc_provider_name>` with the name of your OIDC provider, for example `rh-oidc.s3.us-east-1.amazonaws.com/1v3r0n44npxu4g58so46aeohduomfres`. Replace `<project_name>:<service_account_name>` with your project name and service account name, for example `my-project:test-service-account`.
+
[NOTE]
====
Alternatively, you can limit the role to any service account within the specified project by using `"<oidc_provider_name>:sub": "system:serviceaccount:<project_name>:*"`. If you supply the `*` wildcard, you must replace `StringEquals` with `StringLike` in the preceding line.
====
--

. Create an AWS IAM role that uses the trust policy that is defined in the `trust-policy.json` file:
+
[source,terminal]
----
$ aws iam create-role \
    --role-name <aws_iam_role_name> \ <1>
    --assume-role-policy-document file://trust-policy.json <2>
----
<1> Replace `<aws_iam_role_name>` with the name of your IAM role, for example `pod-identity-test-role`.
<2> References the `trust-policy.json` file that you created in the preceding step.
+
.Example output:
[source,terminal]
----
ROLE    arn:aws:iam::<aws_account_id>:role/<aws_iam_role_name>        2022-09-28T12:03:17+00:00       /       AQWMS3TB4Z2N3SH7675JK   <aws_iam_role_name>
ASSUMEROLEPOLICYDOCUMENT        2012-10-17
STATEMENT       sts:AssumeRoleWithWebIdentity   Allow
STRINGEQUALS    system:serviceaccount:<project_name>:<service_account_name>
PRINCIPAL       <oidc_provider_arn>
----
+
Retain the ARN for the role in the output. The format of the role ARN is `arn:aws:iam::<aws_account_id>:role/<aws_iam_role_name>`.

. Attach any managed AWS permissions that are required when the service account runs AWS SDK operations in your pod:
+
[source,terminal]
----
$ aws iam attach-role-policy \
    --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess \ <1>
    --role-name <aws_iam_role_name> <2>
----
<1> The policy in this example adds read-only access permissions to the IAM role.
<2> Replace `<aws_iam_role_name>` with the name of the IAM role that you created in the preceding step.

. Optional: Add custom attributes or a permissions boundary to the role. For more information, see link:https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html[Creating a role to delegate permissions to an AWS service] in the AWS documentation.
