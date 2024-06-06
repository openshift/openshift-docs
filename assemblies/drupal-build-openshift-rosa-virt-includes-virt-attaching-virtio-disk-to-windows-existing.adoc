// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms/virt-installing-qemu-guest-agent.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-attaching-virtio-disk-to-windows-existing_{context}"]
= Attaching VirtIO container disk to an existing Windows VM

You must attach the VirtIO container disk to the Windows VM to install the necessary Windows drivers. This can be done to an existing VM.

.Procedure

. Navigate to the existing Windows VM, and click *Actions* -> *Stop*.
. Go to *VM Details* -> *Configuration* -> *Disks* and click *Add disk*.
. Add `windows-driver-disk` from container source, set the *Type* to *CD-ROM*, and then set the *Interface* to *SATA*.
. Click *Save*.
. Start the VM, and connect to a graphical console.