// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-local.adoc

[id="local-storage-metrics_{context}"]
= Local Storage Operator Metrics

{product-title} provides the following metrics for the Local Storage Operator:

* `lso_discovery_disk_count`: total number of discovered devices on each node

* `lso_lvset_provisioned_PV_count`: total number of PVs created by `LocalVolumeSet` objects

* `lso_lvset_unmatched_disk_count`: total number of disks that Local Storage Operator did not select for provisioning because of mismatching criteria

* `lso_lvset_orphaned_symlink_count`: number of devices with PVs that no longer match `LocalVolumeSet` object criteria

* `lso_lv_orphaned_symlink_count`: number of devices with PVs that no longer match `LocalVolume` object criteria

* `lso_lv_provisioned_PV_count`: total number of provisioned PVs for `LocalVolume`

To use these metrics, be sure to:

* Enable support for monitoring when installing the Local Storage Operator.

* When upgrading to {product-title} 4.9 or later, enable metric support manually by adding the `operator-metering=true` label to the namespace.
