// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-specializing-windows-sysprep_{context}"]
= Specializing a Windows VM image

Specializing a Windows virtual machine (VM) configures the computer-specific information from a generalized Windows image onto the VM.

.Prerequisites

* You must have a generalized Windows disk image.
* You must create an `unattend.xml` answer file. See the link:https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11[Microsoft documentation] for details.

.Procedure

. In the {product-title} console, click *Virtualization* -> *Catalog*.
. Select a Windows template and click *Customize VirtualMachine*.
. Select *PVC (clone PVC)* from the *Disk source* list.
. Select the PVC project and PVC name of the generalized Windows image.
. Click *Customize VirtualMachine parameters*.
. Click the *Scripts* tab.
. In the *Sysprep* section, click *Edit*, browse to the `unattend.xml` answer file, and click *Save*.
. Click *Create VirtualMachine*.

During the initial boot, Windows uses the `unattend.xml` answer file to specialize the VM. The VM is now ready to use.
