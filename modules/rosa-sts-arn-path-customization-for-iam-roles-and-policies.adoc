// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-sts-arn-path-customization-for-iam-roles-and-policies_{context}"]
= ARN path customization for IAM roles and policies

When you create the AWS IAM roles and policies required for {product-title} (ROSA) clusters that use the AWS Security Token Service (STS), you can specify custom Amazon Resource Name (ARN) paths. This enables you to use role and policy ARN paths that meet the security requirements of your organization.

You can specify custom ARN paths when you create your OCM role, user role, and account-wide roles and policies.

If you define a custom ARN path when you create a set of account-wide roles and policies, the same path is applied to all of the roles and policies in the set. The following example shows the ARNs for a set of account-wide roles and policies. In the example, the ARNs use the custom path `/test/path/dev/` and the custom role prefix `test-env`:

* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Worker-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Support-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-Installer-Role`
* `arn:aws:iam::<account_id>:role/test/path/dev/test-env-ControlPlane-Role`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Worker-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Support-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-Installer-Role-Policy`
* `arn:aws:iam::<account_id>:policy/test/path/dev/test-env-ControlPlane-Role-Policy`

When you create the cluster-specific Operator roles, the ARN path for the relevant account-wide installer role is automatically detected and applied to the Operator roles.

For more information about ARN paths, see link:https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html[Amazon Resource Names (ARNs)] in the AWS documentation.
