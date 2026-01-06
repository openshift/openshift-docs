# Gateway TLS for Cluster Operators

This user guide walks you through an example of how to configure TLS for all routes attached to an ingress gateway.

<br/>

## Requisites

- [Docker](https://docker.io)

### Setup

This step uses tooling from the Kuadrant Operator component to create a containerized Kubernetes server locally using [Kind](https://kind.sigs.k8s.io),
where it installs Istio, Kubernetes Gateway API, CertManager and Kuadrant itself.

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

### Create an ingress gateway

Create a gateway:
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
      hostname: "*.toystore.local"
      port: 443
      protocol: HTTPS
      tls:
        mode: Terminate
        certificateRefs:
          - name: toystore-local-tls
            kind: Secret
EOF
```

### Enable TLS on the gateway

The TLSPolicy requires a reference to an existing [CertManager Issuer](https://cert-manager.io/docs/configuration/).

Create a CertManager Issuer:
```shell
kubectl apply -n my-gateways -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}
EOF
```

> **Note:** We are using a [self-signed](https://cert-manager.io/docs/configuration/selfsigned/) issuer here but any supported CerManager issuer or cluster issuer can be used.

```shell
kubectl get issuer selfsigned-issuer -n my-gateways
```
Response:
```shell
NAME                        READY   AGE
selfsigned-issuer   True    18s
```

Create a Kuadrant `TLSPolicy` to configure TLS:
```sh
kubectl apply -n my-gateways -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: TLSPolicy
metadata:
  name: prod-web
spec:
  targetRef:
    name: prod-web
    group: gateway.networking.k8s.io
    kind: Gateway
  issuerRef:
    group: cert-manager.io
    kind: Issuer
    name: selfsigned-issuer
EOF
```

Check policy status:
```shell
kubectl get tlspolicy -o wide -n my-gateways
```
Response:
```shell
NAME       STATUS     TARGETREFKIND   TARGETREFNAME   AGE
prod-web   Accepted   Gateway         prod-web        13s
```

Check a Certificate resource was created:
```shell
kubectl get certificates -n my-gateways
```
Response
```shell
NAME                 READY   SECRET               AGE
toystore-local-tls   True    toystore-local-tls   7m30s

```

Check a TLS Secret resource was created:
```shell
kubectl get secrets -n my-gateways --field-selector="type=kubernetes.io/tls"
```
Response:
```shell
NAME                 TYPE                DATA   AGE
toystore-local-tls   kubernetes.io/tls   3      7m42s
```

### Deploy a sample API to test TLS

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
  - "*.toystore.local"
  rules:
  - backendRefs:
    - name: toystore
      port: 80
EOF
```

### Verify TLS works by sending requests

Get the gateway address@
```shell
GWADDRESS=`kubectl get gateway/prod-web -n my-gateways -o=jsonpath='{.status.addresses[?(@.type=="IPAddress")].value}'`
echo $GWADDRESS
```
Response:
```shell
172.18.200.1
```

Verify we can access the service via TLS:
```shell
curl -vkI https://api.toystore.local --resolve "api.toystore.local:443:$GWADDRESS"
```
Response:
```shell
* Added api.toystore.local:443:172.18.200.1 to DNS cache
* Hostname api.toystore.local was found in DNS cache
*   Trying 172.18.200.1:443...
* Connected to api.toystore.local (172.18.200.1) port 443 (#0)
* ALPN: offers h2
* ALPN: offers http/1.1
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN: server accepted h2
* Server certificate:
*  subject: [NONE]
*  start date: Feb 15 11:46:50 2024 GMT
*  expire date: May 15 11:46:50 2024 GMT
* Using HTTP2, server supports multiplexing
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* h2h3 [:method: HEAD]
* h2h3 [:path: /]
* h2h3 [:scheme: https]
* h2h3 [:authority: api.toystore.local]
* h2h3 [user-agent: curl/7.85.0]
* h2h3 [accept: */*]
* Using Stream ID: 1 (easy handle 0x5623e4fe5bf0)
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
> HEAD / HTTP/2
> Host: api.toystore.local
> user-agent: curl/7.85.0
> accept: */*
> 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Connection state changed (MAX_CONCURRENT_STREAMS == 2147483647)!
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
< HTTP/2 200 
HTTP/2 200 
< content-type: application/json
content-type: application/json
< server: istio-envoy
server: istio-envoy
< date: Thu, 15 Feb 2024 12:13:27 GMT
date: Thu, 15 Feb 2024 12:13:27 GMT
< content-length: 1658
content-length: 1658
< x-envoy-upstream-service-time: 1
x-envoy-upstream-service-time: 1

< 
* Connection #0 to host api.toystore.local left intact
```

## Cleanup

```shell
make local-cleanup
```
