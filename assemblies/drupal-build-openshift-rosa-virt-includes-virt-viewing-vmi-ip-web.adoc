// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-viewing-vmi-ip-web_{context}"]
= Viewing the IP address of a virtual machine by using the web console

You can view the IP address of a virtual machine (VM) by using the {product-title} web console.

[NOTE]
====
You must install the QEMU guest agent on a VM to view the IP address of a secondary network interface. A pod network interface does not require the QEMU guest agent.
====

.Procedure

. In the {product-title} console, click *Virtualization* -> *VirtualMachines* from the side menu.
. Select a VM to open the *VirtualMachine details* page.
. Click the *Details* tab to view the IP address.
