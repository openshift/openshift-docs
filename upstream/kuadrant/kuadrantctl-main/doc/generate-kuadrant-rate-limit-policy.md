## Generate Kuadrant RateLimitPolicy object from OpenAPI 3

The `kuadrantctl generate kuadrant ratelimitpolicy` command generates an [Kuadrant RateLimitPolicy](https://docs.kuadrant.io/kuadrant-operator/doc/rate-limiting/)
from your [OpenAPI Specification (OAS) 3.x](https://spec.openapis.org/oas/latest.html) powered with [kuadrant extensions](openapi-kuadrant-extensions.md).

### OpenAPI specification

An OpenAPI document resource can be provided to the cli by one of the following channels:

* Filename in the available path.
* URL format (supported schemes are HTTP and HTTPS). The CLI will try to download from the given address.
* Read from stdin standard input stream.

### Usage

```shell
Generate Kuadrant RateLimitPolicy from OpenAPI 3.0.X

Usage:
  kuadrantctl generate kuadrant ratelimitpolicy [flags]

Flags:
  -h, --help         help for ratelimitpolicy
  --oas string        Path to OpenAPI spec file (in JSON or YAML format), URL, or '-' to read from standard input (required)
  -o Output format:   'yaml' or 'json'. (default "yaml")

Global Flags:
  -v, --verbose   verbose output
```

> Under the example folder there are examples of OAS 3 that can be used to generate the resources

### User Guide

* Clone the repo 
```bash
git clone https://github.com/Kuadrant/kuadrantctl.git
cd kuadrantctl
```
* Setup a cluster, Istio and Gateway API CRDs and Kuadrant

Use our single-cluster quick start script - this will install Kuadrant in a local `kind` cluster: https://docs.kuadrant.io/getting-started-single-cluster/

* Build and install CLI in `bin/kuadrantctl` path
```bash
make install
```

* Deploy petstore backend API
```bash
kubectl create namespace petstore
kubectl apply -n petstore -f examples/petstore/petstore.yaml
```
* Let's create Petstore's OpenAPI spec

<details>

```yaml
cat <<EOF >petstore-openapi.yaml
---
openapi: "3.0.3"
info:
  title: "Pet Store API"
  version: "1.0.0"
x-kuadrant:
  route:
    name: "petstore"
    namespace: "petstore"
    hostnames:
      - example.com
    parentRefs:
      - name: istio-ingressgateway
        namespace: istio-system
servers:
  - url: https://example.io/v1
paths:
  /cat:
    x-kuadrant:  ## Path level Kuadrant Extension
      backendRefs:
        - name: petstore
          port: 80
          namespace: petstore
      rate_limit:
        rates:
          - limit: 1
            duration: 10
            unit: second
        counters:
          - request.headers.x-forwarded-for
    get:  # Added to the route and rate limited
      operationId: "getCat"
      responses:
        405:
          description: "invalid input"
    post:  # NOT added to the route
      x-kuadrant: 
        disable: true
      operationId: "postCat"
      responses:
        405:
          description: "invalid input"
  /dog:
    get:  # Added to the route and rate limited
      x-kuadrant:  ## Operation level Kuadrant Extension
        backendRefs:
          - name: petstore
            port: 80
            namespace: petstore
        rate_limit:
          rates:
            - limit: 3
              duration: 10
              unit: second
          counters:
            - request.headers.x-forwarded-for
      operationId: "getDog"
      responses:
        405:
          description: "invalid input"
    post:  # Added to the route and NOT rate limited
      x-kuadrant:  ## Operation level Kuadrant Extension
        backendRefs:
          - name: petstore
            port: 80
            namespace: petstore
      operationId: "postDog"
      responses:
        405:
          description: "invalid input"
EOF
```

</details>

> **NOTE**: `servers` base path not included. WIP in following up PRs.

| Operation | Applied config |
| --- | --- |
| `GET /cat` | It should return 200 Ok and be rate limited (1 req / 10 seconds)  |
| `POST /cat`  | Not added to the HTTPRoute. It should return 404 Not Found  |
| `GET /dog`  | It should return 200 Ok and be rate limited (3 req / 10 seconds) |
| `POST /dog`   | It should return 200 Ok and NOT rate limited  |


* Create the HTTPRoute using the CLI
```bash
bin/kuadrantctl generate gatewayapi httproute --oas petstore-openapi.yaml | kubectl apply -n petstore -f -
```

* Create the Rate Limit Policy
```bash
bin/kuadrantctl generate kuadrant ratelimitpolicy --oas petstore-openapi.yaml | kubectl apply -n petstore -f -
```

* Test OpenAPI endpoints
  * `GET /cat` -> It should return 200 Ok and be rate limited (1 req / 10 seconds)

```bash
curl --resolve example.com:9080:127.0.0.1 -v "http://example.com:9080/cat"
```
  *   `POST /cat` -> Not added to the HTTPRoute. It should return 404 Not Found
```bash
curl --resolve example.com:9080:127.0.0.1 -v -X POST "http://example.com:9080/cat"
```
  * `GET /dog` -> It should return 200 Ok and be rate limited (3 req / 10 seconds)

```bash
curl --resolve example.com:9080:127.0.0.1 -v "http://example.com:9080/dog"
```

   *  `POST /dog` -> It should return 200 Ok and NOT rate limited

```bash
curl --resolve example.com:9080:127.0.0.1 -v -X POST "http://example.com:9080/dog"
```
