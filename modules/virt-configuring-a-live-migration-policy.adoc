// Module included in the following assemblies:
//
// * virt/live_migration/virt-configuring-live-migration.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-configuring-a-live-migration-policy_{context}"]
= Creating a live migration policy by using the command line

You can create a live migration policy by using the command line. A live migration policy is applied to selected virtual machines (VMs) by using any combination of labels:

* VM labels such as `size`, `os`, or `gpu`
* Project labels such as `priority`, `bandwidth`, or `hpc-workload`

For the policy to apply to a specific group of VMs, all labels on the group of VMs must match the labels of the policy.

[NOTE]
====
If multiple live migration policies apply to a VM, the policy with the greatest number of matching labels takes precedence.

If multiple policies meet this criteria, the policies are sorted by alphabetical order of the matching label keys, and the first one in that order takes precedence.
====

.Procedure

. Create a `MigrationPolicy` object as in the following example:
+
[source,yaml]
----
apiVersion: migrations.kubevirt.io/v1alpha1
kind: MigrationPolicy
metadata:
  name: <migration_policy>
spec:
  selectors:
    namespaceSelector: <1>
      hpc-workloads: "True"
      xyz-workloads-type: ""
    virtualMachineInstanceSelector: <2>
      workload-type: "db"
      operating-system: ""
----
<1> Specify project labels.
<2> Specify VM labels.

. Create the migration policy by running the following command:
+
[source,terminal]
----
$ oc create migrationpolicy -f <migration_policy>.yaml
----