// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-azure-file.adoc

:_mod-docs-content-type: PROCEDURE
[id="create-azure-file-secret_{context}"]
= Create the Azure File share persistent volume claim

To create the persistent volume claim, you must first define a `Secret` object that contains the Azure account and key. This secret is used in the `PersistentVolume` definition, and will be referenced by the persistent volume claim for use in applications.

.Prerequisites

* An Azure File share exists.
* The credentials to access this share, specifically the storage account and
key, are available.

.Procedure

. Create a `Secret` object that contains the Azure File credentials:
+
[source,terminal]
----
$ oc create secret generic <secret-name> --from-literal=azurestorageaccountname=<storage-account> \ <1>
  --from-literal=azurestorageaccountkey=<storage-account-key> <2>
----
<1> The Azure File storage account name.
<2> The Azure File storage account key.

. Create a `PersistentVolume` object that references the `Secret` object you created:
+
[source,yaml]
----
apiVersion: "v1"
kind: "PersistentVolume"
metadata:
  name: "pv0001" <1>
spec:
  capacity:
    storage: "5Gi" <2>
  accessModes:
    - "ReadWriteOnce"
  storageClassName: azure-file-sc
  azureFile:
    secretName: <secret-name> <3>
    shareName: share-1 <4>
    readOnly: false
----
<1> The name of the persistent volume.
<2> The size of this persistent volume.
<3> The name of the secret that contains the Azure File share credentials.
<4> The name of the Azure File share.

. Create a `PersistentVolumeClaim` object that maps to the persistent volume you created:
+
[source,yaml]
----
apiVersion: "v1"
kind: "PersistentVolumeClaim"
metadata:
  name: "claim1" <1>
spec:
  accessModes:
    - "ReadWriteOnce"
  resources:
    requests:
      storage: "5Gi" <2>
  storageClassName: azure-file-sc <3>
  volumeName: "pv0001" <4>
----
<1> The name of the persistent volume claim.
<2> The size of this persistent volume claim.
<3> The name of the storage class that is used to provision the persistent volume.
Specify the storage class used in the `PersistentVolume` definition.
<4> The name of the existing `PersistentVolume` object that references the
Azure File share.
