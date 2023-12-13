// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-deleting-vmis-cli.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-vmis-cli_{context}"]

= Deleting a standalone virtual machine instance using the CLI

You can delete a standalone virtual machine instance (VMI) by using the `oc` command-line interface (CLI).

.Prerequisites

* Identify the name of the VMI that you want to delete.

.Procedure

* Delete the VMI by running the following command:
+
[source,terminal]
----
$ oc delete vmi <vmi_name>
----