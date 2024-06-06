// Module included in the following assembly:
//
// * virt/virtual_machines/virt-manage-vmis.adoc
//

:_mod-docs-content-type: CONCEPT
[id="virt-about-vmis_{context}"]
= About virtual machine instances

A virtual machine instance (VMI) is a representation of a running virtual machine (VM). When a VMI is owned by a VM or by another object, you manage it through its owner in the web console or by using the `oc` command-line interface (CLI).

A standalone VMI is created and started independently with a script, through automation, or by using other methods in the CLI. In your environment, you might have standalone VMIs that were developed and started outside of the {VirtProductName} environment. You can continue to manage those standalone VMIs by using the CLI. You can also use the web console for specific tasks associated with standalone VMIs:

* List standalone VMIs and their details.

* Edit labels and annotations for a standalone VMI.

* Delete a standalone VMI.

When you delete a VM, the associated VMI is automatically deleted. You delete a standalone VMI directly because it is not owned by VMs or other objects.

[NOTE]
====
Before you uninstall {VirtProductName}, list and view the standalone VMIs by using the CLI or the web console. Then, delete any outstanding VMIs.
====
