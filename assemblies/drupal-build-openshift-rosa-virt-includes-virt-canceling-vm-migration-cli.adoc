// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-canceling-vm-migration-cli_{context}"]
= Canceling live migration by using the command line

Cancel the live migration of a virtual machine by deleting the
`VirtualMachineInstanceMigration` object associated with the migration.

.Procedure

* Delete the `VirtualMachineInstanceMigration` object that triggered the live
migration, `migration-job` in this example:
+

[source,terminal]
----
$ oc delete vmim migration-job
----
