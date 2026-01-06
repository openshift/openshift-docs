# Simple Rate Limiting for Application Developers

This user guide walks you through an example of how to configure rate limiting for an endpoint of an application using Kuadrant.

<br/>

In this guide, we will rate limit a sample REST API called **Toy Store**. In reality, this API is just an echo service that echoes back to the user whatever attributes it gets in the request. The API listens to requests at the hostname `api.toystore.com`, where it exposes the endpoints `GET /toys*` and `POST /toys`, respectively, to mimic a operations of reading and writing toy records.

We will rate limit the `POST /toys` endpoint to a maximum of 5rp10s ("5 requests every 10 seconds").

<br/>

## Run the steps ① → ③

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

### ② Deploy the Toy Store API

Create the deployment:

```sh
kubectl apply -f examples/toystore/toystore.yaml
```

Create a HTTPRoute to route traffic to the service via Istio Ingress Gateway:

![](https://i.imgur.com/rdN8lo3.png)

```sh
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
        value: "/toys"
    backendRefs:
    - name: toystore
      port: 80
  - matches: # it has to be a separate HTTPRouteRule so we do not rate limit other endpoints
    - method: POST
      path:
        type: Exact
        value: "/toys"
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

Verify the route works:

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/toys -i
# HTTP/1.1 200 OK
```

> **Note**: If the command above fails to hit the Toy Store API on your environment, try forwarding requests to the service and accessing over localhost:
>
> ```sh
> kubectl port-forward -n istio-system service/istio-ingressgateway-istio 9080:80 2>&1 >/dev/null &
> export GATEWAY_URL=localhost:9080
> ```
> ```sh
> curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/toys -i
> # HTTP/1.1 200 OK
> ```

### ③ Enforce rate limiting on requests to the Toy Store API

Create a Kuadrant `RateLimitPolicy` to configure rate limiting:

![](https://i.imgur.com/2A9sXXs.png)

```sh
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: toystore
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: toystore
  limits:
    "create-toy":
      rates:
      - limit: 5
        duration: 10
        unit: second
      routeSelectors:
      - matches: # selects the 2nd HTTPRouteRule of the targeted route
        - method: POST
          path:
            type: Exact
            value: "/toys"
EOF
```

> **Note:** It may take a couple of minutes for the RateLimitPolicy to be applied depending on your cluster.

<br/>

Verify the rate limiting works by sending requests in a loop.

Up to 5 successful (`200 OK`) requests every 10 seconds to `POST /toys`, then `429 Too Many Requests`:

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H 'Host: api.toystore.com' http://$GATEWAY_URL/toys -X POST | grep -E --color "\b(429)\b|$"; sleep 1; done
```

Unlimited successful (`200 OK`) to `GET /toys`:

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H 'Host: api.toystore.com' http://$GATEWAY_URL/toys | grep -E --color "\b(429)\b|$"; sleep 1; done
```

## Cleanup

```sh
make local-cleanup
```
