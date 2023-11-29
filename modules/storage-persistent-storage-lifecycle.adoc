// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc


[id=lifecycle-volume-claim_{context}]
= Lifecycle of a volume and claim

PVs are resources in the cluster. PVCs are requests for those resources
and also act as claim checks to the resource. The interaction between PVs
and PVCs have the following lifecycle.

[id="provisioning_{context}"]
== Provision storage

In response to requests from a developer defined in a PVC, a cluster
administrator configures one or more dynamic provisioners that provision
storage and a matching PV.

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
Alternatively, a cluster administrator can create a number of PVs in advance
that carry the details of the real storage that is available for use. PVs
exist in the API and are available for use.
endif::[]

[id="binding_{context}"]
== Bind claims

When you create a PVC, you request a specific amount of storage, specify the
required access mode, and create a storage class to describe and classify
the storage. The control loop in the master watches for new PVCs and binds
the new PVC to an appropriate PV. If an appropriate PV does not exist, a
provisioner for the storage class creates one.

The size of all PVs might exceed your PVC size. This is especially true
with manually provisioned PVs. To minimize the excess, {product-title}
binds to the smallest PV that matches all other criteria.

Claims remain unbound indefinitely if a matching volume does not exist or
can not be created with any available provisioner servicing a storage
class. Claims are bound as matching volumes become available. For example,
a cluster with many manually provisioned 50Gi volumes would not match a
PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the
cluster.

[id="using-pods_{context}"]
== Use pods and claimed PVs

Pods use claims as volumes. The cluster inspects the claim to find the bound
volume and mounts that volume for a pod. For those volumes that support
multiple access modes, you must specify which mode applies when you use
the claim as a volume in a pod.

Once you have a claim and that claim is bound, the bound PV belongs to you
for as long as you need it. You can schedule pods and access claimed
PVs by including `persistentVolumeClaim` in the pod's volumes block.

[NOTE]
====
If you attach persistent volumes that have high file counts to pods, those pods can fail or can take a long time to start. For
more information, see link:https://access.redhat.com/solutions/6221251[When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state?].
==== 

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]

[id="pvcprotection_{context}"]
== Storage Object in Use Protection

The Storage Object in Use Protection feature ensures that PVCs in active use by a pod and PVs that are bound to PVCs are not removed from the system, as this can result in data loss.

Storage Object in Use Protection is enabled by default.

[NOTE]
====
A PVC is in active use by a pod when a `Pod` object exists that uses the PVC.
====

If a user deletes a PVC that is in active use by a pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any pods. Also, if a cluster admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC.

endif::openshift-origin,openshift-enterprise,openshift-webscale[]

[id="releasing_{context}"]
== Release a persistent volume

When you are finished with a volume, you can delete the PVC object from
the API, which allows reclamation of the resource. The volume is
considered released when the claim is deleted, but it is not yet available
for another claim. The previous claimant's data remains on the volume and
must be handled according to policy.

[id="reclaiming_{context}"]
== Reclaim policy for persistent volumes

The reclaim policy of a persistent volume tells the cluster what to do with the volume after it is released. A volume's reclaim policy can be
`Retain`, `Recycle`, or `Delete`.

* `Retain` reclaim policy allows manual reclamation of the resource for
those volume plugins that support it.

* `Recycle` reclaim policy recycles the volume back into the pool of
unbound persistent volumes once it is released from its claim.

[IMPORTANT]
====
The `Recycle` reclaim policy is deprecated in {product-title} 4. Dynamic provisioning is recommended for equivalent and better
functionality.
====

* `Delete` reclaim policy deletes  both the `PersistentVolume` object
from {product-title} and the associated storage asset in external
infrastructure, such as Amazon Elastic Block Store (Amazon EBS) or VMware vSphere.

[NOTE]
====
Dynamically provisioned volumes are always deleted.
====
