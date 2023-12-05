// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-aws-efs-csi.adoc
// * storage/container_storage_interface/osd-persistent-storage-aws-efs-csi.adoc

:_mod-docs-content-type: PROCEDURE
[id="storage-create-storage-class-cli_{context}"]
= Creating the {StorageClass} storage class using the CLI

[role="_abstract"]
.Procedure

* Create a `StorageClass` object:
+
[source,yaml]
----
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: efs-sc
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap <1>
  fileSystemId: fs-a5324911 <2>
  directoryPerms: "700" <3>
  gidRangeStart: "1000" <4>
  gidRangeEnd: "2000" <4>
  basePath: "/dynamic_provisioning" <5>
----
<1> `provisioningMode` must be `efs-ap` to enable dynamic provisioning.
<2> `fileSystemId` must be the ID of the EFS volume created manually.
<3> `directoryPerms` is the default permission of the root directory of the volume. In this example, the volume is accessible only by the owner.
<4> `gidRangeStart` and `gidRangeEnd` set the range of POSIX Group IDs (GIDs) that are used to set the GID of the AWS access point. If not specified, the default range is 50000-7000000. Each provisioned volume, and thus AWS access point, is assigned a unique GID from this range.
<5> `basePath` is the directory on the EFS volume that is used to create dynamically provisioned volumes. In this case, a PV is provisioned as “/dynamic_provisioning/<random uuid>” on the EFS volume. Only the subdirectory is mounted to pods that use the PV.
+
[NOTE]
====
A cluster admin can create several `StorageClass` objects, each using a different EFS volume.
====