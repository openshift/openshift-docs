// Module included in the following assemblies:
//
// * virt/virt_users_guide/virt-edit-boot-order.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-edit-boot-order-web_{context}"]
= Editing a boot order list in the web console

Edit the boot order list in the web console.

.Procedure

. Click *Virtualization* -> *VirtualMachines* from the side menu.

. Select a virtual machine to open the *VirtualMachine details* page.

. Click the *Details* tab.

. Click the pencil icon that is located on the right side of *Boot Order*.

. Choose the appropriate method to move the item in the boot order list:

* If you do not use a screen reader, hover over the arrow icon next to the item that you want to move, drag the item up or down, and drop it in a location of your choice.

* If you use a screen reader, press the Up Arrow key or Down Arrow key to move the item in the boot order list. Then, press the *Tab* key to drop the item in a location of your choice.

. Click *Save*.

[NOTE]
====
If the virtual machine is running, changes to the boot order list will not take effect until you restart the virtual machine.

You can view pending changes by clicking *View Pending Changes* on the right side of the *Boot Order* field. The *Pending Changes* banner
at the top of the page displays a list of all changes that will be applied when the virtual machine restarts.
====
