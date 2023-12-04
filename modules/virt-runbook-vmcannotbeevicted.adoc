// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-VMCannotBeEvicted"]
= VMCannotBeEvicted

[discrete]
[id="meaning-vmcannotbeevicted"]
== Meaning

This alert fires when the eviction strategy of a virtual machine (VM) is set
to `LiveMigration` but the VM is not migratable.

[discrete]
[id="impact-vmcannotbeevicted"]
== Impact

Non-migratable VMs prevent node eviction. This condition affects operations
such as node drain and updates.

[discrete]
[id="diagnosis-vmcannotbeevicted"]
== Diagnosis

. Check the VMI configuration to determine whether the value of
`evictionStrategy` is `LiveMigrate`:
+
[source,terminal]
----
$ oc get vmis -o yaml
----

. Check for a `False` status in the `LIVE-MIGRATABLE` column to identify VMIs
that are not migratable:
+
[source,terminal]
----
$ oc get vmis -o wide
----

. Obtain the details of the VMI and check `spec.conditions` to identify the
issue:
+
[source,terminal]
----
$ oc get vmi <vmi> -o yaml
----
+
.Example output
+
[source,yaml]
----
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: null
    message: cannot migrate VMI which does not use masquerade to connect
    to the pod network
    reason: InterfaceNotLiveMigratable
    status: "False"
    type: LiveMigratable
----

[discrete]
[id="mitigation-vmcannotbeevicted"]
== Mitigation

Set the `evictionStrategy` of the VMI to `shutdown` or resolve the issue that
prevents the VMI from migrating.
