:_mod-docs-content-type: ASSEMBLY
[id="working-with-volume-snapshots-microshift"]
= Working with volume snapshots
include::_attributes/attributes-microshift.adoc[]
:context: volume-snapshots-microshift

toc::[]

Cluster administrators can use volume snapshots to help protect against data loss by using the supported {microshift-short} logical volume manager storage (LVMS) Container Storage Interface (CSI) provider. Familiarity with xref:../microshift_storage/understanding-persistent-storage-microshift.adoc#persistent-volumes_understanding-persistent-storage-microshift[persistent volumes] is required.

A snapshot represents the state of the storage volume in a cluster at a particular point in time. Volume snapshots can also be used to provision new volumes. Snapshots are created as read-only logical volumes (LVs) located on the same device as the original data.

A cluster administrator can complete the following tasks using CSI volume snapshots:

* Create a snapshot of an existing persistent volume claim (PVC).
* Back up a volume snapshot to a secure location.
* Restore a volume snapshot as a different PVC.
* Delete an existing volume snapshot.

[IMPORTANT]
====
Only the logical volume manager storage (LVMS) plugin CSI driver is supported by {microshift-short}.
====

//additional resources for assembly intro; trailing because 1) relevant here, 2) TOC levels, and 2) last called module has addt'l resources
[role="_additional-resources"]
.Additional resources

* xref:../microshift_storage/understanding-persistent-storage-microshift.adoc#persistent-volumes_understanding-persistent-storage-microshift[Understanding persistent volumes]

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/{op-system-version-major}/html/configuring_and_managing_logical_volumes/creating-and-managing-thin-provisioned-volumes_configuring-and-managing-logical-volumes[Configuring and managing logical volumes]

* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/{ocp-version}/html/storage/using-container-storage-interface-csi#persistent-storage-csi-snapshots[CSI snapshots: `VolumeSnapshot` APIs]

* link:https://docs.openshift.com/container-platform/{ocp-version}/rest_api/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1.html[VolumeSnapshot API specification]

include::modules/microshift-lvm-thin-volumes.adoc[leveloffset=+1]

//additional resources for thin volumes module
[role="_additional-resources"]
.Additional resources

* To create a thin pool on the host, see link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/{op-system-version-major}/html/configuring_and_managing_logical_volumes/creating-and-managing-thin-provisioned-volumes_configuring-and-managing-logical-volumes[Creating and managing thin provisioned volumes]

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/{op-system-version-major}/html/configuring_and_managing_logical_volumes/creating-and-managing-thin-provisioned-volumes_configuring-and-managing-logical-volumes#creating-thinly-provisioned-logical-volumes_creating-and-managing-thin-provisioned-volumes[Creating thinly provisioned logical volumes]

* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/{op-system-version-major}/html/configuring_and_managing_logical_volumes/creating-and-managing-thin-provisioned-volumes_configuring-and-managing-logical-volumes[Configuring and managing thin provisioned volumes]

* xref:../microshift_storage/volume-snapshots-microshift.adoc#microshift-storage-classes_volume-snapshots-microshift[Storage classes]

* xref:../microshift_storage/microshift-storage-plugin-overview.adoc#microshift-storage-device-classes_microshift-storage-plugin-overview[Storage device classes]

include::modules/microshift-storage-classes.adoc[leveloffset=+2]

//additional resources for storage classes module
[role="_additional-resources"]
.Additional resources

* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/{ocp-version}/html/storage/dynamic-provisioning#defining-storage-classes_dynamic-provisioning[Defining storage classes]

* xref:../microshift_storage/microshift-storage-plugin-overview.adoc#microshift-storage-device-classes_microshift-storage-plugin-overview[Storage device classes]

include::modules/microshift-storage-vol-snapshot-class.adoc[leveloffset=+1]

//additional resources for volume snapshot classes module
[role="_additional-resources"]
.Additional resources

* link:https://docs.openshift.com/container-platform/{ocp-version}/storage/container_storage_interface/persistent-storage-csi-snapshots.html#volume-snapshot-crds[OpenShift CSI volume snapshots]

include::modules/microshift-storage-about-vol-snapshots.adoc[leveloffset=+1]

include::modules/microshift-storage-creating-vol-snapshot.adoc[leveloffset=+2]

include::modules/microshift-storage-backup-volume-snapshots.adoc[leveloffset=+2]

include::modules/microshift-storage-vol-snapshot-restore.adoc[leveloffset=+2]

//additional resources for volume snapshot restore module
[role="_additional-resources"]
.Additional resources

* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/{ocp-version}/html/storage/using-container-storage-interface-csi#persistent-storage-csi-snapshots-provision_persistent-storage-csi-snapshots[Restoring a volume snapshot]

//this module is reused from OCP; take care in editing for MicroShift
include::modules/persistent-storage-csi-snapshots-delete.adoc[leveloffset=+2]

include::modules/microshift-storage-volume-cloning.adoc[leveloffset=+1]

//additional resources for volume cloning module
[role="_additional-resources"]
.Additional resources

* link:https://docs.openshift.com/container-platform/{ocp-version}/storage/container_storage_interface/persistent-storage-csi-cloning.html[CSI volume cloning]

* link:https://access.redhat.com/documentation/en-us/openshift_container_platform/{ocp-version}/html/storage/configuring-persistent-storage#lvms-creating-volume-clones-in-single-node-openshift_logical-volume-manager-storage[LVMS volume cloning for Single-Node OpenShift]

* To configure the host to enable cloning, see xref:../microshift_storage/volume-snapshots-microshift.adoc#microshift-lvm-thin-volumes_volume-snapshots-microshift[About LVM thin volumes]
