:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-sts-ocm-role
[id="rosa-sts-ocm-role"]
= ROSA IAM role resources

toc::[]

{product-title} (ROSA) web UI requires that you have specific permissions on your AWS account that create a trust relationship to provide the end-user experience at {cluster-manager-url} and for the `rosa` command line interface (CLI).

This trust relationship is achieved through the creation and association of the `ocm-role` AWS IAM role. This role has a trust policy with the AWS installer that links your Red Hat account to your AWS account. In addition, you also need a `user-role` AWS IAM role for each web UI user, which serves to identify these users. This `user-role` AWS IAM role has no permissions.

The AWS IAM roles required to use {cluster-manager} are:

* `ocm-role`
* `user-role`

Whether you manage your clusters using the ROSA CLI (`rosa`) or {cluster-manager} web UI, you must create the account-wide roles, known as `account-roles` in the ROSA CLI, by using the ROSA CLI. These account roles are necessary for your first cluster, and these roles can be used across multiple clusters. These required account roles are:

* `Worker-Role`
* `Support-Role`
* `Installer-Role`
* `ControlPlane-Role`

[NOTE]
====
Role creation does not request your AWS access or secret keys. AWS Security Token Service (STS) is used as the basis of this workflow. AWS STS uses temporary, limited-privilege credentials to provide authentication.
====

For more information about creating these roles, see xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-account-wide-roles-and-policies[Account-wide IAM role and policy reference].

Cluster-specific Operator roles, known as `operator-roles` in the ROSA CLI, obtain the temporary permissions required to carry out cluster operations, such as managing back-end storage, ingress, and registry. These roles are required by the cluster that you create. These required Operator roles are:

* `<cluster_name>-<hash>-openshift-cluster-csi-drivers-ebs-cloud-credentials`
* `<cluster_name>-<hash>-openshift-cloud-network-config-controller-credentials`
* `<cluster_name>-<hash>-openshift-machine-api-aws-cloud-credentials`
* `<cluster_name>-<hash>-openshift-cloud-credential-operator-cloud-credentials`
* `<cluster_name>-<hash>-openshift-image-registry-installer-cloud-credentials`
* `<cluster_name>-<hash>-openshift-ingress-operator-cloud-credentials`

For more information on creating these roles, see xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-operator-roles_rosa-sts-about-iam-resources[Cluster-specific Operator IAM role reference].

include::modules/rosa-sts-about-ocm-role.adoc[leveloffset=+1]

[discrete]
[id="additional-resources-about-ocm-role"]
[role="_additional-resources"]
== Additional resources
* See xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-understanding-ocm-role[Understanding the OpenShift Cluster Manager role]

include::modules/rosa-sts-ocm-role-creation.adoc[leveloffset=+2]
include::modules/rosa-sts-about-user-role.adoc[leveloffset=+1]
include::modules/rosa-sts-user-role-creation.adoc[leveloffset=+2]

[IMPORTANT]
====
If you unlink or delete your `user-role` IAM role prior to deleting your cluster, an error prevents you from deleting your cluster. You must create or relink this role to proceed with the deletion process. See xref:../support/troubleshooting/rosa-troubleshooting-deployments.adoc#rosa-troubleshooting-cluster-deletion_rosa-troubleshooting-cluster-deployments[Repairing a cluster that cannot be deleted] for more information.
====

include::modules/rosa-sts-aws-requirements-association-concept.adoc[leveloffset=+1]
include::modules/rosa-sts-aws-requirements-creating-association.adoc[leveloffset=+2]
include::modules/rosa-sts-aws-requirements-creating-multi-association.adoc[leveloffset=+2]

[role="_additional-resources"]
== Additional resources
* See xref:../support/troubleshooting/rosa-troubleshooting-iam-resources.adoc#rosa-sts-ocm-roles-and-permissions-troubleshooting[Troubleshooting IAM roles]
* See xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-account-wide-roles-and-policies[Account-wide IAM role and policy reference] for a list of IAM roles needed for cluster creation.