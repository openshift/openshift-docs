// Module included in the following assemblies:
//
// * virt/live_migration/virt-configuring-live-migration.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-vm-eviction-strategy-cli_{context}"]
= Configuring a VM eviction strategy using the command line

You can configure an eviction strategy for a virtual machine (VM) by using the command line.

[IMPORTANT]
====
The default eviction strategy is `LiveMigrate`. A non-migratable VM with a `LiveMigrate` eviction strategy might prevent nodes from draining or block an infrastructure upgrade because the VM is not evicted from the node. This situation causes a migration to remain in a `Pending` or `Scheduling` state unless you shut down the VM manually.

You must set the eviction strategy of non-migratable VMs to `LiveMigrateIfPossible`, which does not block an upgrade, or to `None`, for VMs that should not be migrated.
====

.Procedure

. Edit the `VirtualMachine` resource by running the following command:
+
[source,terminal]
----
$ oc edit vm <vm_name> -n <namespace>
----
+
.Example eviction strategy
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <vm_name>
spec:
  template:
    spec:
      evictionStrategy: LiveMigrateIfPossible <1>
# ...
----
<1> Specify the eviction strategy. The default value is `LiveMigrate`.

. Restart the VM to apply the changes:
+
[source,terminal]
----
$ virtctl restart <vm_name> -n <namespace>
----
