:_mod-docs-content-type: ASSEMBLY
[id="virt-installing-qemu-guest-agent"]
= Installing the QEMU guest agent and VirtIO drivers
include::_attributes/common-attributes.adoc[]
:context: virt-installing-qemu-guest-agent

toc::[]

The QEMU guest agent is a daemon that runs on the virtual machine (VM) and passes information to the host about the VM, users, file systems, and secondary networks.

You must install the QEMU guest agent on VMs created from operating system images that are not provided by Red Hat.

[id="installing-qemu-guest-agent"]
== Installing the QEMU guest agent

include::modules/virt-installing-qemu-guest-agent-on-linux-vm.adoc[leveloffset=+2]

include::modules/virt-installing-qemu-guest-agent-on-windows-vm.adoc[leveloffset=+2]

[id="installing-virtio-drivers"]
== Installing VirtIO drivers on Windows VMs

VirtIO drivers are paravirtualized device drivers required for Microsoft Windows virtual machines (VMs) to run in {VirtProductName}. The drivers are shipped with the rest of the images and do not require a separate download.

The `container-native-virtualization/virtio-win` container disk must be attached to the VM as a SATA CD drive to enable driver installation. You can install VirtIO drivers during Windows installation or added to an existing Windows installation.

After the drivers are installed, the `container-native-virtualization/virtio-win` container disk can be removed from the VM.

.Supported drivers
[options="header"]
|===
|Driver name |Hardware ID |Description

|*viostor*
|VEN_1AF4&DEV_1001 +
VEN_1AF4&DEV_1042
|The block driver. Sometimes labeled as an *SCSI Controller* in the *Other devices* group.

|*viorng*
|VEN_1AF4&DEV_1005 +
VEN_1AF4&DEV_1044
|The entropy source driver. Sometimes labeled as a *PCI Device* in the *Other devices* group.

|*NetKVM*
|VEN_1AF4&DEV_1000 +
VEN_1AF4&DEV_1041
|The network driver. Sometimes labeled as an *Ethernet Controller* in the *Other devices* group. Available only if a VirtIO NIC is configured.
|===

include::modules/virt-attaching-virtio-disk-to-windows.adoc[leveloffset=+2]

include::modules/virt-attaching-virtio-disk-to-windows-existing.adoc[leveloffset=+2]

include::modules/virt-installing-virtio-drivers-installing-windows.adoc[leveloffset=+2]

include::modules/virt-installing-virtio-drivers-existing-windows.adoc[leveloffset=+2]

include::modules/virt-adding-container-disk-as-cd.adoc[leveloffset=+2]

[id="updating-virtio-drivers"]
== Updating VirtIO drivers

include::modules/virt-updating-virtio-drivers-windows.adoc[leveloffset=+2]
