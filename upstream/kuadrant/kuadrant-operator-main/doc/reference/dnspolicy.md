# The DNSPolicy Custom Resource Definition (CRD)

- [DNSPolicy](#DNSPolicy)
- [DNSPolicySpec](#dnspolicyspec)
    - [HealthCheckSpec](#healthcheckspec)
    - [LoadBalancingSpec](#loadbalancingspec)
      - [LoadBalancingWeighted](#loadbalancingweighted)
        - [CustomWeight](#customweight)
      - [LoadBalancingGeo](#loadbalancinggeo)
- [DNSPolicyStatus](#dnspolicystatus)
    - [HealthCheckStatus](#healthcheckstatus)

## DNSPolicy

| **Field** | **Type**                                       | **Required** | **Description**                                |
|-----------|------------------------------------------------|:------------:|------------------------------------------------|
| `spec`    | [DNSPolicySpec](#dnspolicyspec)     |    Yes       | The specification for DNSPolicy custom resource |
| `status`  | [DNSPolicyStatus](#dnspolicystatus) |      No      | The status for the custom resource             | 

## DNSPolicySpec

| **Field**         | **Type**                                                                                                                          |      **Required**      | **Description**                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|:----------------------:|---------------------------------------------------------------------------|
| `targetRef`       | [Gateway API PolicyTargetReference](https://gateway-api.sigs.k8s.io/geps/gep-713/?h=policytargetreference#policy-targetref-api)   |          Yes           | Reference to a Kubernetes resource that the policy attaches to            |
| `healthCheck`     | [HealthCheckSpec](#healthcheckspec)                                                                                               |           No           | HealthCheck spec                                                          |
| `loadBalancing`   | [LoadBalancingSpec](#loadbalancingspec)                                                                                           | Yes(loadbalanced only) | LoadBalancing Spec, required when routingStrategy is "loadbalanced"       |
| `routingStrategy` | String (immutable)                                                                                                                |          Yes           | **Immutable!** Routing Strategy to use, one of "simple" or "loadbalanced" |

## HealthCheckSpec

| **Field**          | **Type**   | **Required** | **Description**                                                                                           |
|--------------------|------------|:------------:|-----------------------------------------------------------------------------------------------------------|
| `endpoint`         | String     |     Yes      | Endpoint is the path to append to the host to reach the expected health check                             | 
| `port`             | Number     |     Yes      | Port to connect to the host on                                                                            | 
| `protocol`         | String     |     Yes      | Protocol to use when connecting to the host, valid values are "HTTP" or "HTTPS"                           | 
| `failureThreshold` | Number     |     Yes      | FailureThreshold is a limit of consecutive failures that must occur for a host to be considered unhealthy | 

## LoadBalancingSpec

| **Field**  | **Type**                                        | **Required**  | **Description**         |
|------------|-------------------------------------------------|:-------------:|-------------------------|
| `weighted` | [LoadBalancingWeighted](#loadbalancingweighted) |      Yes      | Weighted routing spec   |
| `geo`      | [LoadBalancingGeo](#loadbalancinggeo)           |      Yes      | Geo routing spec        |

## LoadBalancingWeighted

| **Field**       | **Type**                        | **Required** | **Description**                                                       |
|-----------------|---------------------------------|:------------:|-----------------------------------------------------------------------|
| `defaultWeight` | Number                          |     Yes      | Default weight to apply to created records                            |
| `custom`        | [][CustomWeight](#customweight) |      No      | Custom weights to manipulate records weights based on label selectors |

## CustomWeight

| **Field**  | **Type**             | **Description**                                                          |
|------------|----------------------|--------------------------------------------------------------------------|
| `selector` | metav1.LabelSelector | Label Selector to specify resources that should have this weight applied |
| `weight`   | Number               | Weight value to apply for matching resources                             |

## LoadBalancingGeo

| **Field**       | **Type**                        | **Required** | **Description**                 |
|-----------------|---------------------------------|:------------:|---------------------------------|
| `defaultGeo` | String                          |     Yes      | Default geo to apply to records |

## DNSPolicyStatus

| **Field**            | **Type**                                                                                                    | **Description**                                                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `observedGeneration` | String                                                                                                      | Number of the last observed generation of the resource. Use it to check if the status info is up to date with latest resource spec. |
| `conditions`         | [][Kubernetes meta/v1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition)         | List of conditions that define that status of the resource.                                                                         |
| `healthCheck`        | [HealthCheckStatus](#healthcheckstatus)                                                                     | HealthCheck status.                                                                                                                 |
| `recordConditions`   | [String][][Kubernetes meta/v1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition) | Status of individual DNSRecords owned by this policy.                                                                               |

## HealthCheckStatus

| **Field**     | **Type**                          | **Description**                                                                                                                     |
|---------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `conditions`  | [][Kubernetes meta/v1.Condition](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Condition)  | List of conditions that define that status of the resource.                                                                         |
