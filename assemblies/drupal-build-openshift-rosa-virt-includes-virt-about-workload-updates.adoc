// Module included in the following assemblies:
//
// * virt/updating/upgrading-virt.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-workload-updates_{context}"]
= About workload updates

When you update {VirtProductName}, virtual machine workloads, including `libvirt`, `virt-launcher`, and `qemu`, update automatically if they support live migration.

[NOTE]
====
Each virtual machine has a `virt-launcher` pod that runs the virtual machine
instance (VMI). The `virt-launcher` pod runs an instance of `libvirt`, which is
used to manage the virtual machine (VM) process.
====

You can configure how workloads are updated by editing the `spec.workloadUpdateStrategy` stanza of the `HyperConverged` custom resource (CR). There are two available workload update methods: `LiveMigrate` and `Evict`.

Because the `Evict` method shuts down VMI pods, only the `LiveMigrate` update strategy is enabled by default.

When `LiveMigrate` is the only update strategy enabled:

* VMIs that support live migration are migrated during the update process. The VM guest moves into a new pod with the updated components enabled.

* VMIs that do not support live migration are not disrupted or updated.

** If a VMI has the `LiveMigrate` eviction strategy but does not support live migration, it is not updated.

If you enable both `LiveMigrate` and `Evict`:

* VMIs that support live migration use the `LiveMigrate` update strategy.

* VMIs that do not support live migration use the `Evict` update strategy. If a VMI is controlled by a `VirtualMachine` object that has `runStrategy: Always` set, a new VMI is created in a new pod with updated components.

[discrete]
[id="migration-attempts-timeouts_{context}"]
== Migration attempts and timeouts

When updating workloads, live migration fails if a pod is in the `Pending` state for the following periods:

5 minutes:: If the pod is pending because it is `Unschedulable`.

15 minutes:: If the pod is stuck in the pending state for any reason.

When a VMI fails to migrate, the `virt-controller` tries to migrate it again. It repeats this process until all migratable VMIs are running on new `virt-launcher` pods. If a VMI is improperly configured, however, these attempts can repeat indefinitely.

[NOTE]
====
Each attempt corresponds to a migration object. Only the five most recent attempts are held in a buffer. This prevents migration objects from accumulating on the system while retaining information for debugging.
====



