// Module included in the following assemblies:
//
// * backup_and_restore/oadp-release-notes-1-3.adoc

:_mod-docs-content-type: PROCEDURE

[id="oadp-upgrade-from-oadp-data-mover-1-2-0_{context}"]
= Upgrading from OADP 1.2 Technology Preview Data Mover

{oadp-first} 1.2 Data Mover backups *cannot* be restored with OADP 1.3. To prevent a gap in the data protection of your applications, complete the following steps before upgrading to OADP 1.3:

.Procedure

. If your cluster backups are sufficient and Container Storage Interface (CSI) storage is available,
back up the applications with a CSI backup.
. If you require off cluster backups:
.. Back up the applications with a file system backup that uses the `--default-volumes-to-fs-backup=true or backup.spec.defaultVolumesToFsBackup` options.
.. Back up the applications with your object storage plugins, for example, `velero-plugin-for-aws`.

[NOTE]
====
To restore OADP 1.2 Data Mover backup, you must uninstall OADP, and install and configure OADP 1.2.
====
