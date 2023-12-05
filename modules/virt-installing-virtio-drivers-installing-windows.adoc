// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-virtio-drivers-installing-windows_{context}"]
= Installing VirtIO drivers during Windows installation

You can install the VirtIO drivers while installing Windows on a virtual machine (VM).

[NOTE]
====
This procedure uses a generic approach to the Windows installation and the installation method might differ between versions of Windows. See the documentation for the version of Windows that you are installing.
====

.Prerequisites

* A storage device containing the `virtio` drivers must be attached to the VM.

.Procedure

. In the Windows operating system, use the `File Explorer` to navigate to the `virtio-win` CD drive.
. Double-click the drive to run the appropriate installer for your VM.
+
For a 64-bit vCPU, select the `virtio-win-gt-x64` installer. 32-bit vCPUs are no longer supported.

. Optional: During the *Custom Setup* step of the installer, select the device drivers you want to install. The recommended driver set is selected by default.
. After the installation is complete, select *Finish*.
. Reboot the VM.

.Verification

. Open the system disk on the PC. This is typically `C:`.
. Navigate to *Program Files* -> *Virtio-Win*.

If the *Virtio-Win* directory is present and contains a sub-directory for each driver, the installation was successful.
