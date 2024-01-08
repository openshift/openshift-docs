// Module included in the following assemblies:
//
// * virt/virtual_machines/virtual_disks/virt-hot-plugging-virtual-disks.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-hot-plugging-disks-ui_{context}"]
= Hot plugging and hot unplugging a disk by using the web console

You can hot plug a disk by attaching it to a virtual machine (VM) while the VM is running by using the {product-title} web console.

The hot plugged disk remains attached to the VM until you unplug it.

You can make a hot plugged disk persistent so that it is permanently mounted on the VM.

.Prerequisites

* You must have a data volume or persistent volume claim (PVC) available for hot plugging.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select a running VM to view its details.
. On the *VirtualMachine details* page, click *Configuration* -> *Disks*.

. Add a hot plugged disk:
.. Click *Add disk*.
.. In the *Add disk (hot plugged)* window, select the disk from the *Source* list and click *Save*.

. Optional: Unplug a hot plugged disk:
.. Click the options menu {kebab} beside the disk and select *Detach*.
.. Click *Detach*.

. Optional: Make a hot plugged disk persistent:
.. Click the options menu {kebab} beside the disk and select *Make persistent*.
.. Reboot the VM to apply the change.
