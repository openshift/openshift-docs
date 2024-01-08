// Module included in the following assemblies:
//
// storage/understanding-persistent-storage.adoc
// microshift_storage/understanding-persistent-storage-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id=persistent-storage-overview_{context}]
= Persistent storage overview

ifndef::microshift[]
Managing storage is a distinct problem from managing compute resources. {product-title} uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision persistent storage for a cluster. Developers can use persistent volume claims (PVCs) to request PV resources without having specific knowledge of the underlying storage infrastructure.

PVCs are specific to a project, and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single project; they can be shared across the entire {product-title} cluster and claimed from any project. After a PV is bound to a PVC, that PV can not then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace, that of the binding project.
endif::microshift[]

ifdef::microshift[]
PVCs are specific to a namespace, and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single namespace; they can be shared across the entire {product-title} cluster and claimed from any namespace. After a PV is bound to a PVC, that PV can not then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace.
endif::microshift[]

PVs are defined by a `PersistentVolume` API object, which represents a piece of existing storage in the cluster that was either statically provisioned by the cluster administrator or dynamically provisioned using a `StorageClass` object. It is a resource in the cluster just like a node is a cluster resource.

ifndef::microshift[]
PVs are volume plugins like `Volumes` but have a lifecycle that is independent of any individual pod that uses the PV. PV objects capture the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.
endif::microshift[]

ifdef::microshift[]
PVs are volume plugins like `Volumes` but have a lifecycle that is independent of any individual pod that uses the PV. PV objects capture the details of the implementation of the storage, be that LVM, the host filesystem such as hostpath, or raw block devices.
endif::microshift[]

[IMPORTANT]
====
High availability of storage in the infrastructure is left to the underlying storage provider.
====

ifndef::microshift[]
PVCs are defined by a `PersistentVolumeClaim` API object, which represents a request for storage by a developer. It is similar to a pod in that pods consume node resources and PVCs consume PV resources. For example, pods can request specific levels of resources, such as CPU and memory, while PVCs can request specific storage capacity and access modes. For example, they can be mounted once read-write or many times read-only.
endif::microshift[]

ifdef::microshift[]
Like `PersistentVolumes`, `PersistentVolumeClaims` (PVCs) are API objects, which represents a request for storage by a developer. It is similar to a pod in that pods consume node resources and PVCs consume PV resources. For example, pods can request specific levels of resources, such as CPU and memory, while PVCs can request specific storage capacity and access modes. Access modes supported by {OCP} are also definable in {product-title}. However, because {product-title} does not support multi-node deployments, only ReadWriteOnce (RWO) is pertinent.
endif::microshift[]