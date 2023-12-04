:_mod-docs-content-type: ASSEMBLY
[id="virt-hot-plugging-virtual-disks"]
= Hot-plugging VM disks
include::_attributes/common-attributes.adoc[]
:context: virt-hot-plugging-virtual-disks

toc::[]

You can add or remove virtual disks without stopping your virtual machine (VM) or virtual machine instance (VMI).

Only data volumes and persistent volume claims (PVCs) can be hot plugged and hot-unplugged. You cannot hot plug or hot-unplug container disks.

A hot plugged disk remains to the VM even after reboot. You must detach the disk to remove it from the VM.

You can make a hot plugged disk persistent so that it is permanently mounted on the VM.

[NOTE]
====
Each VM has a `virtio-scsi` controller so that hot plugged disks can use the `scsi` bus. The `virtio-scsi` controller overcomes the limitations of `virtio` while retaining its performance advantages. It is highly scalable and supports hot plugging over 4 million disks.

Regular `virtio` is not available for hot plugged disks because it is not scalable. Each `virtio` disk uses one of the limited PCI Express (PCIe) slots in the VM. PCIe slots are also used by other devices and must be reserved in advance. Therefore, slots might not be available on demand.
====

include::modules/virt-hot-plugging-disks-ui.adoc[leveloffset=+1]

include::modules/virt-hot-plugging-disk-cli.adoc[leveloffset=+1]



