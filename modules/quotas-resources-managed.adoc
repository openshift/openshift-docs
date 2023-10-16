// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-resources-managed_{context}"]
= Resources managed by quotas

The following describes the set of compute resources and object types that can be managed by a quota.

[NOTE]
====
A pod is in a terminal state if `status.phase in (Failed, Succeeded)` is true.
====

.Compute resources managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`cpu`
|The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.

|`memory`
|The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.

|`requests.cpu`
|The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.

|`requests.memory`
|The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.

|`limits.cpu`
|The sum of CPU limits across all pods in a non-terminal state cannot exceed this value.

|`limits.memory`
|The sum of memory limits across all pods in a non-terminal state cannot exceed this value.

|===

.Storage resources managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`requests.storage`
|The sum of storage requests across all persistent volume claims in any state cannot exceed this value.

|`persistentvolumeclaims`
|The total number of persistent volume claims that can exist in the project.

|`<storage-class-name>.storageclass.storage.k8s.io/requests.storage`
|The sum of storage requests across all persistent volume claims in any state that have a matching storage class, cannot exceed this value.

|`<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims`
|The total number of persistent volume claims with a matching storage class that can exist in the project.

|`ephemeral-storage`
|The sum of local ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably.

|`requests.ephemeral-storage`
|The sum of ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably.

|`limits.ephemeral-storage`
|The sum of ephemeral storage limits across all pods in a non-terminal state cannot exceed this value.
|===

[id="quotas-object-counts-managed_{context}"]
.Object counts managed by quota
[cols="3a,8a",options="header"]
|===

|Resource Name |Description

|`pods`
|The total number of pods in a non-terminal state that can exist in the project.

|`replicationcontrollers`
|The total number of ReplicationControllers that can exist in the project.

|`resourcequotas`
|The total number of resource quotas that can exist in the project.

|`services`
|The total number of services that can exist in the project.

|`services.loadbalancers`
|The total number of services of type `LoadBalancer` that can exist in the project.

|`services.nodeports`
|The total number of services of type `NodePort` that can exist in the project.

|`secrets`
|The total number of secrets that can exist in the project.

|`configmaps`
|The total number of `ConfigMap` objects that can exist in the project.

|`persistentvolumeclaims`
|The total number of persistent volume claims that can exist in the project.

|`openshift.io/imagestreams`
|The total number of imagestreams that can exist in the project.
|===
