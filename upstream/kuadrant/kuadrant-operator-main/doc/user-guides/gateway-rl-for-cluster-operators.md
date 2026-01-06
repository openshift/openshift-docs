# Gateway Rate Limiting for Cluster Operators

This user guide walks you through an example of how to configure rate limiting for all routes attached to an ingress gateway.

<br/>

## Run the steps ① → ⑤

### ① Setup

This step uses tooling from the Kuadrant Operator component to create a containerized Kubernetes server locally using [Kind](https://kind.sigs.k8s.io),
where it installs Istio, Kubernetes Gateway API and Kuadrant itself.

> **Note:** In production environment, these steps are usually performed by a cluster operator with administrator privileges over the Kubernetes cluster.

Clone the project:

```sh
git clone https://github.com/Kuadrant/kuadrant-operator && cd kuadrant-operator
```

Setup the environment:

```sh
make local-setup
```

Request an instance of Kuadrant:

```sh
kubectl -n kuadrant-system apply -f - <<EOF
apiVersion: kuadrant.io/v1beta1
kind: Kuadrant
metadata:
  name: kuadrant
spec: {}
EOF
```

### ② Create the ingress gateways

```sh
kubectl -n istio-system apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: external
  annotations:
    kuadrant.io/namespace: kuadrant-system
    networking.istio.io/service-type: ClusterIP
spec:
  gatewayClassName: istio
  listeners:
  - name: external
    port: 80
    protocol: HTTP
    hostname: '*.io'
    allowedRoutes:
      namespaces:
        from: All
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: internal
  annotations:
    kuadrant.io/namespace: kuadrant-system
    networking.istio.io/service-type: ClusterIP
spec:
  gatewayClassName: istio
  listeners:
  - name: local
    port: 80
    protocol: HTTP
    hostname: '*.local'
    allowedRoutes:
      namespaces:
        from: All
EOF
```

### ③ Enforce rate limiting on requests incoming through the `external` gateway

```
    ┌───────────┐      ┌───────────┐
    │ (Gateway) │      │ (Gateway) │
    │  external │      │  internal │
    │           │      │           │
    │   *.io    │      │  *.local  │
    └───────────┘      └───────────┘
          ▲
          │
┌─────────┴─────────┐
│ (RateLimitPolicy) │
│       gw-rlp      │
└───────────────────┘
```

Create a Kuadrant `RateLimitPolicy` to configure rate limiting:

```sh
kubectl apply -n istio-system -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: gw-rlp
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: external
  limits:
    "global":
      rates:
      - limit: 5
        duration: 10
        unit: second
EOF
```

> **Note:** It may take a couple of minutes for the RateLimitPolicy to be applied depending on your cluster.

### ④ Deploy a sample API to test rate limiting enforced at the level of the gateway

```
                           ┌───────────┐      ┌───────────┐
┌───────────────────┐      │ (Gateway) │      │ (Gateway) │
│ (RateLimitPolicy) │      │  external │      │  internal │
│       gw-rlp      ├─────►│           │      │           │
└───────────────────┘      │   *.io    │      │  *.local  │
                           └─────┬─────┘      └─────┬─────┘
                                 │                  │
                                 └─────────┬────────┘
                                           │
                                 ┌─────────┴────────┐
                                 │   (HTTPRoute)    │
                                 │     toystore     │
                                 │                  │
                                 │ *.toystore.io    │
                                 │ *.toystore.local │
                                 └────────┬─────────┘
                                          │
                                   ┌──────┴───────┐
                                   │   (Service)  │
                                   │   toystore   │
                                   └──────────────┘
```

Deploy the sample API:

```sh
kubectl apply -f examples/toystore/toystore.yaml
```

Route traffic to the API from both gateways:

```sh
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: toystore
spec:
  parentRefs:
  - name: external
    namespace: istio-system
  - name: internal
    namespace: istio-system
  hostnames:
  - "*.toystore.io"
  - "*.toystore.local"
  rules:
  - backendRefs:
    - name: toystore
      port: 80
EOF
```

### ⑤ Verify the rate limiting works by sending requests in a loop

Expose the gateways, respectively at the port numbers `9081` and `9082` of the local host:

```sh
kubectl port-forward -n istio-system service/external-istio 9081:80 2>&1 >/dev/null &
kubectl port-forward -n istio-system service/internal-istio 9082:80 2>&1 >/dev/null &
```

Up to 5 successful (`200 OK`) requests every 10 seconds through the `external` ingress gateway (`*.io`), then `429 Too Many Requests`:

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H 'Host: api.toystore.io' http://localhost:9081 | grep -E --color "\b(429)\b|$"; sleep 1; done
```

Unlimited successful (`200 OK`) through the `internal` ingress gateway (`*.local`):

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H 'Host: api.toystore.local' http://localhost:9082 | grep -E --color "\b(429)\b|$"; sleep 1; done
```

## Cleanup

```sh
make local-cleanup
```
