// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc
// * virt/backup_restore/virt-managing-vm-snapshots.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-updating-virtio-drivers-windows_{context}"]
= Updating VirtIO drivers on a Windows VM

Update the `virtio` drivers on a Windows virtual machine (VM) by using the Windows Update service.

.Prerequisites

* The cluster must be connected to the internet. Disconnected clusters cannot reach the Windows Update service.

.Procedure

. In the Windows Guest operating system, click the *Windows* key and select *Settings*.
. Navigate to *Windows Update* -> *Advanced Options* -> *Optional Updates*.
. Install all updates from *Red Hat, Inc.*.
. Reboot the VM.

.Verification

. On the Windows VM, navigate to the *Device Manager*.
. Select a device.
. Select the *Driver* tab.
. Click *Driver Details* and confirm that the `virtio` driver details displays the correct version.