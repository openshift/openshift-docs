// Module included in the following assembly:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc
//

:_mod-docs-content-type: PROCEDURE
[id="virt-remove-boot-order-item-web_{context}"]

= Removing items from a boot order list in the web console

Remove items from a boot order list by using the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Details* tab.

. Click the pencil icon that is located on the right side of *Boot Order*.

. Click the *Remove* icon {delete} next to the item. The item is removed from the boot order list and saved in the list of available boot sources. If you remove all items from the boot order list, the following message displays: *No resource selected. VM will attempt to boot from disks by order of appearance in YAML file.*

[NOTE]
====
If the virtual machine is running, changes to *Boot Order* will not take effect until you restart the virtual machine.

You can view pending changes by clicking *View Pending Changes* on the right side of the *Boot Order* field. The *Pending Changes* banner at the top of the page displays a list of all changes that will be applied when the virtual machine restarts.
====
