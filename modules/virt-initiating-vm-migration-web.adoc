// Module included in the following assemblies:
//
// * virt/live_migration/virt-initiating-live-migration.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-initiating-vm-migration-web_{context}"]
= Initiating live migration by using the web console

You can live migrate a running virtual machine (VM) to a different node in the cluster by using the {product-title} web console.

[NOTE]
====
The *Migrate* action is visible to all users but only cluster administrators can initiate a live migration.
====

.Prerequisites

* The VM must be migratable.
* If the VM is configured with a host model CPU, the cluster must have an available node that supports the CPU model.

.Procedure

. Navigate to *Virtualization* -> *VirtualMachines* in the web console.
. Select *Migrate* from the Options menu {kebab} beside a VM.
. Click *Migrate*.
