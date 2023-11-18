:_mod-docs-content-type: ASSEMBLY
[id="virt-creating-vms-from-custom-images-overview"]
= Creating virtual machines from custom images overview
include::_attributes/common-attributes.adoc[]
:context: virt-creating-vms-from-custom-images-overview

toc::[]

You can create virtual machines (VMs) from custom operating system images by using one of the following methods:

* xref:../../../virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-container-disks.adoc#virt-creating-vms-from-container-disks[Importing the image as a container disk from a registry].
+
Optional: You can enable auto updates for your container disks. See xref:../../../virt/storage/virt-automatic-bootsource-updates.adoc#virt-automatic-bootsource-updates[Managing automatic boot source updates] for details.

* xref:../../../virt/virtual_machines/creating_vms_custom/virt-creating-vms-from-web-images.adoc#virt-creating-vms-from-web-images[Importing the image from a web page].
* xref:../../../virt/virtual_machines/creating_vms_custom/virt-creating-vms-uploading-images.adoc#virt-creating-vms-uploading-images[Uploading the image from a local machine].
* xref:../../../virt/virtual_machines/creating_vms_custom/virt-creating-vms-by-cloning-pvcs.adoc#virt-creating-vms-by-cloning-pvcs[Cloning a persistent volume claim (PVC) that contains the image].

The Containerized Data Importer (CDI) imports the image into a PVC by using a data volume. You add the PVC to the VM by using the {product-title} web console or command line.

[IMPORTANT]
====
You must install the xref:../../../virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc#virt-installing-qemu-guest-agent[QEMU guest agent] on VMs created from operating system images that are not provided by Red Hat.

You must also install xref:../../../virt/virtual_machines/creating_vms_custom/virt-installing-qemu-guest-agent.adoc#installing-virtio-drivers[VirtIO drivers] on Windows VMs.

The QEMU guest agent is included with Red Hat images.
====
