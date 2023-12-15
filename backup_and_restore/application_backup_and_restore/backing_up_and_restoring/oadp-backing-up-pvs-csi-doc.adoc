:_mod-docs-content-type: ASSEMBLY
[id="oadp-backing-up-pvs-csi-doc"]
= Backing up persistent volumes with CSI snapshots
include::_attributes/common-attributes.adoc[]
:context: backing-up-applications

toc::[]

You back up persistent volumes with Container Storage Interface (CSI) snapshots by editing the `VolumeSnapshotClass` custom resource (CR) of the cloud storage before you create the `Backup` CR, see xref:../../../storage/container_storage_interface/persistent-storage-csi-snapshots.adoc#persistent-storage-csi-snapshots-overview_persistent-storage-csi-snapshots[CSI volume snapshots].

For more information see xref:../../../backup_and_restore/application_backup_and_restore/backing_up_and_restoring/oadp-creating-backup-cr.adoc#oadp-creating-backup-cr-doc[Creating a Backup CR].

.Prerequisites

* The cloud provider must support CSI snapshots.
* You must enable CSI in the `DataProtectionApplication` CR.

.Procedure

* Add the `metadata.labels.velero.io/csi-volumesnapshot-class: "true"` key-value pair to the `VolumeSnapshotClass` CR:
+
[source,yaml,subs="attributes+"]
----
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: <volume_snapshot_class_name>
  labels:
    velero.io/csi-volumesnapshot-class: "true"
driver: <csi_driver>
deletionPolicy: Retain
----

You can now create a `Backup` CR.
