# Kuadrant Rate Limiting

A Kuadrant RateLimitPolicy custom resource, often abbreviated "RateLimitPolicy":

1. Targets Gateway API networking resources such as [HTTPRoutes](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.HTTPRoute) and [Gateways](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.Gateway), using these resources to obtain additional context, i.e., which traffic workload (HTTP attributes, hostnames, user attributes, etc) to rate limit.
2. Supports targeting subsets (sections) of a network resource to apply the limits to.
3. Abstracts the details of the underlying Rate Limit protocol and configuration resources, that have a much broader remit and surface area.
4. Enables cluster operators to set defaults that govern behavior at the lower levels of the network, until a more specific policy is applied.

## How it works

### Envoy's Rate Limit Service Protocol

Kuadrant's Rate Limit implementation relies on the Envoy's [Rate Limit Service (RLS)](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ratelimit/v3/rls.proto) protocol. The workflow per request goes:
1. On incoming request, the gateway checks the matching rules for enforcing rate limits, as stated in the RateLimitPolicy custom resources and targeted Gateway API networking objects
2. If the request matches, the gateway sends one [RateLimitRequest](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ratelimit/v3/rls.proto#service-ratelimit-v3-ratelimitrequest) to the external rate limiting service ("Limitador").
1. The external rate limiting service responds with a [RateLimitResponse](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ratelimit/v3/rls.proto#service-ratelimit-v3-ratelimitresponse) back to the gateway with either an `OK` or `OVER_LIMIT` response code.

A RateLimitPolicy and its targeted Gateway API networking resource contain all the statements to configure both the ingress gateway and the external rate limiting service.

### The RateLimitPolicy custom resource

#### Overview

The `RateLimitPolicy` spec includes, basically, two parts:

* A reference to an existing Gateway API resource (`spec.targetRef`)
* Limit definitions (`spec.limits`)

Each limit definition includes:
* A set of rate limits (`spec.limits.<limit-name>.rates[]`)
* (Optional) A set of dynamic counter qualifiers (`spec.limits.<limit-name>.counters[]`)
* (Optional) A set of route selectors, to further qualify the specific routing rules when to activate the limit (`spec.limits.<limit-name>.routeSelectors[]`)
* (Optional) A set of additional dynamic conditions to activate the limit (`spec.limits.<limit-name>.when[]`)

The limit definitions (`limits`) can be declared at the top-level level of the spec (with the semantics of _defaults_) or alternatively within explicit `defaults` or `overrides` blocks.

<table>
  <tbody>
    <tr>
      <td>Check out Kuadrant <a href="https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md">RFC 0002</a> to learn more about the Well-known Attributes that can be used to define counter qualifiers (<code>counters</code>) and conditions (<code>when</code>).</td>
    </tr>
  </tbody>
</table>

#### High-level example and field definition

```yaml
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: my-rate-limit-policy
spec:
  # Reference to an existing networking resource to attach the policy to. REQUIRED.
  # It can be a Gateway API HTTPRoute or Gateway resource.
  # It can only refer to objects in the same namespace as the RateLimitPolicy.
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute / Gateway
    name: myroute / mygateway

  # The limits definitions to apply to the network traffic routed through the targeted resource.
  # Equivalent to if otherwise declared within `defaults`.
  limits:
    "my_limit":
      # The rate limits associated with this limit definition. REQUIRED.
      # E.g., to specify a 50rps rate limit, add `{ limit: 50, duration: 1, unit: secod }`
      rates: […]

      # Counter qualifiers.
      # Each dynamic value in the data plane starts a separate counter, combined with each rate limit.
      # E.g., to define a separate rate limit for each user name detected by the auth layer, add `metadata.filter_metadata.envoy\.filters\.http\.ext_authz.username`.
      # Check out Kuadrant RFC 0002 (https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md) to learn more about the Well-known Attributes that can be used in this field.
      counters: […]

      # Further qualification of the scpecific HTTPRouteRules within the targeted HTTPRoute that should trigger the limit.
      # Each element contains a HTTPRouteMatch object that will be used to select HTTPRouteRules that include at least one identical HTTPRouteMatch.
      # The HTTPRouteMatch part does not have to be fully identical, but the what's stated in the selector must be identically stated in the HTTPRouteRule.
      # Do not use it on RateLimitPolicies that target a Gateway.
      routeSelectors: […]

      # Additional dynamic conditions to trigger the limit.
      # Use it for filtering attributes not supported by HTTPRouteRule or with RateLimitPolicies that target a Gateway.
      # Check out Kuadrant RFC 0002 (https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md) to learn more about the Well-known Attributes that can be used in this field.
      when: […]

    # Explicit defaults. Used in policies that target a Gateway object to express default rules to be enforced on
    # routes that lack a more specific policy attached to.
    # Mutually exclusive with `overrides` and with declaring `limits` at the top-level of the spec.
    defaults:
      limits: {…}

    # Overrides. Used in policies that target a Gateway object to be enforced on all routes linked to the gateway,
    # thus also overriding any more specific policy occasionally attached to any of those routes.
    # Mutually exclusive with `defaults` and with declaring `limits` at the top-level of the spec.
    overrides:
      limits: {…}
```

## Using the RateLimitPolicy

### Targeting a HTTPRoute networking resource

When a RateLimitPolicy targets a HTTPRoute, the policy is enforced to all traffic routed according to the rules and hostnames specified in the HTTPRoute, across all Gateways referenced in the `spec.parentRefs` field of the HTTPRoute.

The targeted HTTPRoute's rules and/or hostnames to which the policy must be enforced can be filtered to specific subsets, by specifying the [`routeSelectors`](reference/route-selectors.md#the-routeselectors-field) field of the limit definition.

Target a HTTPRoute by setting the `spec.targetRef` field of the RateLimitPolicy as follows:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: <RateLimitPolicy name>
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: <HTTPRoute Name>
  limits: {…}
```

![Rate limit policy targeting a HTTPRoute resource](https://i.imgur.com/ObfOp9u.png)

#### Hostnames and wildcards

If a RateLimitPolicy targets a route defined for `*.com` and another RateLimitPolicy targets another route for `api.com`, the Kuadrant control plane will not merge these two RateLimitPolicies. Unless one of the policies declare an _overrides_ set of limites, the control plane will configure to mimic the behavior of gateway implementation by which the "most specific hostname wins", thus enforcing only the corresponding applicable policies and limit definitions.

E.g., by default, a request coming for `api.com` will be rate limited according to the rules from the RateLimitPolicy that targets the route for `api.com`; while a request for `other.com` will be rate limited with the rules from the RateLimitPolicy targeting the route for `*.com`.

See more examples in [Overlapping Gateway and HTTPRoute RateLimitPolicies](#overlapping-gateway-and-httproute-ratelimitpolicies).

### Targeting a Gateway networking resource

A RateLimitPolicy that targets a Gateway can declare a block of _defaults_ (`spec.defaults`) or a block of _overrides_ (`spec.overrides`). As a standard, gateway policies that do not specify neither defaults nor overrides, act as defaults.

When declaring _defaults_, a RateLimitPolicy which targets a Gateway will be enforced to all HTTP traffic hitting the gateway, unless a more specific RateLimitPolicy targeting a matching HTTPRoute exists. Any new HTTPRoute referrencing the gateway as parent will be automatically covered by the default RateLimitPolicy, as well as changes in the existing HTTPRoutes.

_Defaults_ provide cluster operators with the ability to protect the infrastructure against unplanned and malicious network traffic attempt, such as by setting safe default limits on hostnames and hostname wildcards.

Inversely, a gateway policy that specify _overrides_ declares a set of rules to be enforced on _all routes attached to the gateway_, thus atomically replacing any more specific policy occasionally attached to any of those routes.

Target a Gateway HTTPRoute by setting the `spec.targetRef` field of the RateLimitPolicy as follows:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: <RateLimitPolicy name>
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: <Gateway Name>
  defaults: # alternatively: `overrides`
    limits: {…}
```

![rate limit policy targeting a Gateway resource](https://i.imgur.com/UkivAqA.png)

#### Overlapping Gateway and HTTPRoute RateLimitPolicies

Two possible semantics are to be considered here – gateway policy _defaults_ vs gateway policy _overrides_.

Gateway RateLimitPolicies that declare _defaults_ (or alternatively neither defaults nor overrides) protect all traffic routed through the gateway except where a more specific HTTPRoute RateLimitPolicy exists, in which case the HTTPRoute RateLimitPolicy prevails.

Example with 4 RateLimitPolicies, 3 HTTPRoutes and 1 Gateway _default_ (plus 2 HTTPRoute and 2 Gateways without RateLimitPolicies attached):
- RateLimitPolicy A → HTTPRoute A (`a.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy B → HTTPRoute B (`b.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy W → HTTPRoute W (`*.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy G (defaults) → Gateway G (`*.com`)

Expected behavior:
- Request to `a.toystore.com` → RateLimitPolicy A will be enforced
- Request to `b.toystore.com` → RateLimitPolicy B will be enforced
- Request to `other.toystore.com` → RateLimitPolicy W will be enforced
- Request to `other.com` (suppose a route exists) → RateLimitPolicy G will be enforced
- Request to `yet-another.net` (suppose a route and gateway exist) → No RateLimitPolicy will be enforced

Gateway RateLimitPolicies that declare _overrides_ protect all traffic routed through the gateway, regardless of existence of any more specific HTTPRoute RateLimitPolicy.

Example with 4 RateLimitPolicies, 3 HTTPRoutes and 1 Gateway _override_ (plus 2 HTTPRoute and 2 Gateways without RateLimitPolicies attached):
- RateLimitPolicy A → HTTPRoute A (`a.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy B → HTTPRoute B (`b.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy W → HTTPRoute W (`*.toystore.com`) → Gateway G (`*.com`)
- RateLimitPolicy G (overrides) → Gateway G (`*.com`)

Expected behavior:
- Request to `a.toystore.com` → RateLimitPolicy G will be enforced
- Request to `b.toystore.com` → RateLimitPolicy G will be enforced
- Request to `other.toystore.com` → RateLimitPolicy G will be enforced
- Request to `other.com` (suppose a route exists) → RateLimitPolicy G will be enforced
- Request to `yet-another.net` (suppose a route and gateway exist) → No RateLimitPolicy will be enforced

### Limit definition

A limit will be activated whenever a request comes in and the request matches:
- any of the route rules selected by the limit (via [`routeSelectors`](reference/route-selectors.md#the-routeselectors-field) or implicit "catch-all" selector), and
- all of the `when` conditions specified in the limit.

A limit can define:
- counters that are qualified based on dynamic values fetched from the request, or
- global counters (implicitly, when no qualified counter is specified)

A limit is composed of one or more rate limits.

E.g.

```yaml
spec:
  limits:
    "toystore-all":
      rates:
      - limit: 5000
        duration: 1
        unit: second

    "toystore-api-per-username":
      rates:
      - limit: 100
        duration: 1
        unit: second
      - limit: 1000
        duration: 1
        unit: minute
      counters:
      - auth.identity.username
      routeSelectors:
        hostnames:
        - api.toystore.com

    "toystore-admin-unverified-users":
      rates:
      - limit: 250
        duration: 1
        unit: second
      routeSelectors:
        hostnames:
        - admin.toystore.com
      when:
      - selector: auth.identity.email_verified
        operator: eq
        value: "false"
```

| Request to           | Rate limits enforced                                         |
|----------------------|--------------------------------------------------------------|
| `api.toystore.com`   | 100rps/username or 1000rpm/username (whatever happens first) |
| `admin.toystore.com` | 250rps                                                       |
| `other.toystore.com` | 5000rps                                                      |

### Route selectors

Route selectors allow targeting sections of a HTTPRoute, by specifying sets of HTTPRouteMatches and/or hostnames that make the policy controller look up within the HTTPRoute spec for compatible declarations, and select the corresponding HTTPRouteRules and hostnames, to then build conditions that activate the policy or policy rule.

Check out [Route selectors](reference/route-selectors.md) for a full description, semantics and API reference.

#### `when` conditions

`when` conditions can be used to scope a limit (i.e. to filter the traffic to which a limit definition applies) without any coupling to the underlying network topology, i.e. without making direct references to HTTPRouteRules via [`routeSelectors`](reference/route-selectors.md#the-routeselectors-field).

Use `when` conditions to conditionally activate limits based on attributes that cannot be expressed in the HTTPRoutes' `spec.hostnames` and `spec.rules.matches` fields, or in general in RateLimitPolicies that target a Gateway.

The selectors within the `when` conditions of a RateLimitPolicy are a subset of Kuadrant's Well-known Attributes ([RFC 0002](https://github.com/Kuadrant/architecture/blob/main/rfcs/0002-well-known-attributes.md)). Check out the reference for the full list of supported selectors.

### Examples

Check out the following user guides for examples of rate limiting services with Kuadrant:
* [Simple Rate Limiting for Application Developers](user-guides/simple-rl-for-app-developers.md)
* [Authenticated Rate Limiting for Application Developers](user-guides/authenticated-rl-for-app-developers.md)
* [Gateway Rate Limiting for Cluster Operators](user-guides/gateway-rl-for-cluster-operators.md)
* [Authenticated Rate Limiting with JWTs and Kubernetes RBAC](user-guides/authenticated-rl-with-jwt-and-k8s-authnz.md)

### Known limitations

* One HTTPRoute can only be targeted by one RateLimitPolicy.
* One Gateway can only be targeted by one RateLimitPolicy.
* RateLimitPolicies can only target HTTPRoutes/Gateways defined within the same namespace of the RateLimitPolicy.
* 2+ RateLimitPolicies cannot target network resources that define/inherit the same exact hostname.

#### Limitation: Multiple network resources with identical hostnames

Kuadrant currently does not support multiple RateLimitPolicies simultaneously targeting network resources that declare identical hostnames. This includes multiple HTTPRoutes that specify the same hostnames in the `spec.hostnames` field, as well as HTTPRoutes that specify a hostname that is identical to a hostname specified in a listener of one of the route's parent gateways or HTTPRoutes that don't specify any hostname at all thus inheriting the hostnames from the parent gateways. In any of these cases, **a maximum of one RateLimitPolicy targeting any of those resources that specify identical hostnames is allowed**.

Moreover, having **multiple resources that declare identical hostnames** may lead to unexpected behavior and therefore **should be avoided**.

This limitation is rooted at the underlying components configured by Kuadrant for the implementation of its policies and the lack of information in the data plane regarding the exact route that honored by the API gateway in cases of conflicting hostnames.

To exemplify one way this limitation can impact deployments, consider the following topology:

```
                 ┌──────────────┐
                 │   Gateway    │
                 ├──────────────┤
          ┌─────►│ listeners:   │◄──────┐
          │      │ - host: *.io │       │
          │      └──────────────┘       │
          │                             │
          │                             │
┌─────────┴─────────┐        ┌──────────┴────────┐
│     HTTPRoute     │        │     HTTPRoute     │
│     (route-a)     │        │     (route-b)     │
├───────────────────┤        ├───────────────────┤
│ hostnames:        │        │ hostnames:        │
│ - app.io          │        │ - app.io          │
│ rules:            │        │ rules:            │
│ - matches:        │        │ - matches:        │
│   - path:         │        │   - path:         │
│       value: /foo │        │       value: /bar │
└───────────────────┘        └───────────────────┘
          ▲                            ▲
          │                            │
 ┌────────┴────────┐           ┌───────┴─────────┐
 │ RateLimitPolicy │           │ RateLimitPolicy │
 │   (policy-1)    │           │   (policy-2)    │
 └─────────────────┘           └─────────────────┘
```

In the example above, with the `policy-1` resource created before `policy-2`, `policy-2` will be enforced on all requests to `app.io/bar` while `policy-1` will **not** be enforced at all. I.e. `app.io/foo` will not be rate-limited. Nevertheless, both policies will report status condition as `Enforced`.

Notice the enforcement of `policy-2` and no enforcement of `policy-1` is the opposite behavior as the [analogous problem with the Kuadrant AuthPolicy](auth.md#limitation-multiple-network-resources-with-identical-hostnames).

A different way the limitation applies is when two or more routes of a gateway declare the exact same hostname and a gateway policy is defined with expectation to set default rules for the cases not covered by more specific policies. E.g.:

```
                                    ┌─────────────────┐
                         ┌──────────┤ RateLimitPolicy │
                         │          │    (policy-2)   │
                         ▼          └─────────────────┘
                 ┌──────────────┐
                 │   Gateway    │
                 ├──────────────┤
          ┌─────►│ listeners:   │◄──────┐
          │      │ - host: *.io │       │
          │      └──────────────┘       │
          │                             │
          │                             │
┌─────────┴─────────┐        ┌──────────┴────────┐
│     HTTPRoute     │        │     HTTPRoute     │
│     (route-a)     │        │     (route-b)     │
├───────────────────┤        ├───────────────────┤
│ hostnames:        │        │ hostnames:        │
│ - app.io          │        │ - app.io          │
│ rules:            │        │ rules:            │
│ - matches:        │        │ - matches:        │
│   - path:         │        │   - path:         │
│       value: /foo │        │       value: /bar │
└───────────────────┘        └───────────────────┘
          ▲
          │
 ┌────────┴────────┐
 │ RateLimitPolicy │
 │   (policy-1)    │
 └─────────────────┘
```

Once again, both policies will report status condition as `Enforced`. However, in this case, only `policy-1` will be enforced on requests to `app.io/foo`, while `policy-2` will **not** be enforced at all. I.e. `app.io/bar` will not be not rate-limited. This is same behavior as the [analogous problem with the Kuadrant AuthPolicy](auth.md#limitation-multiple-network-resources-with-identical-hostnames).

To avoid these problems, use different hostnames in each route.

## Implementation details

Driven by limitations related to how Istio injects configuration in the filter chains of the ingress gateways, Kuadrant relies on Envoy's [Wasm Network](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/network_filters/wasm_filter) filter in the data plane, to manage the integration with rate limiting service ("Limitador"), instead of the [Rate Limit](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter) filter.

**Motivation:** _Multiple rate limit domains_<br/>
The first limitation comes from having only one filter chain per listener. This often leads to one single global rate limiting filter configuration per gateway, and therefore to a shared rate limit [domain](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/ratelimit/v3/rate_limit.proto#envoy-v3-api-msg-extensions-filters-http-ratelimit-v3-ratelimit) across applications and policies. Even though, in a rate limit filter, the triggering of rate limit calls, via [actions to build so-called "descriptors"](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter#composing-actions), can be defined at the level of the virtual host and/or specific route rule, the overall rate limit configuration is only one, i.e., always the same rate limit domain for all calls to Limitador.

On the other hand, the possibility to configure and invoke the rate limit service for multiple domains depending on the context allows to isolate groups of policy rules, as well as to optimize performance in the rate limit service, which can rely on the domain for indexation.

**Motivation:** _Fine-grained matching rules_<br/>
A second limitation of configuring the rate limit filter via Istio, particularly from [Gateway API](https://gateway-api.sigs.k8s.io) resources, is that [rate limit descriptors](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter#composing-actions) at the level of a specific HTTP route rule require "named routes" – defined only in an Istio [VirtualService](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRoute) resource and referred in an [EnvoyFilter](https://istio.io/latest/docs/reference/config/networking/envoy-filter/#EnvoyFilter-RouteConfigurationMatch-RouteMatch) one. Because Gateway API HTTPRoute rules lack a "name" property[^1], as well as the Istio VirtualService resources are only ephemeral data structures handled by Istio in-memory in its implementation of gateway configuration for Gateway API, where the names of individual route rules are auto-generated and not referable by users in a policy[^2][^3], rate limiting by attributes of the HTTP request (e.g., path, method, headers, etc) would be very limited while depending only on Envoy's [Rate Limit](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter) filter.

[^1]: https://github.com/kubernetes-sigs/gateway-api/pull/996
[^2]: https://github.com/istio/istio/issues/36790
[^3]: https://github.com/istio/istio/issues/37346

Motivated by the desire to support multiple rate limit domains per ingress gateway, as well as fine-grained HTTP route matching rules for rate limiting, Kuadrant implements a [wasm-shim](https://github.com/Kuadrant/wasm-shim) that handles the rules to invoke the rate limiting service, complying with Envoy's [Rate Limit Service (RLS)](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ratelimit/v3/rls.proto) protocol.

The wasm module integrates with the gateway in the data plane via [Wasm Network](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/network_filters/wasm_filter) filter, and parses a configuration composed out of user-defined RateLimitPolicy resources by the Kuadrant control plane. Whereas the rate limiting service ("Limitador") remains an implementation of Envoy's RLS protocol, capable of being integrated directly via [Rate Limit](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/ratelimit/v3/rate_limit.proto#extension-envoy-filters-network-ratelimit) extension or by Kuadrant, via wasm module for the [Istio Gateway API implementation](https://gateway-api.sigs.k8s.io/implementations/#istio).

As a consequence of this design:
- Users can define fine-grained rate limit rules that match their Gateway and HTTPRoute definitions including for subsections of these.
- Rate limit definitions are insulated, not leaking across unrelated policies or applications.
- Conditions to activate limits are evaluated in the context of the gateway process, reducing the gRPC calls to the external rate limiting service only to the cases where rate limit counters are known in advance to have to be checked/incremented.
- The rate limiting service can rely on the indexation to look up for groups of limit definitions and counters.
- Components remain compliant with industry protocols and flexible for different integration options.

A Kuadrant wasm-shim configuration for 2 RateLimitPolicy custom resources (a Gateway default RateLimitPolicy and a HTTPRoute RateLimitPolicy) looks like the following and it is generated automatically by the Kuadrant control plane:

```yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: kuadrant-istio-ingressgateway
  namespace: istio-system
  …
spec:
  phase: STATS
  pluginConfig:
    failureMode: deny
    rateLimitPolicies:
    - domain: istio-system/gw-rlp # allows isolating policy rules and improve performance of the rate limit service
      hostnames:
      - '*.website'
      - '*.io'
      name: istio-system/gw-rlp
      rules: # match rules from the gateway and according to conditions specified in the policy
      - conditions:
        - allOf:
          - operator: startswith
            selector: request.url_path
            value: /
        data:
        - static: # tells which rate limit definitions and counters to activate
            key: limit.internet_traffic_all__593de456
            value: "1"
      - conditions:
        - allOf:
          - operator: startswith
            selector: request.url_path
            value: /
          - operator: endswith
            selector: request.host
            value: .io
        data:
        - static:
            key: limit.internet_traffic_apis_per_host__a2b149d2
            value: "1"
        - selector:
            selector: request.host
      service: kuadrant-rate-limiting-service
    - domain: default/app-rlp
      hostnames:
      - '*.toystore.website'
      - '*.toystore.io'
      name: default/app-rlp
      rules: # matches rules from a httproute and additional specified in the policy
      - conditions:
        - allOf:
          - operator: startswith
            selector: request.url_path
            value: /assets/
        data:
        - static:
            key: limit.toystore_assets_all_domains__8cfb7371
            value: "1"
      - conditions:
        - allOf:
          - operator: startswith
            selector: request.url_path
            value: /v1/
          - operator: eq
            selector: request.method
            value: GET
          - operator: endswith
            selector: request.host
            value: .toystore.website
          - operator: eq
            selector: auth.identity.username
            value: ""
        - allOf:
          - operator: startswith
            selector: request.url_path
            value: /v1/
          - operator: eq
            selector: request.method
            value: POST
          - operator: endswith
            selector: request.host
            value: .toystore.website
          - operator: eq
            selector: auth.identity.username
            value: ""
        data:
        - static:
            key: limit.toystore_v1_website_unauthenticated__3f9c40c6
            value: "1"
      service: kuadrant-rate-limiting-service
  selector:
    matchLabels:
      istio.io/gateway-name: istio-ingressgateway
  url: oci://quay.io/kuadrant/wasm-shim:v0.3.0
```
