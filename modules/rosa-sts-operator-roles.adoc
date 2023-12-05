// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

:_mod-docs-content-type: REFERENCE
[id="rosa-sts-operator-roles_{context}"]
= Cluster-specific Operator IAM role reference

This section provides details about the Operator IAM roles that are required for {product-title} (ROSA) deployments that use STS. The cluster Operators use the Operator roles to obtain the temporary permissions required to carry out cluster operations, such as managing back-end storage, cloud provider credentials, and external access to a cluster.

When you create the Operator roles, the account-wide Operator policies for the matching cluster version are attached to the roles. The Operator policies are tagged with the Operator and version they are compatible with. The correct policy for an Operator role is determined by using the tags.

[NOTE]
====
If more than one matching policy is available in your account for an Operator role, an interactive list of options is provided when you create the Operator.
====

.ROSA cluster-specific Operator roles
[cols="1,2",options="header"]
|===

|Resource|Description

|`<cluster_name>-<hash>-openshift-cluster-csi-drivers-ebs-cloud-credentials`
|An IAM role required by ROSA to manage back-end storage through the Container Storage Interface (CSI).

|`<cluster_name>-<hash>-openshift-machine-api-aws-cloud-credentials`
|An IAM role required by the ROSA Machine Config Operator to perform core cluster functionality.

|`<cluster_name>-<hash>-openshift-cloud-credential-operator-cloud-credentials`
|An IAM role required by the ROSA Cloud Credential Operator to manage cloud provider credentials.


|`<cluster_name>-<hash>-openshift-cloud-network-config-controller-credentials`
|An IAM role required by the cloud network config controller to manage cloud network configuration for a cluster.

|`<cluster_name>-<hash>-openshift-image-registry-installer-cloud-credentials`
|An IAM role required by the ROSA Image Registry Operator to manage the {product-registry} storage in AWS S3 for a cluster.

|`<cluster_name>-<hash>-openshift-ingress-operator-cloud-credentials`
|An IAM role required by the ROSA Ingress Operator to manage external access to a cluster.

|`<cluster_name>-<hash>-openshift-cloud-network-config-controller-cloud-credentials`
|An IAM role required by the cloud network config controller to manage cloud network credentials for a cluster.

|===
