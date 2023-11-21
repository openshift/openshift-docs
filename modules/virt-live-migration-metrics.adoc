// Module included in the following assemblies:
//
// * virt/support/virt-prometheus-queries.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-live-migration-metrics_{context}"]
= Live migration metrics

The following metrics can be queried to show live migration status:

`kubevirt_vmi_migration_data_processed_bytes`:: The amount of guest operating system data that has migrated to the new virtual machine (VM). Type: Gauge.

`kubevirt_vmi_migration_data_remaining_bytes`:: The amount of guest operating system data that remains to be migrated. Type: Gauge.

`kubevirt_vmi_migration_memory_transfer_rate_bytes`:: The rate at which memory is becoming dirty in the guest operating system. Dirty memory is data that has been changed but not yet written to disk. Type: Gauge.

`kubevirt_vmi_migrations_in_pending_phase`:: The number of pending migrations. Type: Gauge.

`kubevirt_vmi_migrations_in_scheduling_phase`:: The number of scheduling migrations. Type: Gauge.

`kubevirt_vmi_migrations_in_running_phase`:: The number of running migrations. Type: Gauge.

`kubevirt_vmi_migration_succeeded`:: The number of successfully completed migrations. Type: Gauge.

`kubevirt_vmi_migration_failed`:: The number of failed migrations. Type: Gauge.
