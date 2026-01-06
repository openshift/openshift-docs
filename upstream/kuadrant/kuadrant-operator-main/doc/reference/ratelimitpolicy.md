# The RateLimitPolicy Custom Resource Definition (CRD)

- [RateLimitPolicy](#ratelimitpolicy)
- [RateLimitPolicySpec](#ratelimitpolicyspec)
    - [RateLimitPolicyCommonSpec](#rateLimitPolicyCommonSpec)
    - [Limit](#limit)
        - [RateLimit](#ratelimit)
        - [WhenCondition](#whencondition)
- [RateLimitPolicyStatus](#ratelimitpolicystatus)
    - [ConditionSpec](#conditionspec)

## RateLimitPolicy

| **Field** | **Type**                                        | **Required** | **Description**                                       |
|-----------|-------------------------------------------------|:------------:|-------------------------------------------------------|
| `spec`    | [RateLimitPolicySpec](#ratelimitpolicyspec)     |     Yes      | The specification for RateLimitPolicy custom resource |
| `status`  | [RateLimitPolicyStatus](#ratelimitpolicystatus) |      No      | The status for the custom resource                    |

## RateLimitPolicySpec

| **Field**   | **Type**                                                                                                                                    | **Required** | **Description**                                                                                                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `targetRef` | [PolicyTargetReference](https://gateway-api.sigs.k8s.io/v1alpha2/references/spec/#gateway.networking.k8s.io/v1alpha2.PolicyTargetReference) | Yes          | Reference to a Kubernetes resource that the policy attaches to                                                                                                                              |
| `defaults`  | [RateLimitPolicyCommonSpec](#rateLimitPolicyCommonSpec)                                                                                     | No           | Default limit definitions. This field is mutually exclusive with the `limits` field                                                                                                         |
| `overrides` | [RateLimitPolicyCommonSpec](#rateLimitPolicyCommonSpec)                                                                                     | No           | Overrides limit definitions. This field is mutually exclusive with the `limits` field and `defaults` field. This field is only allowed for policies targeting `Gateway` in `targetRef.kind` |
| `limits`    | Map<String: [Limit](#limit)>                                                                                                                | No           | Limit definitions. This field is mutually exclusive with the [`defaults`](#rateLimitPolicyCommonSpec) field                                                                                 |

### RateLimitPolicyCommonSpec

| **Field** | **Type**                     | **Required** | **Description**                                                                                                              |
|-----------|------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
| `limits`  | Map<String: [Limit](#limit)> | No           | Explicit Limit definitions. This field is mutually exclusive with [RateLimitPolicySpec](#ratelimitpolicyspec) `limits` field |

### Limit

| **Field**        | **Type**                                            | **Required** | **Description**                                                                                                                                                                                                                                                                                                  |
|------------------|-----------------------------------------------------|:------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `rates`          | [][RateLimit](#ratelimit)                           |      No      | List of rate limits associated with the limit definition                                                                                                                                                                                                                                                         |
| `counters`       | []String                                            |      No      | List of rate limit counter qualifiers. Items must be a valid [Well-known attribute](https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md). Each distinct value resolved in the data plane starts a separate counter for each rate limit.                                        |
| `routeSelectors` | [][RouteSelector](route-selectors.md#routeselector) |      No      | List of selectors of HTTPRouteRules whose matching rules activate the limit. At least one HTTPRouteRule must be selected to activate the limit. If omitted, all HTTPRouteRules of the targeted HTTPRoute activate the limit. Do not use it in policies targeting a Gateway.                                      |
| `when`           | [][WhenCondition](#whencondition)                   |      No      | List of additional dynamic conditions (expressions) to activate the limit. All expression must evaluate to true for the limit to be applied. Use it for filtering attributes that cannot be expressed in the targeted HTTPRoute's `spec.hostnames` and `spec.rules.matches` fields, or when targeting a Gateway. |

#### RateLimit

| **Field**  | **Type** | **Required** | **Description**                                                                        |
|------------|----------|:------------:|----------------------------------------------------------------------------------------|
| `limit`    | Number   |     Yes      | Maximum value allowed within the given period of time (duration)                       |
| `duration` | Number   |     Yes      | The period of time in the specified unit that the limit applies                        |
| `unit`     | String   |     Yes      | Unit of time for the duration of the limit. One-of: "second", "minute", "hour", "day". |

#### WhenCondition

| **Field**  | **Type** | **Required** | **Description**                                                                                                                                                                                                 |
|------------|----------|:------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `selector` | String   |     Yes      | A valid [Well-known attribute](https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md) whose resolved value in the data plane will be compared to `value`, using the `operator`. |
| `operator` | String   |     Yes      | The binary operator to be applied to the resolved value specified by the selector. One-of: "eq" (equal to), "neq" (not equal to)                                                                                |
| `value`    | String   |     Yes      | The static value to be compared to the one resolved from the selector.                                                                                                                                          |

## RateLimitPolicyStatus

| **Field**            | **Type**                          | **Description**                                                                                                                     |
|----------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `observedGeneration` | String                            | Number of the last observed generation of the resource. Use it to check if the status info is up to date with latest resource spec. |
| `conditions`         | [][ConditionSpec](#conditionspec) | List of conditions that define that status of the resource.                                                                         |

### ConditionSpec

* The *lastTransitionTime* field provides a timestamp for when the entity last transitioned from one status to another.
* The *message* field is a human-readable message indicating details about the transition.
* The *reason* field is a unique, one-word, CamelCase reason for the condition’s last transition.
* The *status* field is a string, with possible values **True**, **False**, and **Unknown**.
* The *type* field is a string with the following possible values:
    * Available: the resource has successfully configured;

| **Field**            | **Type**  | **Description**              |
|----------------------|-----------|------------------------------|
| `type`               | String    | Condition Type               |
| `status`             | String    | Status: True, False, Unknown |
| `reason`             | String    | Condition state reason       |
| `message`            | String    | Condition state description  |
| `lastTransitionTime` | Timestamp | Last transition timestamp    |
