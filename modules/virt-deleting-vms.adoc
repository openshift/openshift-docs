// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-delete-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-vms_{context}"]

= Deleting a virtual machine by using the CLI

You can delete a virtual machine by using the `oc` command line interface (CLI). The `oc` client enables you to perform actions on multiple virtual machines.

.Prerequisites

* Identify the name of the virtual machine that you want to delete.

.Procedure

* Delete the virtual machine by running the following command:
+
[source,terminal]
----
$ oc delete vm <vm_name>
----
+
[NOTE]
====
This command only deletes a VM in the current project. Specify the
`-n <project_name>` option if the VM you want to delete is in
a different project or namespace.
====
