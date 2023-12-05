// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-aws-efs.adoc
// * storage/container_storage_interface/osd-persistent-storage-aws-efs-csi.adoc

:_mod-docs-content-type: PROCEDURE
[id="csi-dynamic-provisioning-aws-efs_{context}"]
= Dynamic provisioning for Amazon Elastic File Storage

[role="_abstract"]
The link:https://github.com/openshift/aws-efs-csi-driver[AWS EFS CSI driver] supports a different form of dynamic provisioning than other CSI drivers. It provisions new PVs as subdirectories of a pre-existing EFS volume. The PVs are independent of each other. However, they all share the same EFS volume. When the volume is deleted, all PVs provisioned out of it are deleted too.
The EFS CSI driver creates an AWS Access Point for each such subdirectory. Due to AWS AccessPoint limits, you can only dynamically provision 1000 PVs from a single `StorageClass`/EFS volume.

[IMPORTANT]
====
Note that `PVC.spec.resources` is not enforced by EFS.

In the example below, you request 5 GiB of space. However, the created PV is limitless and can store any amount of data (like petabytes). A broken application, or even a rogue application, can cause significant expenses when it stores too much data on the volume.

Using monitoring of EFS volume sizes in AWS is strongly recommended.
====

.Prerequisites

* You have created Amazon Elastic File Storage (Amazon EFS) volumes.
* You have created the AWS EFS storage class.

.Procedure

To enable dynamic provisioning:

* Create a PVC (or StatefulSet or Template) as usual, referring to the `StorageClass` created previously.
+
[source,yaml]
----
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test
spec:
  storageClassName: efs-sc
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
----
