// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/advanced-migration-options-3-4.adoc
// * migration_toolkit_for_containers/advanced-migration-options-mtc.adoc

:_mod-docs-content-type: PROCEDURE
[id="migration-enabling-pv-resizing-dvm_{context}"]
= Enabling persistent volume resizing for direct volume migration

You can enable persistent volume (PV) resizing for direct volume migration to avoid running out of disk space on the destination cluster.

When the disk usage of a PV reaches a configured level, the `MigrationController` custom resource (CR) compares the requested storage capacity of a persistent volume claim (PVC) to its actual provisioned capacity. Then, it calculates the space required on the destination cluster.

A `pv_resizing_threshold` parameter determines when PV resizing is used. The default threshold is `3%`. This means that PV resizing occurs when the disk usage of a PV is more than `97%`. You can increase this threshold so that PV resizing occurs at a lower disk usage level.

PVC capacity is calculated according to the following criteria:

* If the requested storage capacity (`spec.resources.requests.storage`) of the PVC is not equal to its actual provisioned capacity (`status.capacity.storage`), the greater value is used.
* If a PV is provisioned through a PVC and then subsequently changed so that its PV and PVC capacities no longer match, the greater value is used.

.Prerequisites

* The PVCs must be attached to one or more running pods so that the `MigrationController` CR can execute commands.

.Procedure

. Log in to the host cluster.
. Enable PV resizing by patching the `MigrationController` CR:
+
[source,terminal]
----
$ oc patch migrationcontroller migration-controller -p '{"spec":{"enable_dvm_pv_resizing":true}}' \ <1>
  --type='merge' -n openshift-migration
----
<1> Set the value to `false` to disable PV resizing.

. Optional: Update the `pv_resizing_threshold` parameter to increase the threshold:
+
[source,terminal]
----
$ oc patch migrationcontroller migration-controller -p '{"spec":{"pv_resizing_threshold":41}}' \ <1>
  --type='merge' -n openshift-migration
----
<1> The default value is `3`.
+
When the threshold is exceeded, the following status message is displayed in the `MigPlan` CR status:
+
[source,yaml]
----
status:
  conditions:
...
  - category: Warn
    durable: true
    lastTransitionTime: "2021-06-17T08:57:01Z"
    message: 'Capacity of the following volumes will be automatically adjusted to avoid disk capacity issues in the target cluster:  [pvc-b800eb7b-cf3b-11eb-a3f7-0eae3e0555f3]'
    reason: Done
    status: "False"
    type: PvCapacityAdjustmentRequired
----
+
[NOTE]
====
For AWS gp2 storage, this message does not appear unless the `pv_resizing_threshold` is 42% or greater because of the way gp2 calculates volume usage and size. (link:https://bugzilla.redhat.com/show_bug.cgi?id=1973148[*BZ#1973148*])
====
