// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-edit-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-add-disk-to-vm_{context}"]

= Adding a disk to a virtual machine

You can add a virtual disk to a virtual machine (VM) by using the {product-title} web console.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a VM to open the *VirtualMachine details* page.

. On the *Disks* tab, click *Add disk*.

. Specify the *Source*, *Name*, *Size*, *Type*, *Interface*, and *Storage Class*.

.. Optional: You can enable preallocation if you use a blank disk source and require maximum write performance when creating data volumes. To do so, select the *Enable preallocation* checkbox.

.. Optional: You can clear *Apply optimized StorageProfile settings* to change the *Volume Mode* and *Access Mode* for the virtual disk. If you do not specify these parameters, the system uses the default values from the `kubevirt-storage-class-defaults` config map.

. Click *Add*.

[NOTE]
====
If the VM is running, you must restart the VM to apply the change.
====

