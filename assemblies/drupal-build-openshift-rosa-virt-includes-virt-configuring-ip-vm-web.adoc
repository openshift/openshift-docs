// Module included in the following assemblies:
//
// * virt/vm_networking/virt-configuring-viewing-ips-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-ip-vm-web_{context}"]
= Configuring a static IP address when creating a virtual machine by using the web console

You can configure a static IP address when you create a virtual machine (VM) by using the web console. The IP address is provisioned with cloud-init.

[NOTE]
====
If the VM is connected to the pod network, the pod network interface is the default route unless you update it.
====

.Prerequisites

* The virtual machine is connected to a secondary network.

.Procedure

. Navigate to *Virtualization* -> *Catalog* in the web console.
. Click a template tile.
. Click *Customize VirtualMachine*.
. Click *Next*.
. On the *Scripts* tab, click the edit icon beside *Cloud-init*.
. Select the *Add network data* checkbox.
. Enter the ethernet name, one or more IP addresses separated by commas, and the gateway address.
. Click *Apply*.
. Click *Create VirtualMachine*.