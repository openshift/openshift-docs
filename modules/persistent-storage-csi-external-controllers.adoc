// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent_storage-csi.adoc
// * microshift_storage/container_storage_interface_microshift/microshift-persistent-storage-csi.adoc


[id="external-csi-contollers_{context}"]
= External CSI controllers

External CSI controllers is a deployment that deploys one or more pods
with five containers:

* The snapshotter container watches `VolumeSnapshot` and `VolumeSnapshotContent` objects and is responsible for the creation and deletion of `VolumeSnapshotContent` object.
* The resizer container is a sidecar container that watches for `PersistentVolumeClaim` updates and triggers `ControllerExpandVolume` operations against a CSI endpoint if you request more storage on `PersistentVolumeClaim` object.
* An external CSI attacher container translates `attach` and `detach`
calls from {product-title} to respective `ControllerPublish` and
`ControllerUnpublish` calls to the CSI driver.
* An external CSI provisioner container that translates `provision` and
`delete` calls from {product-title} to respective `CreateVolume` and
`DeleteVolume` calls to the CSI driver.
* A CSI driver container.

The CSI attacher and CSI provisioner containers communicate with the CSI
driver container using UNIX Domain Sockets, ensuring that no CSI
communication leaves the pod. The CSI driver is not accessible from
outside of the pod.

[NOTE]
====
The `attach`, `detach`, `provision`, and `delete` operations typically require
the CSI driver to use credentials to the storage backend. Run the CSI
controller pods on infrastructure nodes so the credentials are never leaked
to user processes, even in the event of a catastrophic security breach
on a compute node.
====

[NOTE]
====
The external attacher must also run for CSI drivers that do not support
third-party `attach` or `detach` operations. The external attacher will
not issue any `ControllerPublish` or `ControllerUnpublish` operations to
the CSI driver. However, it still must run to implement the necessary
{product-title} attachment API.
====
