# The Kuadrant Custom Resource Definition (CRD)

## kuadrant

<details>
    <summary>Note on Limitador</summary>
The Kuadrant operator creates a Limitador CR named `limitador` in the same namespace as the Kuadrant CR. If there is a pre-existing Limitador CR of the same name the kuadrant operator will take ownership of that Limitador CR. 
</details>

| **Field** | **Type**                          | **Required** | **Description**                                 |
|-----------|-----------------------------------|:------------:|-------------------------------------------------|
| `spec`    | [KuadrantSpec](#kuadrantspec)     |      No      | The specification for Kuadrant custom resource. |
| `status`  | [KuadrantStatus](#kuadrantstatus) |      No      | The status for the custom resources.            |

## KuadrantSpec

| **Field**   | **Type**                | **Required** | **Description**                  |
|-------------|-------------------------|:------------:|----------------------------------|
| `limitador` | [Limitador](#limitador) |      No      | Configure limitador deployments. | 

### Limitador

| **Field**              | **Type**                                                                           | **Required** | **Description**                                    |
|------------------------|------------------------------------------------------------------------------------|:------------:|----------------------------------------------------|
| `affinity`             | [Affinity](https://pkg.go.dev/k8s.io/api/core/v1#Affinity)                         |      No      | Describes the scheduling rules for limitador pods. |
| `replicas`             | Number                                                                             |      No      | Sets the number of limitador replicas to deploy.   |
| `resourceRequirements` | [ResourceRequirements](https://pkg.go.dev/k8s.io/api/core/v1#ResourceRequirements) |      No      | Set the resource requirements for limitador pods.  |
| `pdb`                  | [PodDisruptionBudgetType](#poddisruptionbudgettype)                                |      No      | Configure allowed pod disruption budget fields.    |
| `storage`              | [Storage](#storage)                                                                |      No      | Define backend storage option for limitador.       |

### PodDisruptionBudgetType

| **Field**        | **Type** | **Required** | **Description**                                                                                                                                                                                                                                                                |
|------------------|----------|:------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `maxUnavailable` | Number   |      No      | An eviction is allowed if at most "maxUnavailable" limitador pods are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable". |
| `minAvailable`   | Number   |      No      | An eviction is allowed if at least "minAvailable" limitador pods will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".                                        |

### Storage

| **Field**      | **Type**                    | **Required** | **Description**                                                                                                                                                          |
|----------------|-----------------------------|:------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `redis`        | [Redis](#redis)             |      No      | Uses Redis to store limitador counters.                                                                                                                                  |
| `redis-cached` | [RedisCached](#redisCached) |      No      | Uses Redis to store limitador counters, with an in-memory cache                                                                                                          |
| `disk`         | [Disk](#disk)               |      No      | Counters are held on disk (persistent). Kubernetes [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) will be used to store counters. |

#### Redis

| **Field**         | **Type**                                                                           | **Required** | **Description**                                                 |
|-------------------|------------------------------------------------------------------------------------|:------------:|-----------------------------------------------------------------|
| `configSecretRef` | [LocalObjectReference](https://pkg.go.dev/k8s.io/api/core/v1#LocalObjectReference) |      No      | ConfigSecretRef refers to the secret holding the URL for Redis. |

#### RedisCached

| **Field**         | **Type**                                                                           | **Required** | **Description**                                                 |
|-------------------|------------------------------------------------------------------------------------|:------------:|-----------------------------------------------------------------|
| `configSecretRef` | [LocalObjectReference](https://pkg.go.dev/k8s.io/api/core/v1#LocalObjectReference) |      No      | ConfigSecretRef refers to the secret holding the URL for Redis. |
| `options`         | [Options](#options)                                                                |      No      | Configures a number of caching options for limitador.           |

##### Options

| **Field**      | **Type** | **Required** | **Description**                                                            |
|----------------|----------|:------------:|----------------------------------------------------------------------------|
| `ttl`          | Number   |      No      | TTL for cached counters in milliseconds [default: 5000]                    |
| `ratio`        | Number   |      No      | Ratio to apply to the TTL from Redis on cached counters [default: 10]      |
| `flush-period` | Number   |      No      | FlushPeriod for counters in milliseconds [default: 1000]                   |
| `max-cached`   | Number   |      No      | MaxCached refers to the maximum amount of counters cached [default: 10000] |

#### Disk

| **Field**               | **Type**                          | **Required** | **Description**                                                                               |
|-------------------------|-----------------------------------|:------------:|-----------------------------------------------------------------------------------------------|
| `persistentVolumeClaim` | [PVCGenericSpec](#pvcgenericspec) |      No      | Configure resources for PVC.                                                                  |
| `Optimize`              | String                            |      No      | Defines optimization option of the disk persistence type. Valid options: "throughput", "disk" |

##### PVCGenericSpec

| **Field**          | **Type**                                                          | **Required** | **Description**                                                               |
|--------------------|-------------------------------------------------------------------|:------------:|-------------------------------------------------------------------------------|
| `storageClassName` | String                                                            |      No      | Storage class name                                                            |
| `resources`        | [PersistentVolumeClaimResources](#persistentvolumeclaimresources) |      No      | Resources represent the minimum resources the volume should have              |
| `volumeName`       | String                                                            |      No      | VolumeName is the binding reference to the PersistentVolume backing the claim |

###### PersistentVolumeClaimResources

| **Field**  | **Type**                                                                             | **Required** | **Description**                                                     |
|------------|--------------------------------------------------------------------------------------|:------------:|---------------------------------------------------------------------|
| `requests` | [Quantity](https://pkg.go.dev/k8s.io/apimachinery@v0.28.4/pkg/api/resource#Quantity) |     Yes      | Storage resources requests to be used on the persisitentVolumeClaim |

## KuadrantStatus

| **Field**            | **Type**                                                                                     | **Description**                                                                                                                     |
|----------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `observedGeneration` | String                                                                                       | Number of the last observed generation of the resource. Use it to check if the status info is up to date with latest resource spec. |
| `conditions`         | [][ConditionSpec](https://pkg.go.dev/k8s.io/apimachinery@v0.28.4/pkg/apis/meta/v1#Condition) | List of conditions that define that status of the resource.                                                                         |
