## Generate Kuadrant AuthPolicy object from OpenAPI 3

The `kuadrantctl generate kuadrant authpolicy` command generates an [Kuadrant AuthPolicy](https://docs.kuadrant.io/kuadrant-operator/doc/auth/)
from your [OpenAPI Specification (OAS) 3.x](https://spec.openapis.org/oas/latest.html) powered with [kuadrant extensions](openapi-kuadrant-extensions.md).

### OpenAPI specification

An OpenAPI document resource can be provided to the cli by one of the following channels:

* Filename in the available path.
* URL format (supported schemes are HTTP and HTTPS). The CLI will try to download from the given address.
* Read from stdin standard input stream.

OpenAPI [Security Scheme Object](https://spec.openapis.org/oas/latest.html#security-scheme-object) types

| Types | Implemented |
| --- | --- |
| `openIdConnect` | **YES** |
| `apiKey` | **YES** |
| `http` | NO |
| `oauth2` | NO |

### `openIdConnect` Type Description

The following OAS example has one protected endpoint `GET /dog` with `openIdConnect` security scheme type.

```yaml
paths:
  /dog:
    get:
      operationId: "getDog"
      security:
        - securedDog: []
      responses:
        405:
          description: "invalid input"
components:
  securitySchemes:
    securedDog:
      type: openIdConnect
      openIdConnectUrl: https://example.com/.well-known/openid-configuration
```

Running the command

```
kuadrantctl generate kuadrant authpolicy --oas ./petstore-openapi.yaml  | yq -P
```

The generated authpolicy (only relevan fields shown here):

```yaml
kind: AuthPolicy
apiVersion: kuadrant.io/v1beta2
metadata:
  name: petstore
  namespace: petstore
  creationTimestamp: null
spec:
  routeSelectors:
    - matches:
        - path:
            type: Exact
            value: /api/v1/dog
          method: GET
  rules:
    authentication:
      getDog_securedDog:
        credentials: {}
        jwt:
          issuerUrl: https://example.com/.well-known/openid-configuration
        routeSelectors:
          - matches:
              - path:
                  type: Exact
                  value: /api/v1/dog
                method: GET
```

### `apiKey` Type Description

The following OAS example has one protected endpoint `GET /dog` with `apiKey` security scheme type.

```yaml
paths:
  /dog:
    get:
      operationId: "getDog"
      security:
        - securedDog: []
      responses:
        405:
          description: "invalid input"
components:
  securitySchemes:
    securedDog:
      type: apiKey
      name: dog_token
      in: query
```

Running the command

```
kuadrantctl generate kuadrant authpolicy --oas ./petstore-openapi.yaml  | yq -P
```

The generated authpolicy (only relevan fields shown here):

```yaml
kind: AuthPolicy
apiVersion: kuadrant.io/v1beta2
metadata:
  name: petstore
  namespace: petstore
  creationTimestamp: null
spec:
  routeSelectors:
    - matches:
        - path:
            type: Exact
            value: /dog
          method: GET
  rules:
    authentication:
      getDog_securedDog:
        credentials:
          queryString:
            name: dog_token
          apiKey:
            selector:
              matchLabels:
                kuadrant.io/apikeys-by: securedDog
        routeSelectors:
          - matches:
              - path:
                  type: Exact
                  value: /dog
                method: GET
```

In this particular example, the endpoint `GET /dog` will be protected.
The token needs to be in the query string of the request included in a parameter named `dog_token`.
Kuadrant will validate received tokens against tokens found in kubernetes secrets with label `kuadrant.io/apikeys-by: ${sec scheme name}`.
In this particular example the label selector will be: `kuadrant.io/apikeys-by: securedDog`.

Like the following example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: api-key-1
  labels:
    authorino.kuadrant.io/managed-by: authorino
    kuadrant.io/apikeys-by: securedDog
stringData:
  api_key: MYSECRETTOKENVALUE
type: Opaque
```
> **Note**: Kuadrant validates tokens against api keys found in secrets. The label selector format `kuadrant.io/apikeys-by: ${sec scheme name}` is arbitrary and designed for this CLI command.

For more information about Kuadrant auth based on api key: https://docs.kuadrant.io/authorino/docs/user-guides/api-key-authentication/

### Usage

```shell
Generate Kuadrant AuthPolicy from OpenAPI 3.0.X

Usage:
  kuadrantctl generate kuadrant authpolicy [flags]

Flags:
  -h, --help         help for authpolicy
  --oas string        Path to OpenAPI spec file (in JSON or YAML format), URL, or '-' to read from standard input (required)
  -o Output format:   'yaml' or 'json'. (default "yaml")

Global Flags:
  -v, --verbose   verbose output
```

> Under the example folder there are examples of OAS 3 that can be used to generate the resources

### User Guide

The verification steps will lead you to the process of deploying and testing the following api with
endpoints protected using different security schemes:

| Operation | Security Scheme |
| --- | --- |
| `GET /api/v1/cat` | public (not auth) |
| `POST /api/v1/cat` | ApiKey in header |
| `GET /api/v1/dog` | OpenIdConnect  |
| `GET /api/v1/snake` | OpenIdConnect **OR** ApiKey in query string  |

* [Optional] Setup SSO service supporting OIDC. For this example, we will be using [keycloak](https://www.keycloak.org).
  * Create a new realm `petstore`
  * Create a client `petstore`. In the Client Protocol field, select `openid-connect`.
  * Configure client settings. Access Type to public. Direct Access Grants Enabled to ON (for this example password will be used directly to generate the token).
  * Add a user to the realm
    * Click the Users menu on the left side of the window.  Click Add user.
    * Type the username `bob`, set the Email Verified switch to ON, and click Save.
    * On the Credentials tab, set the password `p`. Enter the password in both the fields, set the Temporary switch to OFF to avoid the password reset at the next login, and click `Set Password`.

Now, let's run local cluster to test the kuadrantctl new command to generate authpolicy.

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
openapi: "3.1.0"
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
  - url: https://example.io/api/v1
paths:
  /cat:
    x-kuadrant:
      backendRefs:
        - name: petstore
          port: 80
          namespace: petstore
    get:  # No sec requirements
      operationId: "getCat"
      responses:
        405:
          description: "invalid input"
    post:  # API key
      operationId: "postCat"
      security:
        - cat_api_key: []
      responses:
        405:
          description: "invalid input"
  /dog:
    x-kuadrant:
      backendRefs:
        - name: petstore
          port: 80
          namespace: petstore
    get:  # OIDC
      operationId: "getDog"
      security:
        - oidc:
          - read:dogs
      responses:
        405:
          description: "invalid input"
  /snake:
    x-kuadrant:
      backendRefs:
        - name: petstore
          port: 80
          namespace: petstore
    get:  # OIDC or API key
      operationId: "getSnake"
      security:
        - oidc: ["read:snakes"]
        - snakes_api_key: []
      responses:
        405:
          description: "invalid input"
components:
  securitySchemes:
    cat_api_key:
      type: apiKey
      name: api_key
      in: header
    oidc:
      type: openIdConnect
      openIdConnectUrl: https://${KEYCLOAK_PUBLIC_DOMAIN}/auth/realms/petstore
    snakes_api_key:
      type: apiKey
      name: snake_token
      in: query
EOF
```

</details>

> Replace `${KEYCLOAK_PUBLIC_DOMAIN}` with your SSO instance domain

* Create an API key only valid for `POST /api/v1/cat` endpoint
```yaml
kubectl apply -f -<<EOF
apiVersion: v1
kind: Secret
metadata:
  name: cat-api-key-1
  namespace: petstore
  labels:
    authorino.kuadrant.io/managed-by: authorino
    kuadrant.io/apikeys-by: cat_api_key
stringData:
  api_key: I_LIKE_CATS
type: Opaque
EOF
```
> **Note**: the label's value of `kuadrant.io/apikeys-by: cat_api_key` is the name of the sec scheme of the OpenAPI spec.

* Create an API key only valid for `GET /api/v1/snake` endpoint

```yaml
kubectl apply -f -<<EOF
apiVersion: v1
kind: Secret
metadata:
  name: snake-api-key-1
  namespace: petstore
  labels:
    authorino.kuadrant.io/managed-by: authorino
    kuadrant.io/apikeys-by: snakes_api_key
stringData:
  api_key: I_LIKE_SNAKES
type: Opaque
EOF
```

> **Note**: the label's value of `kuadrant.io/apikeys-by: snakes_api_key` is the name of the sec scheme of the OpenAPI spec.

* Create the HTTPRoute using the CLI

```bash
bin/kuadrantctl generate gatewayapi httproute --oas petstore-openapi.yaml | kubectl apply -n petstore -f -
```

* Create Kuadrant's Auth Policy

```bash
bin/kuadrantctl generate kuadrant authpolicy --oas petstore-openapi.yaml | kubectl apply -n petstore -f -
```

Now, we are ready to test OpenAPI endpoints :exclamation:

- `GET /api/v1/cat` -> It's a public endpoint, hence should return 200 Ok

```bash
curl  -H "Host: example.com" -i "http://127.0.0.1:9080/api/v1/cat"
```

- `POST /api/v1/cat` -> It's a protected endpoint with apikey

Without any credentials, it should return `401 Unauthorized`

```bash
curl  -H "Host: example.com" -X POST -i "http://127.0.0.1:9080/api/v1/cat"
```

```
HTTP/1.1 401 Unauthorized
www-authenticate: Bearer realm="getDog_oidc"
www-authenticate: Bearer realm="getSnake_oidc"
www-authenticate: snake_token realm="getSnake_snakes_api_key"
www-authenticate: api_key realm="postCat_cat_api_key"
x-ext-auth-reason: {"postCat_cat_api_key":"credential not found"}
date: Tue, 28 Nov 2023 22:28:44 GMT
server: istio-envoy
content-length: 0
```

The *reason* headers tell that `credential not found`.
Credentials satisfying `postCat_cat_api_key` authentication is needed.

According to the OpenAPI spec, it should be a header named `api_key`.
What if we try a wrong token? one token assigned to other endpoint,
i.e. `I_LIKE_SNAKES` instead of the valid one `I_LIKE_CATS`. It should return `401 Unauthorized`.

```bash
curl  -H "Host: example.com" -H "api_key: I_LIKE_SNAKES" -X POST -i "http://127.0.0.1:9080/api/v1/cat"
```

```
HTTP/1.1 401 Unauthorized
www-authenticate: Bearer realm="getDog_oidc"
www-authenticate: Bearer realm="getSnake_oidc"
www-authenticate: snake_token realm="getSnake_snakes_api_key"
www-authenticate: api_key realm="postCat_cat_api_key"
x-ext-auth-reason: {"postCat_cat_api_key":"the API Key provided is invalid"}
date: Tue, 28 Nov 2023 22:32:55 GMT
server: istio-envoy
content-length: 0
```

The *reason* headers tell that `the API Key provided is invalid`.
Using valid token (from the secret `cat-api-key-1` assigned to `POST /api/v1/cats`)
in the `api_key` header should return 200 Ok

```
curl  -H "Host: example.com" -H "api_key: I_LIKE_CATS" -X POST -i "http://127.0.0.1:9080/api/v1/cat"
```

- `GET /api/v1/dog` -> It's a protected endpoint with oidc (assigned to our keycloak instance and `petstore` realm)

without credentials, it should return `401 Unauthorized`

```bash
curl -H "Host: example.com" -i "http://127.0.0.1:9080/api/v1/dog"
```

To get the authentication token, this example is using Direct Access Grants oauth2 grant type
(also known as Client Credentials grant type). When configuring the Keycloak (OIDC provider) client
settings, we enabled Direct Access Grants to enable this procedure.
We will be authenticating as `bob` user with `p` password.
We previously created `bob` user in Keycloak in the `petstore` realm.

```
export ACCESS_TOKEN=$(curl -k -H "Content-Type: application/x-www-form-urlencoded" \
        -d 'grant_type=password' \
        -d 'client_id=petstore' \
        -d 'scope=openid' \
        -d 'username=bob' \
        -d 'password=p' "https://${KEYCLOAK_PUBLIC_DOMAIN}/auth/realms/petstore/protocol/openid-connect/token" | jq -r '.access_token')
```

> Replace `${KEYCLOAK_PUBLIC_DOMAIN}` with your SSO instance domain


With the access token in place, let's try to get those puppies

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: example.com' http://127.0.0.1:9080/api/v1/dog -i
```

it should return 200 OK

- `GET /api/v1/snake` -> It's a protected endpoint with oidc (assigned to our keycloak instance and `petstore` realm) **OR** with apiKey

This example is to show that multiple security requirements (with *OR* semantics) can be specified
for an OpenAPI operation.

Without credentials, it should return `401 Unauthorized`

```bash
curl -H "Host: example.com" -i "http://127.0.0.1:9080/api/v1/snake"
```

With the access token in place, it should return 200 OK (unless the token has expired).

```bash
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: example.com' http://127.0.0.1:9080/api/v1/snake -i
```

With apiKey it should also work. According to the OpenAPI spec security scheme,
it should be a query string named `snake_token` and the token needs to be valid token
(from the secret `snake-api-key-1` assigned to `GET /api/v1/snake`)

```bash
curl -H 'Host: example.com' -i "http://127.0.0.1:9080/api/v1/snake?snake_token=I_LIKE_SNAKES"
```

