// Module included in the following assemblies
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc

[id="available-plug-ins_{context}"]
= Available dynamic provisioning plugins

{product-title} provides the following provisioner plugins, which have
generic implementations for dynamic provisioning that use the cluster's
configured provider's API to create new storage resources:


[options="header",cols="1,1,1"]
|===

|Storage type
|Provisioner plugin name
|Notes

ifndef::openshift-dedicated,openshift-rosa[]
|{rh-openstack-first} Cinder
|`kubernetes.io/cinder`
|

|{rh-openstack} Manila Container Storage Interface (CSI)
|`manila.csi.openstack.org`
|Once installed, the OpenStack Manila CSI Driver Operator and ManilaDriver automatically create the required storage classes for all available Manila share types needed for dynamic provisioning.
endif::openshift-dedicated,openshift-rosa[]

|Amazon Elastic Block Store (Amazon EBS)
|`kubernetes.io/aws-ebs`
|For dynamic provisioning when using multiple clusters in different zones,
tag each node with `Key=kubernetes.io/cluster/<cluster_name>,Value=<cluster_id>`
where `<cluster_name>` and `<cluster_id>` are unique per cluster.

ifndef::openshift-dedicated,openshift-rosa[]
|Azure Disk
|`kubernetes.io/azure-disk`
|

|Azure File
|`kubernetes.io/azure-file`
|The `persistent-volume-binder` service account requires permissions to create
and get secrets to store the Azure storage account and keys.
endif::openshift-dedicated,openshift-rosa[]

ifndef::openshift-rosa[]
|GCE Persistent Disk (gcePD)
|`kubernetes.io/gce-pd`
|In multi-zone configurations, it is advisable to run one {product-title}
cluster per GCE project to avoid PVs from being created in zones where
no node in the current cluster exists.

|{ibm-power-server-name} Block
|`powervs.csi.ibm.com`
|After installation, the {ibm-power-server-name} Block CSI Driver Operator and {ibm-power-server-name} Block CSI Driver automatically create the required storage classes for dynamic provisioning.
endif::openshift-rosa[]

//|GlusterFS
//|`kubernetes.io/glusterfs`
//|

//|Ceph RBD
//|`kubernetes.io/rbd`
//|

//|Trident from NetApp
//|`netapp.io/trident`
//|Storage orchestrator for NetApp ONTAP, SolidFire, and E-Series storage.

ifndef::openshift-dedicated,openshift-rosa[]
|link:https://www.vmware.com/support/vsphere.html[VMware vSphere]
|`kubernetes.io/vsphere-volume`
|
endif::openshift-dedicated,openshift-rosa[]

//|HPE Nimble Storage
//|`hpe.com/nimble`
//|Dynamic provisioning of HPE Nimble Storage resources using the
//HPE Nimble Kube Storage Controller.

|===

[IMPORTANT]
====
Any chosen provisioner plugin also requires configuration for the relevant
cloud, host, or third-party provider as per the relevant documentation.
====
