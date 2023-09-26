[id="persistentvolume-core-v1"]
= PersistentVolume [core/v1]
ifdef::product-title[]
include::_attributes/common-attributes.adoc[]
endif::[]

toc::[]


Description::
+
--
PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
--

Type::
  `object`



== Specification

[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `apiVersion`
| `string`
| APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

| `kind`
| `string`
| Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

| `metadata`
| xref:../objects/index.adoc#objectmeta-meta-v1[`ObjectMeta meta/v1`]
| Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

| `spec`
| `object`
| PersistentVolumeSpec is the specification of a persistent volume.

| `status`
| `object`
| PersistentVolumeStatus is the current status of a persistent volume.

|===
..spec
Description::
+
--
PersistentVolumeSpec is the specification of a persistent volume.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `accessModes`
| `array (string)`
| AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes

| `awsElasticBlockStore`
| xref:../objects/index.adoc#awselasticblockstorevolumesource-core-v1[`AWSElasticBlockStoreVolumeSource core/v1`]
| AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

| `azureDisk`
| xref:../objects/index.adoc#azurediskvolumesource-core-v1[`AzureDiskVolumeSource core/v1`]
| AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

| `azureFile`
| xref:../objects/index.adoc#azurefilepersistentvolumesource-core-v1[`AzureFilePersistentVolumeSource core/v1`]
| AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

| `capacity`
| xref:../objects/index.adoc#quantity-api-none[`object (Quantity api/none)`]
| A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

| `cephfs`
| xref:../objects/index.adoc#cephfspersistentvolumesource-core-v1[`CephFSPersistentVolumeSource core/v1`]
| CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

| `cinder`
| xref:../objects/index.adoc#cinderpersistentvolumesource-core-v1[`CinderPersistentVolumeSource core/v1`]
| Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md

| `claimRef`
| xref:../objects/index.adoc#objectreference-core-v1[`ObjectReference core/v1`]
| ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding

| `csi`
| xref:../objects/index.adoc#csipersistentvolumesource-core-v1[`CSIPersistentVolumeSource core/v1`]
| CSI represents storage that is handled by an external CSI driver (Beta feature).

| `fc`
| xref:../objects/index.adoc#fcvolumesource-core-v1[`FCVolumeSource core/v1`]
| FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

| `flexVolume`
| xref:../objects/index.adoc#flexpersistentvolumesource-core-v1[`FlexPersistentVolumeSource core/v1`]
| FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.

| `flocker`
| xref:../objects/index.adoc#flockervolumesource-core-v1[`FlockerVolumeSource core/v1`]
| Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

| `gcePersistentDisk`
| xref:../objects/index.adoc#gcepersistentdiskvolumesource-core-v1[`GCEPersistentDiskVolumeSource core/v1`]
| GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

| `glusterfs`
| xref:../objects/index.adoc#glusterfspersistentvolumesource-core-v1[`GlusterfsPersistentVolumeSource core/v1`]
| Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md

| `hostPath`
| xref:../objects/index.adoc#hostpathvolumesource-core-v1[`HostPathVolumeSource core/v1`]
| HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

| `iscsi`
| xref:../objects/index.adoc#iscsipersistentvolumesource-core-v1[`ISCSIPersistentVolumeSource core/v1`]
| ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

| `local`
| xref:../objects/index.adoc#localvolumesource-core-v1[`LocalVolumeSource core/v1`]
| Local represents directly-attached storage with node affinity

| `mountOptions`
| `array (string)`
| A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options

| `nfs`
| xref:../objects/index.adoc#nfsvolumesource-core-v1[`NFSVolumeSource core/v1`]
| NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

| `nodeAffinity`
| xref:../objects/index.adoc#volumenodeaffinity-core-v1[`VolumeNodeAffinity core/v1`]
| NodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.

| `persistentVolumeReclaimPolicy`
| `string`
| What happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming

| `photonPersistentDisk`
| xref:../objects/index.adoc#photonpersistentdiskvolumesource-core-v1[`PhotonPersistentDiskVolumeSource core/v1`]
| PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

| `portworxVolume`
| xref:../objects/index.adoc#portworxvolumesource-core-v1[`PortworxVolumeSource core/v1`]
| PortworxVolume represents a portworx volume attached and mounted on kubelets host machine

| `quobyte`
| xref:../objects/index.adoc#quobytevolumesource-core-v1[`QuobyteVolumeSource core/v1`]
| Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

| `rbd`
| xref:../objects/index.adoc#rbdpersistentvolumesource-core-v1[`RBDPersistentVolumeSource core/v1`]
| RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md

| `scaleIO`
| xref:../objects/index.adoc#scaleiopersistentvolumesource-core-v1[`ScaleIOPersistentVolumeSource core/v1`]
| ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

| `storageClassName`
| `string`
| Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.

| `storageos`
| xref:../objects/index.adoc#storageospersistentvolumesource-core-v1[`StorageOSPersistentVolumeSource core/v1`]
| StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md

| `volumeMode`
| `string`
| volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.

| `vsphereVolume`
| xref:../objects/index.adoc#vspherevirtualdiskvolumesource-core-v1[`VsphereVirtualDiskVolumeSource core/v1`]
| VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

|===
..status
Description::
+
--
PersistentVolumeStatus is the current status of a persistent volume.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `message`
| `string`
| A human-readable message indicating details about why the volume is in this state.

| `phase`
| `string`
| Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase

| `reason`
| `string`
| Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.

|===

== API endpoints

The following API endpoints are available:

* `/api/v1/persistentvolumes`
- `DELETE`: delete collection of PersistentVolume
- `GET`: list or watch objects of kind PersistentVolume
- `POST`: create a PersistentVolume
* `/api/v1/persistentvolumes/{name}`
- `DELETE`: delete a PersistentVolume
- `GET`: read the specified PersistentVolume
- `PATCH`: partially update the specified PersistentVolume
- `PUT`: replace the specified PersistentVolume
* `/api/v1/persistentvolumes/{name}/status`
- `GET`: read status of the specified PersistentVolume
- `PATCH`: partially update status of the specified PersistentVolume
- `PUT`: replace status of the specified PersistentVolume


=== /api/v1/persistentvolumes


.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `DELETE`

Description::
  delete collection of PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `continue`
| `string`
| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the &quot;next key&quot;.

This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldSelector`
| `string`
| A selector to restrict the list of returned objects by their fields. Defaults to everything.
| `gracePeriodSeconds`
| `integer`
| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
| `labelSelector`
| `string`
| A selector to restrict the list of returned objects by their labels. Defaults to everything.
| `limit`
| `integer`
| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.

The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
| `orphanDependents`
| `boolean`
| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the &quot;orphan&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
| `propagationPolicy`
| `string`
| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground.
| `resourceVersion`
| `string`
| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `resourceVersionMatch`
| `string`
| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `timeoutSeconds`
| `integer`
| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#deleteoptions-meta-v1[`DeleteOptions meta/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#status-meta-v1[`Status meta/v1`]
|===

HTTP method::
  `GET`

Description::
  list or watch objects of kind PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `allowWatchBookmarks`
| `boolean`
| allowWatchBookmarks requests watch events with type &quot;BOOKMARK&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#x27;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.
| `continue`
| `string`
| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the &quot;next key&quot;.

This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
| `fieldSelector`
| `string`
| A selector to restrict the list of returned objects by their fields. Defaults to everything.
| `labelSelector`
| `string`
| A selector to restrict the list of returned objects by their labels. Defaults to everything.
| `limit`
| `integer`
| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.

The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
| `resourceVersion`
| `string`
| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `resourceVersionMatch`
| `string`
| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `timeoutSeconds`
| `integer`
| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
| `watch`
| `boolean`
| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
|===


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#persistentvolumelist-core-v1[`PersistentVolumeList core/v1`]
|===

HTTP method::
  `POST`

Description::
  create a PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===


=== /api/v1/persistentvolumes/{name}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the PersistentVolume
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `DELETE`

Description::
  delete a PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `gracePeriodSeconds`
| `integer`
| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
| `orphanDependents`
| `boolean`
| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the &quot;orphan&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
| `propagationPolicy`
| `string`
| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#deleteoptions-meta-v1[`DeleteOptions meta/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===

HTTP method::
  `GET`

Description::
  read the specified PersistentVolume


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update the specified PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
| `force`
| `boolean`
| Force is going to &quot;force&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#patch-meta-v1[`Patch meta/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace the specified PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===


=== /api/v1/persistentvolumes/{name}/status

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the PersistentVolume
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `GET`

Description::
  read status of the specified PersistentVolume


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update status of the specified PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
| `force`
| `boolean`
| Force is going to &quot;force&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#patch-meta-v1[`Patch meta/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace status of the specified PersistentVolume


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/persistentvolume-core-v1.adoc#persistentvolume-core-v1[`PersistentVolume core/v1`]
|===


