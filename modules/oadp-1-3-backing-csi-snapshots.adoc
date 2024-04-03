// Module included in the following assemblies:
//
// * backup_and_restore/application_backup_and_restore/installing/oadp-backup-restore-csi-snapshots.adoc
:_mod-docs-content-type: PROCEDURE
[id="oadp-1-3-backing-csi-snapshots_{context}"]
= Backing up persistent volumes with CSI snapshots

You can use the OADP Data Mover to back up Container Storage Interface (CSI) volume snapshots to a remote object store.

.Prerequisites

* You have access to the cluster with the `cluster-admin` role.
* You have installed the OADP Operator.
* You have included the CSI plugin and enabled the node agent in the `DataProtectionApplication` custom resource (CR).
* You have an application with persistent volumes running in a separate namespace.
* You have added the `metadata.labels.velero.io/csi-volumesnapshot-class: "true"` key-value pair to the `VolumeSnapshotClass` CR.

.Procedure

. Create a YAML file for the `Backup` object, as in the following example:
+
.Example `Backup` CR
[source,yaml]
----
kind: Backup
apiVersion: velero.io/v1
metadata:
  name: backup
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup: false
  includedNamespaces:
  - mysql-persistent
  itemOperationTimeout: 4h0m0s
  snapshotMoveData: true <1>
  storageLocation: default
  ttl: 720h0m0s
  volumeSnapshotLocations:
  - dpa-sample-1
# ...
----
<1> Set to `true` to enable movement of CSI snapshots to remote object storage.

. Apply the manifest:
+
[source,terminal]
----
$ oc create -f backup.yaml
----
+
A `DataUpload` CR is created after the snapshot creation is complete.

.Verification
* Verify that the snapshot data is successfully transferred to the remote object store by monitoring the `status.phase` field of the `DataUpload` CR.  Possible values are `In Progress`, `Completed`, `Failed`, or `Canceled`. The object store is configured in the `backupLocations` stanza of the `DataProtectionApplication` CR.

** Run the following command to get a list of all `DataUpload` objects:
+
[source,terminal]
----
$ oc get datauploads -A
----
+
.Example output
[source,terminal]
----
NAMESPACE       NAME                  STATUS      STARTED   BYTES DONE   TOTAL BYTES   STORAGE LOCATION   AGE     NODE
openshift-adp   backup-test-1-sw76b   Completed   9m47s     108104082    108104082     dpa-sample-1       9m47s   ip-10-0-150-57.us-west-2.compute.internal
openshift-adp   mongo-block-7dtpf     Completed   14m       1073741824   1073741824    dpa-sample-1       14m     ip-10-0-150-57.us-west-2.compute.internal
----

** Check the value of the `status.phase` field of the specific `DataUpload` object by running the following command:
+
[source,terminal]
----
$ oc get datauploads <dataupload_name> -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: velero.io/v2alpha1
kind: DataUpload
metadata:
  name: backup-test-1-sw76b
  namespace: openshift-adp
spec:
  backupStorageLocation: dpa-sample-1
  csiSnapshot:
    snapshotClass: ""
    storageClass: gp3-csi
    volumeSnapshot: velero-mysql-fq8sl
  operationTimeout: 10m0s
  snapshotType: CSI
  sourceNamespace: mysql-persistent
  sourcePVC: mysql
status:
  completionTimestamp: "2023-11-02T16:57:02Z"
  node: ip-10-0-150-57.us-west-2.compute.internal
  path: /host_pods/15116bac-cc01-4d9b-8ee7-609c3bef6bde/volumes/kubernetes.io~csi/pvc-eead8167-556b-461a-b3ec-441749e291c4/mount
  phase: Completed <1>
  progress:
    bytesDone: 108104082
    totalBytes: 108104082
  snapshotID: 8da1c5febf25225f4577ada2aeb9f899
  startTimestamp: "2023-11-02T16:56:22Z"
----
<1> Indicates that snapshot data is successfully transferred to the remote object store.
