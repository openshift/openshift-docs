// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/backing_up_and_restoring/backing-up-applications.adoc

:_mod-docs-content-type: PROCEDURE
[id="oadp-backing-up-applications-restic_{context}"]
= Backing up applications with Restic

You back up Kubernetes resources, internal images, and persistent volumes with Restic by editing the `Backup` custom resource (CR).

You do not need to specify a snapshot location in the `DataProtectionApplication` CR.

[IMPORTANT]
====
Restic does not support backing up `hostPath` volumes. For more information, see link:https://{velero-domain}/docs/v{velero-version}/restic/#limitations[additional Restic limitations].
====

.Prerequisites

* You must install the OpenShift API for Data Protection (OADP) Operator.
* You must not disable the default Restic installation by setting `spec.configuration.restic.enable` to `false` in the `DataProtectionApplication` CR.
* The `DataProtectionApplication` CR must be in a `Ready` state.

.Procedure

* Edit the `Backup` CR, as in the following example:
+
[source,yaml]
----
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup>
  labels:
    velero.io/storage-location: default
  namespace: openshift-adp
spec:
  defaultVolumesToFsBackup: true <1>
...
----
<1> In OADP version 1.2 and later, add the `defaultVolumesToFsBackup: true` setting within the `spec` block. In OADP version 1.1, add `defaultVolumesToRestic: true`.