// Module included in the following assemblies:
//
// * storage/understanding-persistent-storage.adoc
//* microshift_storage/understanding-persistent-storage-microshift.adoc


:_mod-docs-content-type: PROCEDURE
[id="reclaim-manual_{context}"]
= Reclaiming a persistent volume manually

ifndef::microshift[]
When a persistent volume claim (PVC) is deleted, the persistent volume (PV) still exists and is considered "released". However, the PV is not yet available for another claim because the data of the previous claimant remains on the volume.
endif::microshift[]

ifdef::microshift[]
When a persistent volume claim (PVC) is deleted, the underlying logical volume is handled according to the `reclaimPolicy`.
endif::[]

.Procedure
To manually reclaim the PV as a cluster administrator:

. Delete the PV.
+
[source,terminal]
----
$ oc delete pv <pv-name>
----
+
ifndef::openshift-dedicated,openshift-rosa[]
The associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume, still exists after the PV is deleted.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated[]
The associated storage asset in the external infrastructure, such as an AWS EBS or GCE PD volume, still exists after the PV is deleted.
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
The associated storage asset in the external infrastructure, such as an Amazon Elastic Block Store (Amazon EBS) volume, still exists after the PV is deleted.
endif::openshift-rosa[]

. Clean up the data on the associated storage asset.

. Delete the associated storage asset. Alternately, to reuse the same storage asset, create a new PV with the storage asset definition.

The reclaimed PV is now available for use by another PVC.
