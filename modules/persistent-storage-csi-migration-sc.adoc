// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-migration.adoc

:_mod-docs-content-type: CONCEPT
[id="persistent-storage-csi-migration-sc-implications_{context}"]
= Storage class implications

For new {product-title} 4.13, and later, installations, the default storage class is the CSI storage class. All volumes provisioned using this storage class are CSI persistent volumes (PVs).

For clusters upgraded from 4.12, and earlier, to 4.13, and later, the CSI storage class is created, and is set as the default if no default storage class was set prior to the upgrade. In the very unlikely case that there is a storage class with the same name, the existing storage class remains unchanged. Any existing in-tree storage classes remain, and might be necessary for certain features, such as volume expansion to work for existing in-tree PVs. While storage class referencing to the in-tree storage plugin will continue working, we recommend that you switch the default storage class to the CSI storage class.