// Module included in the following assemblies:
//
// * virt/backup_restore/virt-managing-vm-snapshots.adoc
// * virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-installing-virtio-drivers-existing-windows_{context}"]
= Installing VirtIO drivers from a SATA CD drive on an existing Windows VM

You can install the VirtIO drivers from a SATA CD drive on an existing Windows virtual machine (VM).

[NOTE]
====
This procedure uses a generic approach to adding drivers to Windows. See the installation documentation for your version of Windows for specific installation steps.
====

.Prerequisites

* A storage device containing the virtio drivers must be attached to the VM as a SATA CD drive.

.Procedure

. Start the VM and connect to a graphical console.
. Log in to a Windows user session.
. Open *Device Manager* and expand *Other devices* to list any *Unknown device*.
.. Open the *Device Properties* to identify the unknown device.
.. Right-click the device and select *Properties*.
.. Click the *Details* tab and select *Hardware Ids* in the *Property* list.
.. Compare the *Value* for the *Hardware Ids* with the supported VirtIO drivers.

. Right-click the device and select *Update Driver Software*.
. Click *Browse my computer for driver software* and browse to the attached
SATA CD drive, where the VirtIO drivers are located. The drivers are arranged
hierarchically according to their driver type, operating system,
and CPU architecture.
. Click *Next* to install the driver.
. Repeat this process for all the necessary VirtIO drivers.
. After the driver installs, click *Close* to close the window.
. Reboot the VM to complete the driver installation.
