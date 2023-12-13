// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-attaching-virtio-disk-to-windows_{context}"]
= Attaching VirtIO container disk to Windows VMs during installation

You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done during creation of the VM.

.Procedure

. When creating a Windows VM from a template, click *Customize VirtualMachine*.
. Select *Mount Windows drivers disk*.
. Click the *Customize VirtualMachine parameters*.
. Click *Create VirtualMachine*.

After the VM is created, the `virtio-win` SATA CD disk will be attached to the VM.
