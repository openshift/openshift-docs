:_mod-docs-content-type: ASSEMBLY
[id="rosa-sts-understanding-the-deployment-workflow"]
= Understanding the ROSA with STS deployment workflow
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-sts-overview-of-the-deployment-workflow

toc::[]

Before you create a {product-title} (ROSA) cluster, you must complete the AWS prerequisites, verify that the required AWS service quotas are available, and set up your environment.

This document provides an overview of the ROSA with STS deployment workflow stages and refers to detailed resources for each stage.

[id="rosa-sts-overview-of-the-deployment-workflow"]
== Overview of the ROSA with STS deployment workflow

The AWS Security Token Service (STS) is a global web service that provides short-term credentials for IAM or federated users. You can use AWS STS with {product-title} (ROSA) to allocate temporary, limited-privilege credentials for component-specific IAM roles. The service enables cluster components to make AWS API calls using secure cloud resource management practices.

You can follow the workflow stages outlined in this section to set up and access a ROSA cluster that uses STS.

. xref:../rosa_planning/rosa-sts-aws-prereqs.adoc#rosa-sts-aws-prereqs[Complete the AWS prerequisites for ROSA with STS]. To deploy a ROSA cluster with STS, your AWS account must meet the prerequisite requirements.
. xref:../rosa_planning/rosa-sts-required-aws-service-quotas.adoc#rosa-sts-required-aws-service-quotas[Review the required AWS service quotas]. To prepare for your cluster deployment, review the AWS service quotas that are required to run a ROSA cluster.
. xref:../rosa_planning/rosa-sts-setting-up-environment.adoc#rosa-sts-setting-up-environment[Set up the environment and install ROSA using STS]. Before you create a ROSA with STS cluster, you must enable ROSA in your AWS account, install and configure the required CLI tools, and verify the configuration of the CLI tools. You must also verify that the AWS Elastic Load Balancing (ELB) service role exists and that the required AWS resource quotas are available.
. xref:../rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc#rosa-sts-creating-a-cluster-quickly[Create a ROSA cluster with STS quickly] or xref:../rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc#rosa-sts-creating-a-cluster-with-customizations[create a cluster using customizations]. Use the ROSA CLI (`rosa`) or {cluster-manager-first} to create a cluster with STS. You can create a cluster quickly by using the default options, or you can apply customizations to suit the needs of your organization.
. xref:../rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc#rosa-sts-accessing-cluster[Access your cluster]. You can configure an identity provider and grant cluster administrator privileges to the identity provider users as required. You can also access a newly-deployed cluster quickly by configuring a `cluster-admin` user.
. xref:../rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc#rosa-sts-deleting-access-cluster[Revoke access to a ROSA cluster for a user]. You can revoke access to a ROSA with STS cluster from a user by using the ROSA CLI or the web console.
. xref:../rosa_install_access_delete_clusters/rosa-sts-deleting-cluster.adoc#rosa-sts-deleting-cluster[Delete a ROSA cluster]. You can delete a ROSA with STS cluster by using the ROSA CLI (`rosa`). After deleting a cluster, you can delete the STS resources by using the AWS Identity and Access Management (IAM) Console.

[id="additional_resources_{context}"]
[role="_additional-resources"]
== Additional resources

* For information about using the ROSA deployment workflow to create a cluster that does not use AWS STS, see xref:../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-getting-started-workflow.adoc#rosa-understanding-the-deployment-workflow[Understanding the ROSA deployment workflow].
