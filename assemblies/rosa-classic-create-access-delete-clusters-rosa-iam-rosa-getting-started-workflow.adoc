:_mod-docs-content-type: ASSEMBLY
[id="rosa-understanding-the-deployment-workflow"]
= Understanding the ROSA deployment workflow
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-understanding-the-deployment-workflow

toc::[]

Before you create a {product-title} (ROSA) cluster, you must complete the AWS prerequisites, verify that the required AWS service quotas are available, and set up your environment.

This document provides an overview of the ROSA workflow stages and refers to detailed resources for each stage.

include::snippets/rosa-sts.adoc[]

[id="rosa-overview-of-the-deployment-workflow"]
== Overview of the ROSA deployment workflow

You can follow the workflow stages outlined in this section to set up and access a {product-title} (ROSA) cluster.

. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-aws-prereqs.adoc#prerequisites[Perform the AWS prerequisites]. To deploy a ROSA cluster, your AWS account must meet the prerequisite requirements.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-required-aws-service-quotas.adoc#rosa-required-aws-service-quotas[Review the required AWS service quotas]. To prepare for your cluster deployment, review the AWS service quotas that are required to run a ROSA cluster.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-config-aws-account.adoc#rosa-config-aws-account[Configure your AWS account]. Before you create a ROSA cluster, you must enable ROSA in your AWS account, install and configure the AWS CLI (`aws`) tool, and verify the AWS CLI tool configuration.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-installing-rosa.adoc#rosa-installing-cli[Install the ROSA and OpenShift CLI tools and verify the AWS servce quotas]. Install and configure the ROSA CLI (`rosa`) and the OpenShift CLI (`oc`). You can verify if the required AWS resource quotas are available by using the ROSA CLI.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-creating-cluster.adoc#rosa-creating-cluster[Create a ROSA cluster] or xref:../../rosa_install_access_delete_clusters/rosa-aws-privatelink-creating-cluster.adoc#rosa-aws-privatelink-creating-cluster[Create a ROSA cluster using AWS PrivateLink]. Use the ROSA CLI (`rosa`) to create a cluster. You can optionally create a ROSA cluster with AWS PrivateLink.
. xref:../../rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc#rosa-sts-accessing-cluster[Access a cluster]. You can configure an identity provider and grant cluster administrator privileges to the identity provider users as required. You can also access a newly deployed cluster quickly by configuring a `cluster-admin` user.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc#rosa-deleting-access-cluster[Revoke access to a ROSA cluster for a user]. You can revoke access to a ROSA cluster from a user by using the ROSA CLI or the web console.
. xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-cluster.adoc#rosa-deleting-cluster[Delete a ROSA cluster]. You can delete a ROSA cluster by using the ROSA CLI (`rosa`).

[id="additional_resources_{context}"]
[role="_additional-resources"]
== Additional resources

* For information about using the ROSA deployment workflow to create a cluster that uses the AWS Security Token Service (STS), see xref:../../rosa_getting_started/rosa-sts-getting-started-workflow.adoc#rosa-sts-overview-of-the-deployment-workflow[Understanding the ROSA with STS deployment workflow].
* xref:../../rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc#rosa-sts-config-identity-providers[Configuring identity providers]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-cluster.adoc#rosa-deleting-cluster[Deleting a cluster]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-deleting-access-cluster.adoc#rosa-deleting-access-cluster[Deleting access to a cluster]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-quickstart.adoc#rosa-command-reference[Command quick reference for creating clusters and users]
