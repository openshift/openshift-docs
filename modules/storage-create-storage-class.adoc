// Be sure to set the :StorageClass: and :Provisioner: value in each assembly
// on the line before the include statement for this module. For example, to
// set the StorageClass value to "AWS EBS", add the following line to the
// assembly:
// :StorageClass: AWS EBS
// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws.adoc
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/persistent_storage/rosa-persistent-storage-aws-efs-csi.adoc
// * storage/container_storage_interface/osd-persistent-storage-aws-efs-csi.adoc

:_mod-docs-content-type: PROCEDURE
[id="storage-create-storage-class_{context}"]
= Creating the {StorageClass} storage class

Storage classes are used to differentiate and delineate storage levels and
usages. By defining a storage class, users can obtain dynamically provisioned
persistent volumes.

ifeval::["{Provisioner}" == "efs.csi.aws.com"]
The _link:https://github.com/openshift/aws-efs-csi-driver-operator[AWS EFS CSI Driver Operator] (a Red Hat operator)_, after being installed, does not create a storage class by default. However, you can manually create the AWS EFS storage class.
endif::[]



