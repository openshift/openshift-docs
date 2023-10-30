// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-vm-snapshot-cli_{context}"]
= Deleting a virtual machine snapshot in the CLI

You can delete an existing virtual machine (VM) snapshot by deleting the appropriate `VirtualMachineSnapshot` object.

.Prerequisites

* Install the OpenShift CLI (`oc`).

.Procedure

* Delete the `VirtualMachineSnapshot` object:
+
[source,terminal]
----
$ oc delete vmsnapshot <snapshot_name>
----
+
The snapshot controller deletes the `VirtualMachineSnapshot` along with the associated `VirtualMachineSnapshotContent` object.

.Verification

* Verify that the snapshot is deleted and no longer attached to this VM:
+
[source,terminal]
----
$ oc get vmsnapshot
----
