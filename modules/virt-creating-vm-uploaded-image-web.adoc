// Module included in the following assemblies:
//
// * virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-vm-uploaded-image-web_{context}"]
= Creating a VM from an uploaded image by using the web console

You can create a virtual machine (VM) from an uploaded operating system image by using the {product-title} web console.

.Prerequisites

* You must have an `IMG`, `ISO`, or `QCOW2` image file.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click a template tile without an available boot source.
. Click *Customize VirtualMachine*.
. On the *Customize template parameters* page, expand *Storage* and select *Upload (Upload a new file to a PVC)* from the *Disk source* list.
. Browse to the image on your local machine and set the disk size.
. Click *Customize VirtualMachine*.
. Click *Create VirtualMachine*.