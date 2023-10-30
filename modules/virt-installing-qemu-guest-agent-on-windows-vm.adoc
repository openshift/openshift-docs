// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-qemu-guest-agent-on-windows-vm_{context}"]
= Installing the QEMU guest agent on a Windows VM

For Windows virtual machines (VMs), the QEMU guest agent is included in the VirtIO drivers. You can install the drivers during a Windows installation or on an existing Windows VM.

[NOTE]
====
To create snapshots of an online (Running state) VM with the highest integrity, install the QEMU guest agent.

The QEMU guest agent takes a consistent snapshot by attempting to quiesce the VM file system as much as possible, depending on the system workload. This ensures that in-flight I/O is written to the disk before the snapshot is taken. If the guest agent is not present, quiescing is not possible and a best-effort snapshot is taken. The conditions under which the snapshot was taken are reflected in the snapshot indications that are displayed in the web console or CLI.
====

.Procedure

. In the Windows guest operating system, use the *File Explorer* to navigate to the `guest-agent` directory in the `virtio-win` CD drive.
. Run the `qemu-ga-x86_64.msi` installer.

.Verification
. Obtain a list of network services by running the following command:
+
[source,terminal]
----
$ net start
----

. Verify that the output contains the `QEMU Guest Agent`.