// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/migrating-applications-3-4.adoc
// * migration_toolkit_for_containers/migrating-applications-with-mtc.adoc

[id="migration-direct-volume-migration-and-direct-image-migration_{context}"]
= Direct volume migration and direct image migration

You can use direct image migration (DIM) and direct volume migration (DVM) to migrate images and data directly from the source cluster to the target cluster.

If you run DVM with nodes that are in different availability zones, the migration might fail because the migrated pods cannot access the persistent volume claim.

DIM and DVM have significant performance benefits because the intermediate steps of backing up files from the source cluster to the replication repository and restoring files from the replication repository to the target cluster are skipped. The data is transferred with link:https://rsync.samba.org/[Rsync].

DIM and DVM have additional prerequisites.
