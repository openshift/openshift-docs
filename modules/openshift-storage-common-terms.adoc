// Module included in the following assemblies:
//
// * storage/index.adoc

:_mod-docs-content-type: REFERENCE
[id="openshift-storage-common-terms_{context}"]
= Glossary of common terms for {product-title} storage

This glossary defines common terms that are used in the storage content.

Access modes:: Volume access modes describe volume capabilities. You can use access modes to match persistent volume claim (PVC) and persistent volume (PV). The following are the examples of access modes:

* ReadWriteOnce (RWO)
* ReadOnlyMany (ROX)
* ReadWriteMany (RWX)
* ReadWriteOncePod (RWOP)

ifndef::openshift-dedicated,openshift-rosa[]
Cinder:: The Block Storage service for {rh-openstack-first} which manages the administration, security, and scheduling of all volumes.
endif::openshift-dedicated,openshift-rosa[]

Config map:: A config map provides a way to inject configuration data into pods. You can reference the data stored in a config map in a volume of type `ConfigMap`. Applications running in a pod can use this data.

Container Storage Interface (CSI)::
An API specification for the management of container storage across different container orchestration (CO) systems.

Dynamic Provisioning::
The framework allows you to create storage volumes on-demand, eliminating the need for cluster administrators to pre-provision persistent storage.

Ephemeral storage::
Pods and containers can require temporary or transient local storage for their operation. The lifetime of this ephemeral storage does not extend beyond the life of the individual pod, and this ephemeral storage cannot be shared across pods.

ifndef::openshift-dedicated,openshift-rosa[]
Fiber channel:: A networking technology that is used to transfer data among data centers, computer servers, switches and storage.

FlexVolume:: FlexVolume is an out-of-tree plugin interface that uses an exec-based model to interface with storage drivers. You must install the FlexVolume driver binaries in a pre-defined volume plugin path on each node and in some cases the control plane nodes.
endif::openshift-dedicated,openshift-rosa[]

fsGroup:: The fsGroup defines a file system group ID of a pod.

ifndef::openshift-dedicated,openshift-rosa[]
iSCSI:: Internet Small Computer Systems Interface (iSCSI) is an Internet Protocol-based storage networking standard for linking data storage facilities.
An iSCSI volume allows an existing iSCSI (SCSI over IP) volume to be mounted into your Pod.
endif::openshift-dedicated,openshift-rosa[]

hostPath::
A hostPath volume in an OpenShift Container Platform cluster mounts a file or directory from the host node’s filesystem into your pod.

KMS key:: The Key Management Service (KMS) helps you achieve the required level of encryption of your data across different services. you can use the KMS key to encrypt, decrypt, and re-encrypt data.

Local volumes:: A local volume represents a mounted local storage device such as a disk, partition or directory.

ifndef::openshift-dedicated,openshift-rosa[]
NFS:: A Network File System (NFS) that allows remote hosts to mount file systems over a network and interact with those file systems as though they are mounted locally. This enables system administrators to consolidate resources onto centralized servers on the network.
endif::openshift-dedicated,openshift-rosa[]

OpenShift Data Foundation::
A provider of agnostic persistent storage for OpenShift Container Platform supporting file, block, and object storage, either in-house or in hybrid clouds

Persistent storage::
Pods and containers can require permanent storage for their operation. {product-title} uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision persistent storage for a cluster. Developers can use PVC to request PV resources without having specific knowledge of the underlying storage infrastructure.

Persistent volumes (PV):: {product-title} uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision persistent storage for a cluster. Developers can use PVC to request PV resources without having specific knowledge of the underlying storage infrastructure.

Persistent volume claims (PVCs):: You can use a PVC to mount a PersistentVolume into a Pod. You can access the storage without knowing the details of the cloud environment.

Pod::
One or more containers with shared resources, such as volume and IP addresses, running in your {product-title} cluster.
A pod is the smallest compute unit defined, deployed, and managed.

Reclaim policy::
A policy that tells the cluster what to do with the volume after it is released. A volume’s reclaim policy can be `Retain`, `Recycle`, or `Delete`.

Role-based access control (RBAC):: Role-based access control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within your organization.

Stateless applications:: A stateless application is an application program that does not save client data generated in one session for use in the next session with that client.

Stateful applications:: A stateful application is an application program that saves data to persistent disk storage. A server, client, and applications can use a persistent disk storage. You can use the `Statefulset` object in {product-title} to manage the deployment and scaling of a set of Pods, and provides guarantee about the ordering and uniqueness of these Pods.

Static provisioning:: A cluster administrator creates a number of PVs. PVs contain the details of storage. PVs exist in the Kubernetes API and are available for consumption.

Storage:: {product-title} supports many types of storage, both for on-premise and cloud providers. You can manage container storage for persistent and non-persistent data in an {product-title} cluster.

Storage class:: A storage class provides a way for administrators to describe the classes of storage they offer. Different classes might map to quality of service levels, backup policies, arbitrary policies determined by the cluster administrators.

ifndef::openshift-dedicated,openshift-rosa[]
VMware vSphere’s Virtual Machine Disk (VMDK) volumes:: Virtual Machine Disk (VMDK) is a file format that describes containers for virtual hard disk drives that is used in virtual machines.
endif::openshift-dedicated,openshift-rosa[]