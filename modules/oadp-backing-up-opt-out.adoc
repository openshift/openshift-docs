// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/advanced-topics.adoc

[id="oadp-backing-up-opt-out_{context}"]
:_mod-docs-content-type: PROCEDURE
= Backing up pod volumes by using the opt-out method

When using the opt-out approach, all pod volumes are backed up by using File System Backup (FSB), although there are some exceptions:

* Volumes that mount the default service account token, secrets, and configuration maps.

* `hostPath` volumes

You can use the opt-out method to specify which volumes *not* to back up. You can do this by using the `backup.velero.io/backup-volumes-excludes` command.

.Procedure

* On each pod that contains one or more volumes that you do not want to back up, run the following command:
+
[source,terminal]
----
$ oc -n <your_pod_namespace> annotate pod/<your_pod_name> \
  backup.velero.io/backup-volumes-excludes=<your_volume_name_1>, \ <your_volume_name_2>>,...,<your_volume_name_n>
----
+
where:

`<your_volume_name_x>`:: specifies the name of the xth volume in the pod specification.

[NOTE]
====
You can enable this behavior for all Velero backups by running the `velero install` command with the `--default-volumes-to-fs-backup` flag.
====
