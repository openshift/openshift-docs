:_mod-docs-content-type: ASSEMBLY
[id="microshift-troubleshoot-backup-restore"]
= Troubleshooting data backup and restore
include::_attributes/attributes-microshift.adoc[]
:context: microshift-troubleshoot-data-backup-and-restore

toc::[]

To troubleshoot failed data backups and restorations, check the basics first, such as data paths, storage configuration, and storage capacity.

[id="troubleshoot-backup-restore-microshift-backup-data-failed_{context}"]
== Backing up data failed
Data backups are automatic on `rpm-ostree` systems. If you are not using an `rpm-ostree` system and attempted to create a manual backup, the following reasons can cause the backup to fail:

* Not waiting several minutes after a system start to successfully stop {microshift-short}. The system must complete health checks and any other background processes before a back up can succeed.
* If {microshift-short} stopped running because of an error, you cannot perform a backup of the data.
** Make sure the system is healthy.
** Stop it in a healthy state before attempting a backup.
* If you do not have sufficient storage for the data, the backup fails. Ensure that you have enough storage for the {microshift-short} data.
* If you do not have sufficient permissions, a backup can fail. Ensure you have the correct user permissions to create a backup and perform the required configurations.

[id="troubleshoot-backup-restore-microshift-backup-logs_{context}"]
== Backup logs
* Logs print to the console during manual backups.
* Logs are automatically generated for `rpm-ostree` system automated backups as part of the {microshift-short} journal logs. You can check the logs by running the following command:
+
[source,terminal]
----
$ sudo journalctl -u microshift
----

[id="troubleshoot-backup-restore-microshift-restore-data-failed_{context}"]
== Restoring data failed
The restoration of data can fail for many reasons, including storage and permission issues. Mismatched data versions can cause failures when {microshift-short} restarts.

[id="troubleshoot-backup-restore-microshift-RPM-OSTree-data-restore-failed_{context}"]
=== RPM-OSTree-based systems data restore failed
Data restorations are automatic on `rpm-ostree` systems, but can fail, for example:

* The only backups that are restored on `rpm-ostree` systems are backups from the current deployment or a rollback deployment. Backups are not taken on an unhealthy system.

** Only the latest backups that have corresponding deployments are retained. Outdated backups that do not have a matching deployment are automatically removed.

** Data is usually not restored from a newer version of {microshift-short}.

** Ensure that the data you are restoring follows same versioning pattern as the update path. For example, if the destination version of {microshift-short} is an older version than the version of the {microshift-short} data you are currently using, the restoration can fail.

[id="troubleshoot-backup-restore-microshift-rpm-manual-restore-data-failed_{context}"]
=== RPM-based manual data restore failed
If you are using an RPM system that is not `rpm-ostree` and tried to restore a manual backup, the following reasons can cause the restoration to fail:

* If {microshift-short} stopped running because of an error, you cannot restore data.
** Make sure the system is healthy.
** Start it in a healthy state before attempting to restore data.

* If you do not have enough storage space allocated for the incoming data, the restoration fails.
** Make sure that your current system storage is configured to accept the restored data.

* You are attempting to restore data from a newer version of {microshift-short}.
** Ensure that the data you are restoring follows same versioning pattern as the update path. For example, if the destination version of {microshift-short} is an older version than the version of the {microshift-short} data you are attempting to use, the restoration can fail.

[id="troubleshoot-backup-restore-microshift-storage-migration-failed_{context}"]
== Storage migration failed
Storage migration failures are typically caused by substantial changes in custom resources (CRs) from one {microshift-short} to the next. If a storage migration fails, there is usually an unresolvable discrepancy between versions that requires manual review.

