// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-creating-operator-roles-and-oidc-manually-ocm_{context}"]
= Creating the Operator roles and OIDC provider using {cluster-manager}

If you use {cluster-manager-first} to install your cluster and opt to create the required AWS IAM Operator roles and the OIDC provider using `manual` mode, you are prompted to select one of the following methods to install the resources. The options are provided to enable you to choose a resource creation method that suits the needs of your organization:

//CloudFormation:: You can use this method to create the Operator roles and the OIDC provider from the CLI using an AWS CloudFormation template and a parameter file. For more information about AWS CloudFormation, see the link:https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html[AWS documentation].

AWS CLI (`aws`):: With this method, you can download and extract an archive file that contains the `aws` commands and policy files required to create the IAM resources. Run the provided CLI commands from the directory that contains the policy files to create the Operator roles and the OIDC provider.

The {product-title} (ROSA) CLI, `rosa`:: You can run the commands provided by this method to create the Operator roles and the OIDC provider for your cluster using `rosa`.

If you use `auto` mode, {cluster-manager} creates the Operator roles and the OIDC provider automatically, using the permissions provided through the {cluster-manager} IAM role. To use this feature, you must apply admin privileges to the role.
