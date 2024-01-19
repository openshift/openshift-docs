// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-generalizing-windows-sysprep_{context}"]
= Generalizing a Windows VM image

You can generalize a Windows operating system image to remove all system-specific configuration data before you use the image to create a new virtual machine (VM).

Before generalizing the VM, you must ensure the `sysprep` tool cannot detect an answer file after the unattended Windows installation.

.Prerequisites

* A running Windows VM with the QEMU guest agent installed.

.Procedure

. In the {product-title} console, click *Virtualization* -> *VirtualMachines*.
. Select a Windows VM to open the *VirtualMachine details* page.
. Click *Configuration* -> *Disks*.
. Click the Options menu {kebab} beside the `sysprep` disk and select *Detach*.
. Click *Detach*.
. Rename `C:\Windows\Panther\unattend.xml` to avoid detection by the `sysprep` tool.

. Start the `sysprep` program by running the following command:
+
[source,terminal]
----
%WINDIR%\System32\Sysprep\sysprep.exe /generalize /shutdown /oobe /mode:vm
----
. After the `sysprep` tool completes, the Windows VM shuts down. The disk image of the VM is now available to use as an installation image for Windows VMs.

You can now specialize the VM.
