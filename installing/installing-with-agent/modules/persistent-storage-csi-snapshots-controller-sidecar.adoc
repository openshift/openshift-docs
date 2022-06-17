// Module included in the following assemblies:
//
// * storage/container_storage_interface/persistent-storage-csi-snapshots.adoc

[id="persistent-storage-csi-snapshots-controller-sidecar_{context}"]
= CSI snapshot controller and sidecar

{product-title} provides a snapshot controller that is deployed into the control plane. In addition, your CSI driver vendor provides the CSI snapshot sidecar as a helper container that is installed during the CSI driver installation.

The CSI snapshot controller and sidecar provide volume snapshotting through the {product-title} API. These external components run in the cluster.

The external controller is deployed by the CSI Snapshot Controller Operator.

== External controller
The CSI snapshot controller binds `VolumeSnapshot` and `VolumeSnapshotContent` objects. The controller manages dynamic provisioning by creating and deleting `VolumeSnapshotContent` objects.

== External sidecar
Your CSI driver vendor provides the `csi-external-snapshotter` sidecar. This is a separate helper container that is deployed with the CSI driver. The sidecar manages snapshots by triggering `CreateSnapshot` and `DeleteSnapshot` operations. Follow the installation instructions provided by your vendor.
