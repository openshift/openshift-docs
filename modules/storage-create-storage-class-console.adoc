// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws-efs-csi.adoc
// * storage/container_storage_interface/osd-persistent-storage-aws-efs-csi.adoc

:_mod-docs-content-type: PROCEDURE
[id="storage-create-storage-class-console_{context}"]
= Creating the {StorageClass} storage class using the console

[role="_abstract"]
.Procedure

. In the {product-title} console, click *Storage* -> *StorageClasses*.

. On the *StorageClasses* page, click *Create StorageClass*.

. On the *StorageClass* page, perform the following steps:

.. Enter a name to reference the storage class.

.. Optional: Enter the description.

.. Select the reclaim policy.

.. Select *`{Provisioner}`* from the *Provisioner* drop-down list.
+
ifeval::["{Provisioner}" == "kubernetes.io/aws-ebs"]
[NOTE]
====
To create the storage class with the equivalent CSI driver, select `{CsiDriver}` from the drop-down list. For more details, see _AWS Elastic Block Store CSI Driver Operator_.
====
endif::[]

.. Optional: Set the configuration parameters for the selected provisioner.

. Click *Create*.