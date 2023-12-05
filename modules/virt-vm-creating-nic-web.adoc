// Module included in the following assemblies:
//
// * virt/vm_networking/virt-connecting-vm-to-linux-bridge.adoc
// * virt/virtual_machines/virt-accessing-vm-ssh.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-vm-creating-nic-web_{context}"]
= Configuring a VM network interface by using the web console

You can configure a network interface for a virtual machine (VM) by using the {product-title} web console.

.Prerequisites

* You created a network attachment definition for the network.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines*.
. Click a VM to view the *VirtualMachine details* page.
. On the *Configuration* tab, click the *Network interfaces* tab.
. Click *Add network interface*.
. Enter the interface name and select the network attachment definition from the *Network* list.
. Click *Save*.
. Restart the VM to apply the changes.
