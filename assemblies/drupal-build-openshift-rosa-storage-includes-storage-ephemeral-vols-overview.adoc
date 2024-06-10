// Module included in the following assemblies:
//
// * storage/generic-ephemeral-vols.adoc
//* microshift_storage/generic-ephemeral-volumes-microshift.adoc


:_mod-docs-content-type: CONCEPT
[id="generic-ephemeral-vols-overview_{context}"]
= Overview

Generic ephemeral volumes are a type of ephemeral volume that can be provided by all storage drivers that support persistent volumes and dynamic provisioning. Generic ephemeral volumes are similar to `emptyDir` volumes in that they provide a per-pod directory for scratch data, which is usually empty after provisioning.

Generic ephemeral volumes are specified inline in the pod spec and follow the pod's lifecycle. They are created and deleted along with the pod.

Generic ephemeral volumes have the following features:

* Storage can be local or network-attached.

* Volumes can have a fixed size that pods are not able to exceed.

* Volumes might have some initial data, depending on the driver and parameters.

* Typical operations on volumes are supported, assuming that the driver supports them, including snapshotting, cloning, resizing, and storage capacity tracking.

[NOTE]
====
Generic ephemeral volumes do not support offline snapshots and resize.

ifndef::openshift-dedicated,openshift-rosa,microshift[]
Due to this limitation, the following Container Storage Interface (CSI) drivers do not support the following features for generic ephemeral volumes:

* Azure Disk CSI driver does not support resize.

* Cinder CSI driver does not support snapshot.
endif::openshift-dedicated,openshift-rosa,microshift[]
====
