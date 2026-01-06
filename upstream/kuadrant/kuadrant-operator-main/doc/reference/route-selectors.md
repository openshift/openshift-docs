# Route selectors

The route selectors of a policy spec or policy rule (limit definition or auth rule) allow to specify **selectors of routes** or parts of a route, that _transitively induce a set of conditions for a policy or policy rule to be enforced_. It is defined as a set of HTTP route matching rules, where these matching rules must exist, partially or identically stated within the HTTPRouteRules of the HTTPRoute that is targeted by the policy.

## The `routeSelectors` field

The `routeSelectors` field can be found in policy specs and policy rules (limit definition or auth rule).

| **Field**        | **Type**                          | **Required** | **Description**                                                                                      |
|------------------|-----------------------------------|:------------:|------------------------------------------------------------------------------------------------------|
| `routeSelectors` | [][RouteSelector](#routeselector) | No           | List of route selectors of HTTPRouteRules whose HTTPRouteMatches activate the policy or policy rule. |

### RouteSelector

Each `RouteSelector` is an object composed of a set of [HTTPRouteMatch](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.HTTPPathMatch) objects (from Gateway API), and an additional `hostnames` field.

| **Field**   | **Type**                                                                                                                       | **Required** | **Description**                                                                             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|:------------:|---------------------------------------------------------------------------------------------|
| `matches`   | [][HTTPRouteMatch](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.HTTPRouteMatch) | No           | List of selectors of HTTPRouteRules whose matching rules activate the policy or policy rule |
| `hostnames` | [][Hostname](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.Hostname)             | No           | List of hostnames of the HTTPRoute that activate the policy or policy rule                  |

## Mechanics of the route selectors

Route selectors matches and the HTTPRoute's HTTPRouteMatches are pairwise compared to select or not select HTTPRouteRules that should activate a policy rule. To decide whether the route selector selects a HTTPRouteRule or not, for each pair of route selector HTTPRouteMatch and HTTPRoute HTTPRouteMatch:
1. The route selector selects the HTTPRoute's HTTPRouteRule if the HTTPRouteRule contains at least one HTTPRouteMatch that specifies fields that are literally identical to all the fields specified by at least one HTTPRouteMatch of the route selector.
2. A HTTPRouteMatch within a HTTPRouteRule may include other fields that are not specified in a route selector match, and yet the route selector match selects the HTTPRouteRule if all fields of the route selector match are identically included in the HTTPRouteRule's HTTPRouteMatch; the opposite is NOT true.
3. Each field `path` of a HTTPRouteMatch, as well as each field `method` of a HTTPRouteMatch, as well as each element of the fields `headers` and `queryParams` of a HTTPRouteMatch, is atomic – this is true for the HTTPRouteMatches within a HTTPRouteRule, as well as for HTTPRouteMatches of a route selector.

Additionally, at least one hostname specified in a route selector must identically match one of the hostnames specified (or inherited, when omitted) by the targeted HTTPRoute.

The semantics of the route selectors allows to assertively relate policy rule definitions to routing rules, with benefits for identifying the subsets of the network that are covered by a policy rule, while preventing unreachable definitions, as well as the overhead associated with the maintenance of such rules across multiple resources throughout time, according to network topology beneath. Moreover, the requirement of not having to be a full copy of the targeted HTTPRouteRule matches, but only partially identical, helps prevent repetition to some degree, as well as it enables to more easily define policy rules that scope across multiple HTTPRouteRules (by specifying less rules in the selector).

## Golden rules and corner cases

A few rules and corner cases to keep in mind while using the RLP's `routeSelectors`:
1. **The golden rule –** The route selectors in a policy or policy rule are **not** to be interpreted as the route matching rules that activate the policy or policy rule, but as **selectors of the route rules** that activate the policy or policy rule.
2. Due to (1) above, this can lead to cases, e.g., where a route selector that states `matches: [{ method: POST }]` selects a HTTPRouteRule that defines `matches: [{ method: POST },  { method: GET }]`, effectively causing the policy or policy rule to be activated on requests to the HTTP method `POST`, but **also** to the HTTP method `GET`.
3. The requirement for the route selector match to state patterns that are identical to the patterns stated by the HTTPRouteRule (partially or entirely) makes, e.g., a route selector such as `matches: { path: { type: PathPrefix, value: /foo } }` to select a HTTPRouteRule that defines `matches: { path: { type: PathPrefix, value: /foo }, method: GET }`, but **not** to select a HTTPRouteRule that only defines `matches: { method: GET }`, even though the latter includes technically all HTTP paths; **nor** it selects a HTTPRouteRule that only defines `matches: { path: { type: Exact, value: /foo } }`, even though all requests to the exact path `/foo` are also technically requests to `/foo*`.
4. The atomicity property of fields of the route selectors makes, e.g., a route selector such as `matches: { path: { value: /foo } }` to select a HTTPRouteRule that defines `matches: { path: { value: /foo } }`, but **not** to select a HTTPRouteRule that only defines `matches: { path: { type: PathPrefix, value: /foo } }`. (This case may actually never happen because `PathPrefix` is the default value for `path.type` and will be set automatically by the Kubernetes API server.)

Due to the nature of route selectors of defining pointers to HTTPRouteRules, the `routeSelectors` field is not supported in a RLP that targets a Gateway resource.
