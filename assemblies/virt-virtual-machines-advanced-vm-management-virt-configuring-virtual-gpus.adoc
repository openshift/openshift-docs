:_mod-docs-content-type: ASSEMBLY
[id="virt-configuring-virtual-gpus"]
= Configuring virtual GPUs
include::_attributes/common-attributes.adoc[]
:context: virt-configuring-virtual-gpus

toc::[]

If you have graphics processing unit (GPU) cards, {VirtProductName} can automatically create virtual GPUs (vGPUs) that you can assign to virtual machines (VMs).

include::modules/virt-about-using-virtual-gpus.adoc[leveloffset=+1]

[id="preparing-hosts-mdevs_{context}"]
== Preparing hosts for mediated devices

You must enable the Input-Output Memory Management Unit (IOMMU) driver before you can configure mediated devices.

include::modules/virt-adding-kernel-arguments-enable-iommu.adoc[leveloffset=+2]

[id="configuring-nvidia-gpu-operator_{context}"]
== Configuring the NVIDIA GPU Operator

You can use the NVIDIA GPU Operator to provision worker nodes for running GPU-accelerated virtual machines (VMs) in {VirtProductName}.

[NOTE]
====
The NVIDIA GPU Operator is supported only by NVIDIA. For more information, see link:https://access.redhat.com/solutions/5174941[Obtaining Support from NVIDIA] in the Red Hat Knowledgebase.
====

include::modules/about-using-gpu-operator.adoc[leveloffset=+2]

include::modules/virt-options-configuring-mdevs.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* xref:../../../virt/virtual_machines/advanced_vm_management/virt-configuring-pci-passthrough.adoc#virt-configuring-pci-passthrough[Configuring PCI passthrough]

include::modules/virt-how-virtual-gpus-assigned-nodes.adoc[leveloffset=+1]

[id="managing-mediated-devices_{context}"]
== Managing mediated devices

Before you can assign mediated devices to virtual machines, you must create the devices and expose them to the cluster. You can also reconfigure and remove mediated devices.

include::modules/virt-creating-and-exposing-mediated-devices.adoc[leveloffset=+2]

include::modules/virt-about-changing-removing-mediated-devices.adoc[leveloffset=+2]

include::modules/virt-removing-mediated-device-from-cluster-cli.adoc[leveloffset=+2]

[id="using-mediated-devices_{context}"]
== Using mediated devices

You can assign mediated devices to one or more virtual machines.

include::modules/virt-assigning-vgpu-vm-cli.adoc[leveloffset=+2]

include::modules/virt-assigning-vgpu-vm-web.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-troubleshooting-enabling_intel_vt_x_and_amd_v_virtualization_hardware_extensions_in_bios[Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS]