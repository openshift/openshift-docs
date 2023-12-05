// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-local.adoc

:_mod-docs-content-type: PROCEDURE
[id="create-local-pvc_{context}"]
= Creating the local volume persistent volume claim

Local volumes must be statically created as a persistent volume claim (PVC)
to be accessed by the pod.

.Prerequisites

* Persistent volumes have been created using the local volume provisioner.

.Procedure

. Create the PVC using the corresponding storage class:
+
[source,yaml]
----
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: local-pvc-name <1>
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem <2>
  resources:
    requests:
      storage: 100Gi <3>
  storageClassName: local-sc <4>
----
<1> Name of the PVC.
<2> The type of the PVC. Defaults to `Filesystem`.
<3> The amount of storage available to the PVC.
<4> Name of the storage class required by the claim.

. Create the PVC in the {product-title} cluster, specifying the file
you just created:
+
[source,terminal]
----
$ oc create -f <local-pvc>.yaml
----
