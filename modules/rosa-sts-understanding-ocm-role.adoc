// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
//
:_mod-docs-content-type: CONCEPT
[id="rosa-sts-understanding-ocm-role_{context}"]
= Understanding the {cluster-manager} role

Creating ROSA clusters in {cluster-manager-url} require an `ocm-role` IAM role. The basic `ocm-role` IAM role permissions let you to perform cluster maintenance within {cluster-manager}. To automatically create the operator roles and OpenID Connect (OIDC) provider, you must add the `--admin` option to the `rosa create` command. This command creates an `ocm-role` resource with additional permissions needed for administrative tasks.

[NOTE]
====
This elevated IAM role allows {cluster-manager} to automatically create the cluster-specific Operator roles and OIDC provider during cluster creation. For more information about this automatic role and policy creation, see the "Methods of account-wide role creation" link in Additional resources.
====

[id="rosa-sts-understanding-user-role_{context}"]
== Understanding the user role

In addition to an `ocm-role` IAM role, you must create a user role so that {product-title} can verify your AWS identity. This role has no permissions, and it is only used to create a trust relationship between the installer account and your `ocm-role` resources.

The following tables show the associated basic and administrative permissions for the `ocm-role` resource.

.Associated permissions for the basic `ocm-role` resource
[cols="1,2",options="header"]
|===

|Resource|Description

| `iam:GetOpenIDConnectProvider`
| This permission allows the basic role to retrieve information about the specified OpenID Connect (OIDC) provider.
| `iam:GetRole`
| This permission allows the basic role to retrieve any information for a specified role. Some of the data returned include the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role.
| `iam:ListRoles`
| This permission allows the basic role to list the roles within a path prefix.
| `iam:ListRoleTags`
| This permission allows the basic role to list the tags on a specified role.
| `ec2:DescribeRegions`
| This permission allows the basic role to return information about all of the enabled regions on your account.
| `ec2:DescribeRouteTables`
| This permission allows the basic role to return information about all of your route tables.
| `ec2:DescribeSubnets`
| This permission allows the basic role to return information about all of your subnets.
| `ec2:DescribeVpcs`
| This permission allows the basic role to return information about all of your virtual private clouds (VPCs).
| `sts:AssumeRole`
| This permission allows the basic role to retrieve temporary security credentials to access AWS resources that are beyond its normal permissions.
| `sts:AssumeRoleWithWebIdentity`
| This permission allows the basic role to retrieve temporary security credentials for users authenticated their account with a web identity provider.

|===

.Additional permissions for the admin `ocm-role` resource
[cols="1,2",options="header"]
|===

|Resource|Description

| `iam:AttachRolePolicy`
| This permission allows the admin role to attach a specified policy to the desired IAM role.
| `iam:CreateOpenIDConnectProvider`
| This permission creates a resource that describes an identity provider, which supports OpenID Connect (OIDC). When you create an OIDC provider with this permission, this provider establishes a trust relationship between the provider and AWS.
| `iam:CreateRole`
| This permission allows the admin role to create a role for your AWS account.
| `iam:ListPolicies`
| This permission allows the admin role to list any policies associated with your AWS account.
| `iam:ListPolicyTags`
| This permission allows the admin role to list any tags on a designated policy.
| `iam:PutRolePermissionsBoundary`
| This permission allows the admin role to change the permissions boundary for a user based on a specified policy.
| `iam:TagRole`
| This permission allows the admin role to add tags to an IAM role.

|===
