// This module is included in the following assemblies:
//
// storage/persistent_storage/persistent_storage_local/persistent-storage-using-lvms.adoc

:_mod-docs-content-type: PROCEDURE
[id="adding-a-storage-class_{context}"]
= Adding a storage class

You can add a storage class to an {product-title} cluster. A storage class describes a class of storage in the cluster and how the cluster dynamically provisions the persistent volumes (PVs) when the user specifies the storage class. A storage class describes the type of device classes, the quality-of-service level, the filesystem type, and other details.

.Procedure

. Create a YAML file:
+
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: lvm-storageclass
parameters:
  csi.storage.k8s.io/fstype: ext4
  topolvm.io/device-class: vg1
provisioner: topolvm.io
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
----
+
Save the file by using a name similar to the storage class name. For example, `lvm-storageclass.yaml`.

. Apply the YAML file by using the `oc` command:
+
[source,terminal]
----
$ oc apply -f <file_name> <1>
----
<1> Replace `<file_name>` with the name of the YAML file. For example, `lvm-storageclass.yaml`.
+
The cluster will create the storage class.

. Verify that the cluster created the storage class by using the following command:
+
[source,terminal]
----
$ oc get storageclass <name> <1>
----
<1> Replace `<name>` with the name of the storage class. For example, `lvm-storageclass`.
+
.Example output
[source,terminal,options="nowrap",role="white-space-pre"]
----
NAME              PROVISIONER  RECLAIMPOLICY  VOLUMEBINDINGMODE     ALLOWVOLUMEEXPANSION  AGE
lvm-storageclass  topolvm.io   Delete         WaitForFirstConsumer  true                  1s
----
