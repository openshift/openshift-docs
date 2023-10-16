// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-manila.adoc

[id="persistent-storage-manila-usage_{context}"]
= Provisioning an {rh-openstack} Manila persistent volume

{rh-openstack-first} Manila shares are dynamically provisioned as needed. When the
PersistentVolumeClaim is deleted the provisioner will automatically 
delete and unexport the {rh-openstack} Manila share.

.Prerequisites

* The {rh-openstack} Manila external provisioner must be installed.

.Procedure

* Create a PersistentVolumeClaim using the corresponding
StorageClass.
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: manila-nfs-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2G
  storageClassName: manila-share
----
