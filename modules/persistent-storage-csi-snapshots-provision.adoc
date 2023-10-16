// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-provision_{context}"]
= Volume snapshot provisioning

There are two ways to provision snapshots: dynamically and manually.

[id="snapshots-dynamic-provisioning_{context}"]
== Dynamic provisioning

Instead of using a preexisting snapshot, you can request that a snapshot be taken dynamically from a persistent volume claim. Parameters are specified using a `VolumeSnapshotClass` CRD.

[id="snapshots-manual-provisioning_{context}"]
== Manual provisioning

As a cluster administrator, you can manually pre-provision a number of `VolumeSnapshotContent` objects. These carry the real volume snapshot details available to cluster users.
