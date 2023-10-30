// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-aws.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-azure.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-gcp.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-mcg.adoc
// * backup_and_restore/application_backup_and_restore/installing/installing-oadp-ocs.adoc

:_mod-docs-content-type: PROCEDURE
[id="oadp-creating-default-secret_{context}"]
= Creating a default Secret

You create a default `Secret` if your backup and snapshot locations use the same credentials or if you do not require a snapshot location.

ifdef::installing-oadp-aws,installing-oadp-azure,installing-oadp-gcp,installing-oadp-mcg[]
The default name of the `Secret` is `{credentials}`.
endif::[]
ifdef::installing-oadp-ocs[]
The default name of the `Secret` is `{credentials}`, unless your backup storage provider has a default plugin, such as `aws`, `azure`, or `gcp`. In that case, the default name is specified in the provider-specific OADP installation procedure.
endif::[]

[NOTE]
====
The `DataProtectionApplication` custom resource (CR) requires a default `Secret`.  Otherwise, the installation will fail. If the name of the backup location `Secret` is not specified, the default name is used.

If you do not want to use the backup location credentials during the installation, you can create a `Secret` with the default name by using an empty `credentials-velero` file.
====

.Prerequisites

* Your object storage and cloud storage, if any, must use the same credentials.
* You must configure object storage for Velero.
* You must create a `credentials-velero` file for the object storage in the appropriate format.

.Procedure

* Create a `Secret` with the default name:
+
[source,terminal,subs="attributes+"]
----
$ oc create secret generic {credentials} -n openshift-adp --from-file cloud=credentials-velero
----

The `Secret` is referenced in the `spec.backupLocations.credential` block of the `DataProtectionApplication` CR when you install the Data Protection Application.
