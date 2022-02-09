// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc

[id="gce-persistentdisk-storage-class_{context}"]
= GCE PersistentDisk (gcePD) object definition

.gce-pd-storageclass.yaml
[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: <storage-class-name> <1>
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard <2>
  replication-type: none
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Delete
----
<1> Name of the storage class. The persistent volume claim uses this storage class for provisioning the associated persistent volumes.
<2> Select either `pd-standard` or `pd-ssd`. The default is `pd-standard`.
