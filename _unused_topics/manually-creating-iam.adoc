:_mod-docs-content-type: ASSEMBLY
[id="manually-creating-iam-aws"]
= Manually creating IAM for AWS
include::_attributes/common-attributes.adoc[]
:context: manually-creating-iam-aws

//TO-DO: this should be one file for AWS, Azure, and GCP with conditions for specifics.

toc::[]

In environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace, you can put the Cloud Credential Operator (CCO) into manual mode before you install the cluster.

include::modules/alternatives-to-storing-admin-secrets-in-kube-system.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

// AWS only. Condition out if combining topic for AWS/Azure/GCP.
* To learn how to use the CCO utility (`ccoctl`) to configure the CCO to use the AWS STS, see xref:../../authentication/managing_cloud_provider_credentials/cco-mode-sts.adoc#cco-mode-sts[Using manual mode with STS].

// Not supported in Azure. Condition out if combining topic for AWS/Azure/GCP.
* To learn how to rotate or remove the administrator-level credential secret after installing {product-title}, see xref:../../post_installation_configuration/cluster-tasks.adoc#post-install-rotate-remove-cloud-creds[Rotating or removing cloud provider credentials].

* For a detailed description of all available CCO credential modes and their supported platforms, see xref:../../authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.adoc#about-cloud-credential-operator[About the Cloud Credential Operator].

include::modules/manually-create-identity-access-management.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../updating/preparing_for_updates/preparing-manual-creds-update.adoc#preparing-manual-creds-update[Preparing to update a cluster with manually maintained credentials]

include::modules/mint-mode.adoc[leveloffset=+1]

include::modules/mint-mode-with-removal-of-admin-credential.adoc[leveloffset=+1]

[id="manually-creating-iam-aws-next-steps"]
== Next steps

* Install an {product-title} cluster:
** xref:../../installing/installing_aws/installing-aws-default.adoc#installing-aws-default[Installing a cluster quickly on AWS] with default options on installer-provisioned infrastructure
** xref:../../installing/installing_aws/installing-aws-customizations.adoc#installing-aws-customizations[Install a cluster with cloud customizations on installer-provisioned infrastructure]
** xref:../../installing/installing_aws/installing-aws-network-customizations.adoc#installing-aws-network-customizations[Install a cluster with network customizations on installer-provisioned infrastructure]
** xref:../../installing/installing_aws/installing-aws-user-infra.adoc#installing-aws-user-infra[Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates]
