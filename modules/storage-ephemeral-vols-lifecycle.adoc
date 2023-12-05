// Module included in the following assemblies:
//
// * storage/generic-ephemeral-vols.adoc
//* microshift_storage/generic-ephemeral-volumes-microshift.adoc


:_mod-docs-content-type: CONCEPT
[id="generic-ephemeral-vols-lifecycle_{context}"]
= Lifecycle and persistent volume claims

The parameters for a volume claim are allowed inside a volume source of a pod. Labels, annotations, and the whole set of fields for persistent volume claims (PVCs) are supported. When such a pod is created, the ephemeral volume controller then creates an actual PVC object (from the template shown in the _Creating generic ephemeral volumes_ procedure) in the same namespace as the pod, and ensures that the PVC is deleted when the pod is deleted. This triggers volume binding and provisioning in one of two ways:


* Either immediately, if the storage class uses immediate volume binding.
+
With immediate binding, the scheduler is forced to select a node that has access to the volume after it is available.

* When the pod is tentatively scheduled onto a node (`WaitForFirstConsumervolume` binding mode).
+
This volume binding option is recommended for generic ephemeral volumes because then the scheduler can choose a suitable node for the pod.

In terms of resource ownership, a pod that has generic ephemeral storage is the owner of the PVCs that provide that ephemeral storage. When the pod is deleted, the Kubernetes garbage collector deletes the PVC, which then usually triggers deletion of the volume because the default reclaim policy of storage classes is to delete volumes. You can create quasi-ephemeral local storage by using a storage class with a reclaim policy of retain: the storage outlives the pod, and in this case, you must ensure that volume clean-up happens separately. While these PVCs exist, they can be used like any other PVC. In particular, they can be referenced as data source in volume cloning or snapshotting. The PVC object also holds the current status of the volume.
