# Enforcing authentication & authorization with Kuadrant AuthPolicy

This guide walks you through the process of setting up a local Kubernetes cluster with Kuadrant where you will protect [Gateway API](https://gateway-api.sigs.k8s.io/) endpoints by declaring Kuadrant AuthPolicy custom resources.

Two AuthPolicies will be declared:

| Use case                       | AuthPolicy                                                                                                                                                                                                                                                                                |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **App developer**              | 1 AuthPolicy targeting a HTTPRoute that routes traffic to a sample Toy Store application, and enforces API key authentication to all requests in this route, as well as requires API key owners to be mapped to `groups:admins` metadata to access a specific HTTPRouteRule of the route. |
| **Platform engineer use-case** | 1 AuthPolicy targeting the `istio-ingressgateway` Gateway that enforces a trivial "deny-all" policy that locks down any other HTTPRoute attached to the Gateway.                                                                                                                          |

Topology:

```
                   ┌───────────────┐
                   │ (AuthPolicy)  │
                   │    gw-auth    │
                   └───────┬───────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     (Gateway)        │
                │ istio-ingressgateway │
          ┌────►│                      │◄───┐
          │     │          *           │    │
          │     └──────────────────────┘    │
          │                                 │
 ┌────────┴─────────┐              ┌────────┴─────────┐
 │   (HTTPRoute)    │              │   (HTTPRoute)    │
 │    toystore      │              │      other       │
 │                  │              │                  │
 │ api.toystore.com │              │ *.other-apps.com │
 └──────────────────┘              └──────────────────┘
          ▲
          │
  ┌───────┴───────┐
  │ (AuthPolicy)  │
  │    toystore   │
  └───────────────┘
```

## Requisites

- [Docker](https://docker.io)

## Run the guide ① → ④

### ①  Setup (Persona: _Cluster admin_)

Clone the repo:

```sh
git clone git@github.com:Kuadrant/kuadrant-operator.git && cd kuadrant-operator
```

Run the following command to create a local Kubernetes cluster with [Kind](https://kind.sigs.k8s.io/), install & deploy Kuadrant:

```sh
make local-setup
```

Request an instance of Kuadrant in the `kuadrant-system` namespace:

```sh
kubectl -n kuadrant-system apply -f - <<EOF
apiVersion: kuadrant.io/v1beta1
kind: Kuadrant
metadata:
  name: kuadrant
spec: {}
EOF
```

### ② Deploy the Toy Store sample application (Persona: _App developer_)

```sh
kubectl apply -f examples/toystore/toystore.yaml

kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: toystore
spec:
  parentRefs:
  - name: istio-ingressgateway
    namespace: istio-system
  hostnames:
  - api.toystore.com
  rules:
  - matches:
    - method: GET
      path:
        type: PathPrefix
        value: "/cars"
    - method: GET
      path:
        type: PathPrefix
        value: "/dolls"
    backendRefs:
    - name: toystore
      port: 80
  - matches:
    - path:
        type: PathPrefix
        value: "/admin"
    backendRefs:
    - name: toystore
      port: 80
EOF
```

Export the gateway hostname and port:

```sh
export INGRESS_HOST=$(kubectl get gtw istio-ingressgateway -n istio-system -o jsonpath='{.status.addresses[0].value}')
export INGRESS_PORT=$(kubectl get gtw istio-ingressgateway -n istio-system -o jsonpath='{.spec.listeners[?(@.name=="http")].port}')
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
```

Send requests to the application unprotected:

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/cars -i
# HTTP/1.1 200 OK
```

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/dolls -i
# HTTP/1.1 200 OK
```

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/admin -i
# HTTP/1.1 200 OK
```

### ③ Protect the Toy Store application (Persona: _App developer_)

Create the AuthPolicy to enforce the following auth rules:
- **Authentication:**
  - All users must present a valid API key
- **Authorization:**
  - `/admin*` routes require user mapped to the `admins` group (`kuadrant.io/groups=admins` annotation added to the Kubernetes API key Secret)

```sh
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: AuthPolicy
metadata:
  name: toystore
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: toystore
  rules:
    authentication:
      "api-key-authn":
        apiKey:
          selector: {}
        credentials:
          authorizationHeader:
            prefix: APIKEY
    authorization:
      "only-admins":
        opa:
          rego: |
            groups := split(object.get(input.auth.identity.metadata.annotations, "kuadrant.io/groups", ""), ",")
            allow { groups[_] == "admins" }
        routeSelectors:
        - matches:
          - path:
              type: PathPrefix
              value: "/admin"
EOF
```

Create the API keys:

```sh
kubectl apply -f -<<EOF
apiVersion: v1
kind: Secret
metadata:
  name: api-key-regular-user
  labels:
    authorino.kuadrant.io/managed-by: authorino
stringData:
  api_key: iamaregularuser
type: Opaque
---
apiVersion: v1
kind: Secret
metadata:
  name: api-key-admin-user
  labels:
    authorino.kuadrant.io/managed-by: authorino
  annotations:
    kuadrant.io/groups: admins
stringData:
  api_key: iamanadmin
type: Opaque
EOF
```

Send requests to the application protected by Kuadrant:

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/cars -i
# HTTP/1.1 401 Unauthorized
```

```sh
curl -H 'Host: api.toystore.com' -H 'Authorization: APIKEY iamaregularuser' http://$GATEWAY_URL/cars -i
# HTTP/1.1 200 OK
```

```sh
curl -H 'Host: api.toystore.com' -H 'Authorization: APIKEY iamaregularuser' http://$GATEWAY_URL/admin -i
# HTTP/1.1 403 Forbidden
```

```sh
curl -H 'Host: api.toystore.com' -H 'Authorization: APIKEY iamanadmin' http://$GATEWAY_URL/admin -i
# HTTP/1.1 200 OK
```

### ④ Create a default "deny-all" policy at the level of the gateway (Persona: _Platform engineer_)

Create the policy:

```sh
kubectl -n istio-system apply -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: AuthPolicy
metadata:
  name: gw-auth
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: istio-ingressgateway
  rules:
    authorization:
      deny-all:
        opa:
          rego: "allow = false"
    response:
      unauthorized:
        headers:
          "content-type":
            value: application/json
        body:
          value: |
            {
              "error": "Forbidden",
              "message": "Access denied by default by the gateway operator. If you are the administrator of the service, create a specific auth policy for the route."
            }
EOF
```

The policy won't be effective until there is at least one accepted route not yet protected by another more specific policy attached to it.

Create a route that will inherit the default policy attached to the gateway:

```sh
kubectl apply -f -<<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: other
spec:
  parentRefs:
  - name: istio-ingressgateway
    namespace: istio-system
  hostnames:
  - "*.other-apps.com"
EOF
```

Send requests to the route protected by the default policy set at the level of the gateway:

```sh
curl -H 'Host: foo.other-apps.com' http://$GATEWAY_URL/ -i
# HTTP/1.1 403 Forbidden
```

## Cleanup

```sh
make local-cleanup
```
