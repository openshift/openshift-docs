// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="oadp-operator-issues_{context}"]
= OADP Operator issues

The {oadp-first} Operator might encounter issues caused by problems it is not able to resolve.

[id="oadp-operator-fails-silently_{context}"]
== OADP Operator fails silently

The S3 buckets of an OADP Operator might be empty, but when you run the command `oc get po -n <OADP_Operator_namespace>`, you see that the Operator has a status of `Running`.  In such a case, the Operator is said to have _failed silently_ because it incorrectly reports that it is running.

.Cause

The problem is caused when cloud credentials provide insufficient permissions.

.Solution

Retrieve a list of backup storage locations (BSLs) and check the manifest of each BSL for credential issues.

.Procedure

. Run one of the following commands to retrieve a list of BSLs:

.. Using the OpenShift CLI:
+
[source,terminal]
----
$ oc get backupstoragelocation -A
----

.. Using the Velero CLI:
+
[source,terminal]
----
$ velero backup-location get -n <OADP_Operator_namespace>
----

. Using the list of BSLs, run the following command to display the manifest of each BSL, and examine each manifest for an error.
+
[source,terminal]
----
$ oc get backupstoragelocation -n <namespace> -o yaml
----

.Example result

[source, yaml]
----
apiVersion: v1
items:
- apiVersion: velero.io/v1
  kind: BackupStorageLocation
  metadata:
    creationTimestamp: "2023-11-03T19:49:04Z"
    generation: 9703
    name: example-dpa-1
    namespace: openshift-adp-operator
    ownerReferences:
    - apiVersion: oadp.openshift.io/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: DataProtectionApplication
      name: example-dpa
      uid: 0beeeaff-0287-4f32-bcb1-2e3c921b6e82
    resourceVersion: "24273698"
    uid: ba37cd15-cf17-4f7d-bf03-8af8655cea83
  spec:
    config:
      enableSharedConfig: "true"
      region: us-west-2
    credential:
      key: credentials
      name: cloud-credentials
    default: true
    objectStorage:
      bucket: example-oadp-operator
      prefix: example
    provider: aws
  status:
    lastValidationTime: "2023-11-10T22:06:46Z"
    message: "BackupStorageLocation \"example-dpa-1\" is unavailable: rpc
      error: code = Unknown desc = WebIdentityErr: failed to retrieve credentials\ncaused
      by: AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity\n\tstatus
      code: 403, request id: d3f2e099-70a0-467b-997e-ff62345e3b54"
    phase: Unavailable
kind: List
metadata:
  resourceVersion: ""
----
