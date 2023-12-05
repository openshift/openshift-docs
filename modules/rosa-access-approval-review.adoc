// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-sre-access.adoc

:_mod-docs-content-type: REFERENCE

[id="rosa-policy-access-approval_{context}"]
= Access approval and review
New SRE user access requires management approval. Separated or transferred SRE accounts are removed as authorized users through an automated process. Additionally, the SRE performs periodic access review, including management sign-off of authorized user lists.

The access and identity authorization table includes responsibilities for managing authorized access to clusters, applications, and infrastructure resources. This includes tasks such as providing access control mechanisms, authentication, authorization, and managing access to resources.

[cols="2a,3a,3a",options="header"]
|===
|Resource
|Service responsibilities
|Customer responsibilities

|Logging
|**Red Hat**

- Adhere to an industry standards-based tiered internal access process for platform audit logs.

- Provide native OpenShift RBAC capabilities.

|- Configure OpenShift RBAC to control access to projects and by extension a project's application logs.
- For third-party or custom application logging solutions, the customer is responsible for access management.

|Application networking
|**Red Hat**

- Provide native OpenShift RBAC and `dedicated-admin` capabilities.

|- Configure OpenShift `dedicated-admin` and RBAC to control access to route configuration as required.
- Manage organization administrators for Red Hat to grant access to {cluster-manager}. The cluster manager is used to configure router options and provide service load balancer quota.

|Cluster networking
|**Red Hat**

- Provide customer access controls through {cluster-manager}.

- Provide native OpenShift RBAC and `dedicated-admin` capabilities.

|- Manage Red Hat organization membership of Red Hat accounts.
- Manage organization administrators for Red Hat to grant access to {cluster-manager}.
- Configure OpenShift `dedicated-admin` and RBAC to control access to route configuration as required.

|Virtual networking management
|**Red Hat**

- Provide customer access controls through {cluster-manager}.

|- Manage optional user access to AWS components through {cluster-manager}.

|Virtual storage management
|**Red Hat**

- Provide customer access controls through
Red Hat OpenShift Cluster Manager.

|- Manage optional user access to AWS components through {cluster-manager}.
- Create AWS IAM roles and attached policies necessary to enable ROSA service access.

|Virtual compute management
|**Red Hat**

- Provide customer access controls through
Red Hat OpenShift Cluster Manager.

|- Manage optional user access to AWS components through {cluster-manager}.
- Create AWS IAM roles and attached policies necessary to enable ROSA service access.

|AWS software (public AWS services)
|**AWS**

**Compute:** Provide the Amazon EC2 service, used for ROSA control plane, infrastructure, and worker nodes.

**Storage:** Provide Amazon EBS, used to allow ROSA to provision local node storage and persistent volume storage for the cluster.

**Storage:** Provide Amazon S3, used for the service's built-in image registry.

**Networking:** Provide AWS Identity and Access Management (IAM), used by customers to control access to ROSA resources running on customer accounts.

|- Create AWS IAM roles and attached policies necessary to enable ROSA service access.

- Use IAM tools to apply the appropriate permissions to AWS
resources in the customer account.

- To enable ROSA across your AWS organization, the customer is
responsible for managing AWS Organizations administrators.

- To enable ROSA across your AWS organization, the customer is
responsible for distributing the ROSA entitlement grant using AWS License Manager.

|Hardware and AWS global infrastructure
|**AWS**

- For information about physical access controls for AWS data centers, see link:https://aws.amazon.com/compliance/data-center/controls/[Our Controls] on the AWS Cloud Security page.
|- Customer is not responsible for AWS global infrastructure.
|===