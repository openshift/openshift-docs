// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-default-pod-network.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-jumbo-frames-vm-pod-nw_{context}"]
= About jumbo frames support

When using the OVN-Kubernetes CNI plugin, you can send unfragmented jumbo frame packets between two virtual machines (VMs) that are connected on the default pod network. Jumbo frames have a maximum transmission unit (MTU) value greater than 1500 bytes.

The VM automatically gets the MTU value of the cluster network, set by the cluster administrator, in one of the following ways:

* `libvirt`: If the guest OS has the latest version of the VirtIO driver that can interpret incoming data via a Peripheral Component Interconnect (PCI) config register in the emulated device.

* DHCP: If the guest DHCP client can read the MTU value from the DHCP server response.

[NOTE]
====
For Windows VMs that do not have a VirtIO driver, you must set the MTU manually by using `netsh` or a similar tool. This is because the Windows DHCP client does not read the MTU value.
====