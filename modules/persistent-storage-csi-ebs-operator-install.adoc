// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-ebs.adoc

[id="persistent-storage-csi-ebs-operator-install_{context}"]
= Installing the AWS Elastic Block Store CSI Driver Operator

The AWS Elastic Block Store (EBS) Container Storage Interface (CSI) Driver Operator enables the replacement of the existing AWS EBS in-tree storage plugin.

[IMPORTANT]
====
AWS EBS CSI Driver Operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.
====

Installing the AWS EBS CSI Driver Operator provides the CSI driver that allows you to use CSI volumes with the `PersistentVolumeClaims`, `PersistentVolumes`, and `StorageClasses` API objects in {product-title}. It also deploys the StorageClass that you can use to create persistent volume claims (PVCs).

The AWS EBS CSI Driver Operator is not installed in {product-title} by default. Use the following procedure to install and configure this Operator to enable the AWS EBS CSI driver in your cluster.

.Prerequisites
* Access to the {product-title} web console.

.Procedure
To install the AWS EBS CSI Driver Operator from the web console:

. Log in to the web console.

. Navigate to *Operators* -> *OperatorHub*.

. To locate the AWS EBS CSI Driver Operator, type *AWS EBS CSI* into the filter box.

. Click *Install*.

. On the *Install Operator* page, be sure that *All namespaces on the cluster (default)* is selected. Select *openshift-aws-ebs-csi-driver-operator* from the *Installed Namespace* drop-down menu.

. Adjust the values for *Update Channel* and *Approval Strategy* to the values that you want.

. Click *Install*.

Once finished, the AWS EBS CSI Driver Operator is listed in the *Installed Operators* section of the web console.
