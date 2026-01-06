# Gateway DNS for Cluster Operators

This user guide walks you through an example of how to configure DNS for all routes attached to an ingress gateway.

<br/>

## Requisites

- [Docker](https://docker.io)
- [Rout53 Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html)

### Setup

This step uses tooling from the Kuadrant Operator component to create a containerized Kubernetes server locally using [Kind](https://kind.sigs.k8s.io),
where it installs Istio, Kubernetes Gateway API and Kuadrant itself.

Clone the project:

```shell
git clone https://github.com/Kuadrant/kuadrant-operator && cd kuadrant-operator
```

Setup the environment:

```shell
make local-setup
```

Create a namespace:
```shell
kubectl create namespace my-gateways
```

Export a root domain and hosted zone id:
```shell
export ROOT_DOMAIN=<ROOT_DOMAIN>
export AWS_HOSTED_ZONE_ID=<AWS_HOSTED_ZONE_ID>
```

> **Note:** ROOT_DOMAIN and AWS_HOSTED_ZONE_ID should be set to your AWS hosted zone *name* and *id* respectively.

### Create a ManagedZone

Create AWS credentials secret
```shell
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

kubectl -n my-gateways create secret generic aws-credentials \
  --type=kuadrant.io/aws \
  --from-literal=AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  --from-literal=AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
```

Create a ManagedZone
```sh
kubectl -n my-gateways apply -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: ManagedZone
metadata:
  name: $ROOT_DOMAIN
spec:
  id: $AWS_HOSTED_ZONE_ID
  domainName: $ROOT_DOMAIN
  description: "my managed zone"
  dnsProviderSecretRef:
    name: aws-credentials
EOF
```

Check it's ready
```shell
kubectl get managedzones -n my-gateways
```

### Create an ingress gateway

Create a gateway using your ROOT_DOMAIN as part of a listener hostname:
```sh
kubectl -n my-gateways apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-web
spec:
  gatewayClassName: istio
  listeners:
    - allowedRoutes:
        namespaces:
          from: All
      name: api
      hostname: "*.$ROOT_DOMAIN"
      port: 80
      protocol: HTTP
EOF
```

Check gateway status:
```shell
kubectl get gateway prod-web -n my-gateways
```
Response:
```shell
NAME       CLASS   ADDRESS        PROGRAMMED   AGE
prod-web   istio   172.18.200.1   True         25s
```

### Enable DNS on the gateway

Create a Kuadrant `DNSPolicy` to configure DNS:
```shell
kubectl -n my-gateways apply -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: DNSPolicy
metadata:
  name: prod-web
spec:
  targetRef:
    name: prod-web
    group: gateway.networking.k8s.io
    kind: Gateway
  routingStrategy: simple
EOF
```

Check policy status:
```shell
kubectl get dnspolicy -o wide -n my-gateways
```
Response:
```shell
NAME       STATUS     TARGETREFKIND   TARGETREFNAME   AGE
prod-web   Accepted   Gateway         prod-web        26s
```

### Deploy a sample API to test DNS

Deploy the sample API:
```shell
kubectl -n my-gateways apply -f examples/toystore/toystore.yaml
kubectl -n my-gateways wait --for=condition=Available deployments toystore --timeout=60s
```

Route traffic to the API from our gateway:
```shell
kubectl -n my-gateways apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: toystore
spec:
  parentRefs:
  - name: prod-web
    namespace: my-gateways
  hostnames:
  - "*.$ROOT_DOMAIN"
  rules:
  - backendRefs:
    - name: toystore
      port: 80
EOF
```

Verify a DNSRecord resource is created:
```shell
kubectl get dnsrecords -n my-gateways
NAME           READY
prod-web-api   True
```

### Verify DNS works by sending requests

Verify DNS using dig:
```shell
dig foo.$ROOT_DOMAIN +short
```
Response:
```shell
172.18.200.1
```

Verify DNS using curl:

```shell
curl http://api.$ROOT_DOMAIN
```
Response:
```shell
{
  "method": "GET",
  "path": "/",
  "query_string": null,
  "body": "",
  "headers": {
    "HTTP_HOST": "api.$ROOT_DOMAIN",
    "HTTP_USER_AGENT": "curl/7.85.0",
    "HTTP_ACCEPT": "*/*",
    "HTTP_X_FORWARDED_FOR": "10.244.0.1",
    "HTTP_X_FORWARDED_PROTO": "http",
    "HTTP_X_ENVOY_INTERNAL": "true",
    "HTTP_X_REQUEST_ID": "9353dd3d-0fe5-4404-86f4-a9732a9c119c",
    "HTTP_X_ENVOY_DECORATOR_OPERATION": "toystore.my-gateways.svc.cluster.local:80/*",
    "HTTP_X_ENVOY_PEER_METADATA": "ChQKDkFQUF9DT05UQUlORVJTEgIaAAoaCgpDTFVTVEVSX0lEEgwaCkt1YmVybmV0ZXMKHQoMSU5TVEFOQ0VfSVBTEg0aCzEwLjI0NC4wLjIyChkKDUlTVElPX1ZFUlNJT04SCBoGMS4xNy4yCtcBCgZMQUJFTFMSzAEqyQEKIwoVaXN0aW8uaW8vZ2F0ZXdheS1uYW1lEgoaCHByb2Qtd2ViChkKDGlzdGlvLmlvL3JldhIJGgdkZWZhdWx0CjMKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSEBoOcHJvZC13ZWItaXN0aW8KLwojc2VydmljZS5pc3Rpby5pby9jYW5vbmljYWwtcmV2aXNpb24SCBoGbGF0ZXN0CiEKF3NpZGVjYXIuaXN0aW8uaW8vaW5qZWN0EgYaBHRydWUKGgoHTUVTSF9JRBIPGg1jbHVzdGVyLmxvY2FsCigKBE5BTUUSIBoecHJvZC13ZWItaXN0aW8tYzU0NWQ4ZjY4LTdjcjg2ChoKCU5BTUVTUEFDRRINGgtteS1nYXRld2F5cwpWCgVPV05FUhJNGktrdWJlcm5ldGVzOi8vYXBpcy9hcHBzL3YxL25hbWVzcGFjZXMvbXktZ2F0ZXdheXMvZGVwbG95bWVudHMvcHJvZC13ZWItaXN0aW8KFwoRUExBVEZPUk1fTUVUQURBVEESAioACiEKDVdPUktMT0FEX05BTUUSEBoOcHJvZC13ZWItaXN0aW8=",
    "HTTP_X_ENVOY_PEER_METADATA_ID": "router~10.244.0.22~prod-web-istio-c545d8f68-7cr86.my-gateways~my-gateways.svc.cluster.local",
    "HTTP_X_ENVOY_ATTEMPT_COUNT": "1",
    "HTTP_X_B3_TRACEID": "d65f580db9c6a50c471cdb534771c61a",
    "HTTP_X_B3_SPANID": "471cdb534771c61a",
    "HTTP_X_B3_SAMPLED": "0",
    "HTTP_VERSION": "HTTP/1.1"
  },
  "uuid": "0ecb9f84-db30-4289-a3b8-e22d4021122f"
}
```

## Cleanup

```shell
make local-cleanup
```
