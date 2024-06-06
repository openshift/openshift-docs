// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-understanding-deployment-modes_{context}"]
= Understanding the auto and manual deployment modes

When installing a {product-title} (ROSA) cluster that uses the AWS Security Token Service (STS), you can choose between the `auto` and `manual` modes to create the required AWS Identity and Access Management (IAM) resources.

`auto` mode:: With this mode, the ROSA CLI (`rosa`) immediately creates the required IAM roles and policies, and an OpenID Connect (OIDC) provider in your AWS account.

`manual` mode:: With this mode, `rosa` outputs the `aws` commands needed to create the IAM resources. The corresponding policy JSON files are also saved to the current directory. By using `manual` mode, you can review the generated `aws` commands before running them manually. `manual` mode also enables you to pass the commands to another administrator or group in your organization so that they can create the resources.

[IMPORTANT]
====
If you opt to use `manual` mode, the cluster installation waits until you create the cluster-specific Operator roles and OIDC provider manually. After you create the resources, the installation proceeds. For more information, see _Creating the Operator roles and OIDC provider using OpenShift Cluster Manager_.
====

For more information about the AWS IAM resources required to install ROSA with STS, see _About IAM resources for clusters that use STS_.
