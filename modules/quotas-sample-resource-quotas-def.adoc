// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

[id="quotas-sample-resource-quota-definitions_{context}"]
= Sample resource quota definitions

.`core-object-counts.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: core-object-counts
spec:
  hard:
    configmaps: "10" <1>
    persistentvolumeclaims: "4" <2>
    replicationcontrollers: "20" <3>
    secrets: "10" <4>
    services: "10" <5>
    services.loadbalancers: "2" <6>
----
<1> The total number of `ConfigMap` objects that can exist in the project.
<2> The total number of persistent volume claims (PVCs) that can exist in the
project.
<3> The total number of replication controllers that can exist in the project.
<4> The total number of secrets that can exist in the project.
<5> The total number of services that can exist in the project.
<6> The total number of services of type `LoadBalancer` that can exist in the project.

.`openshift-object-counts.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: openshift-object-counts
spec:
  hard:
    openshift.io/imagestreams: "10" <1>
----
<1> The total number of image streams that can exist in the project.

.`compute-resources.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    pods: "4" <1>
    requests.cpu: "1" <2>
    requests.memory: 1Gi <3>
    limits.cpu: "2" <4>
    limits.memory: 2Gi <5>
    
----
<1> The total number of pods in a non-terminal state that can exist in the project.
<2> Across all pods in a non-terminal state, the sum of CPU requests cannot exceed 1 core.
<3> Across all pods in a non-terminal state, the sum of memory requests cannot exceed 1Gi.
<4> Across all pods in a non-terminal state, the sum of CPU limits cannot exceed 2 cores.
<5> Across all pods in a non-terminal state, the sum of memory limits cannot exceed 2Gi.


.`besteffort.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: besteffort
spec:
  hard:
    pods: "1" <1>
  scopes:
  - BestEffort <2>
----
<1> The total number of pods in a non-terminal state with `BestEffort` quality of service that can exist in the project.
<2> Restricts the quota to only matching pods that have `BestEffort` quality of service for either memory or CPU.

.`compute-resources-long-running.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-long-running
spec:
  hard:
    pods: "4" <1>
    limits.cpu: "4" <2>
    limits.memory: "2Gi" <3>
  scopes:
  - NotTerminating <4>
----
<1> The total number of pods in a non-terminal state.
<2> Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value.
<3> Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value.
<4> Restricts the quota to only matching pods where `spec.activeDeadlineSeconds` is set to `nil`. Build pods fall under `NotTerminating` unless the `RestartNever` policy is applied.

.`compute-resources-time-bound.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources-time-bound
spec:
  hard:
    pods: "2" <1>
    limits.cpu: "1" <2>
    limits.memory: "1Gi" <3>
  scopes:
  - Terminating <4>
----
<1> The total number of pods in a terminating state.
<2> Across all pods in a terminating state, the sum of CPU limits cannot exceed this value.
<3> Across all pods in a terminating state, the sum of memory limits cannot exceed this value.
<4> Restricts the quota to only matching pods where `spec.activeDeadlineSeconds >=0`. For example, this quota charges for build or deployer pods, but not long running pods like a web server or database.

.`storage-consumption.yaml`
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: storage-consumption
spec:
  hard:
    persistentvolumeclaims: "10" <1>
    requests.storage: "50Gi" <2>
    gold.storageclass.storage.k8s.io/requests.storage: "10Gi" <3>
    silver.storageclass.storage.k8s.io/requests.storage: "20Gi" <4>
    silver.storageclass.storage.k8s.io/persistentvolumeclaims: "5" <5>
    bronze.storageclass.storage.k8s.io/requests.storage: "0" <6>
    bronze.storageclass.storage.k8s.io/persistentvolumeclaims: "0" <7>
    requests.ephemeral-storage: 2Gi <8>
    limits.ephemeral-storage: 4Gi <9>
----
<1> The total number of persistent volume claims in a project
<2> Across all persistent volume claims in a project, the sum of storage requested cannot exceed this value.
<3> Across all persistent volume claims in a project, the sum of storage requested in the gold storage class cannot exceed this value.
<4> Across all persistent volume claims in a project, the sum of storage requested in the silver storage class cannot exceed this value.
<5> Across all persistent volume claims in a project, the total number of claims in the silver storage class cannot exceed this value.
<6> Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot request storage.
<7> Across all persistent volume claims in a project, the sum of storage requested in the bronze storage class cannot exceed this value. When this is set to `0`, it means bronze storage class cannot create claims.
<8> Across all pods in a non-terminal state, the sum of ephemeral storage requests cannot exceed 2Gi.
<9> Across all pods in a non-terminal state, the sum of ephemeral storage limits cannot exceed 4Gi.
