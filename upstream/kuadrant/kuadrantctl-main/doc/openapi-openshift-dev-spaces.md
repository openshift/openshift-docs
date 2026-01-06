# Integrating Kuadrant OAS extensions with Red Hat OpenShift Dev Spaces

[OpenAPI extensions](https://swagger.io/docs/specification/openapi-extensions/) enhance the standard OpenAPI specification by adding custom functionality. Kuadrant OpenAPI extensions are identified by the `x-kuadrant` prefix. You can use OpenAPI extensions to integrate Kuadrant policies directly into your API definitions.

[Red Hat OpenShift Dev Spaces](https://developers.redhat.com/developer-sandbox/ide) provides a browser-based, cloud-native IDE that supports rapid and decentralized development in container-based environments. This tutorial demonstrates how to use OpenShift Dev Spaces to modify an OpenAPI definition by incorporating Kuadrant policies, and then use the `kuadrantctl` CLI to create Kubernetes resources for both Gateway API and Kuadrant.


## Prerequisites

- You must have access to one of the following Dev Spaces instances:
 
  - A self-hosted OpenShift Dev Spaces instance.
  - An OpenShift Dev Spaces instance provided by the [Red Hat Developer Sandbox](https://developers.redhat.com/developer-sandbox/ide).

## Procedure 

### Step 1 - Setting up your workspace

Create a workspace in Dev Spaces for your project as follows:

1. Fork the following repository: [https://github.com/Kuadrant/blank-petstore](https://github.com/Kuadrant/blank-petstore).
2. In Dev Spaces, select **Create Workspace**, and enter the URL of your forked repository. For example: `https://github.com/<your-username>/blank-petstore.git`.
3. Click **Create & Open**.

### Step 2 - Configuring VS Code in Dev Spaces

For this tutorial, you will perform the following tasks:

- Install `kuadrantctl` in your workspace to demonstrate Kubernetes resource generation from your modified OpenAPI definition.
- Optional: Configure Git with your username and email to enable pushing changes back to your repository.


#### Install the kuadrantctl CLI

To install `kuadrantctl` in your Dev Spaces workspace, enter the following command:

```bash
curl -sL "https://github.com/kuadrant/kuadrantctl/releases/download/v0.2.3/kuadrantctl-v0.2.3-linux-amd64.tar.gz" | tar xz -C /home/user/.local/bin
```

This command installs `kuadrantctl` in `/home/user/.local/bin`, which is included in the container's `$PATH` by default.

#### Optional: Configuring Git

If you plan to push changes back to your repository, configure your Git username and email as follows:

```bash
git config --global user.email "foo@example.com"
git config --global user.name "Foo Example"
```

### Step 3 - Adding Kuadrant policies to your OpenAPI definition 

After creating your workspace, Dev Spaces will launch VS Code loaded with your forked repository. Navigate to the `openapi.yaml` file in the sample app to begin modifications.

#### Kuadrant policies overview 

You will enhance your API definition by applying Kuadrant policies to the following endpoints:

- `/pet/findByStatus`
-  `/user/login`
-  `/store/inventory`

In this tutorial, you will add Kuadrant policies to your API definition as follows:

- Generate an `HTTPRoute` to expose these three routes for an existing `Gateway`.
- Add API key authentication for the `/user/login` route, using a Kuadrant `AuthPolicy` and OAS `securitySchemes`.
- Add a Kuadrant `RateLimitPolicy` to the `/store/inventory` endpoint, to limit the amount of requests this endpoint can receive.

#### Defining a Gateway

Use the `x-kuadrant` extension in the root level to specify a `Gateway`. This information will be used to generate `HTTPRoute`s at the path level. For example:

```yaml
x-kuadrant:
  route:  ## HTTPRoute metadata
    name: "petstore"
    namespace: "petstore"
    labels:  ## map[string]string
      deployment: petstore
    hostnames:  ## []gateway.networking.k8s.io/v1beta1.Hostname
      - example.com
    parentRefs:  ## []gateway.networking.k8s.io/v1beta1.ParentReference
      - name: apiGateway
        namespace: gateways
```

#### Specifying HTTPRoutes for each path

For each path, add an `x-kuadrant` extension with `backendRefs` to link your routes to your paths as follows:

```yaml
  /pet/findByStatus:
    x-kuadrant:
      backendRefs:
      - name: petstore
        namespace: petstore
        port: 8080
    get:
      # ...
```

```yaml
  /user/login:
    x-kuadrant:
      backendRefs:
      - name: petstore
        namespace: petstore
        port: 8080
    get:
      # ...
```

```yaml
  /store/inventory:
    x-kuadrant:
      backendRefs:
      - name: petstore
        namespace: petstore
        port: 8080
    get:
      # ...
```

**Note:** The `x-kuadrant` extension at the path level applies to all HTTP methods defined in the path. For method-specific policies, move the extension inside the relevant HTTP method block, for example, `get` or `post`.


#### Implementing AuthPolicy and security schemes

To secure the `/user/login` endpoint with API key authentication, use the following configuration:

```yaml
  /user/login:
    # ...
    get:
      security:
      - api_key: []
```

```yaml
components:
  schemas:
    # ...
  securitySchemes:
    api_key:
      type: apiKey
      name: api_key
      in: header
```

This configuration generates an `AuthPolicy` that references an API key stored in a labeled `Secret`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: petstore-api-key
  namespace: petstore
  labels:
    authorino.kuadrant.io/managed-by: authorino
    kuadrant.io/apikeys-by: api_key
stringData:
  api_key: secret
type: Opaque
```
For simplicity, this example uses a simple, static API key for your app.


#### Applying a RateLimitPolicy to an endpoint

To enforce rate limiting on the `/store/inventory` endpoint, add the following `x-kuadrant` extension:

```yaml
  /store/inventory:
    get:
      # ...
      x-kuadrant:
        backendRefs:
          # ...
        rate_limit:
          rates:
          - limit: 10
            duration: 10
            unit: second
```

This limits to 10 requests every 10 seconds for the `/store/inventory` endpoint.


### Step 4 - Generate Kubernetes resources by using kuadrantctl

With your extensions in place, you can use `kuadrantctl` to generate the follollowing Kubernetes resources:

- An `HTTPRoute` for your `petstore` app for each of your endpoints.
- An `AuthPolicy` with a simple, static API key from a secret for the `/user/login` endpoint.
- A `RateLimitPolicy` with a rate limit of 10 requests every 10 seconds for the `/store/inventory` endpoint.

In Dev Spaces, select **☰ > Terminal > New Terminal**, and run the following commands:

##### Generate an HTTPRoute

```bash
kuadrantctl generate gatewayapi httproute --oas openapi.yaml
```

This command outputs the following `HTTPRoute`:

```yaml
kind: HTTPRoute
apiVersion: gateway.networking.k8s.io/v1beta1
metadata:
  name: petstore
  namespace: petstore
  creationTimestamp: null
  labels:
    deployment: petstore
spec:
  parentRefs:
    - namespace: gateways
      name: apiGateway
  hostnames:
    - example.com
  rules:
    - matches:
        - path:
            type: Exact
            value: /api/v3/pet/findByStatus
          method: GET
      backendRefs:
        - name: petstore
          namespace: petstore
          port: 8080
    - matches:
        - path:
            type: Exact
            value: /api/v3/store/inventory
          method: GET
      backendRefs:
        - name: petstore
          namespace: petstore
          port: 8080
    - matches:
        - path:
            type: Exact
            value: /api/v3/user/login
          method: GET
      backendRefs:
        - name: petstore
          namespace: petstore
          port: 8080
status:
  parents: null
```

##### Generate an AuthPolicy

```bash
kuadrantctl generate kuadrant authpolicy --oas openapi.yaml
```

This command outputs the following `AuthPolicy`:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: AuthPolicy
metadata:
  name: petstore
  namespace: petstore
  creationTimestamp: null
  labels:
    deployment: petstore
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: petstore
    namespace: petstore
  routeSelectors:
    - matches:
        - path:
            type: Exact
            value: /api/v3/user/login
          method: GET
  rules:
    authentication:
      GETuserlogin_api_key:
        credentials:
          customHeader:
            name: api_key
        apiKey:
          selector:
            matchLabels:
              kuadrant.io/apikeys-by: api_key
        routeSelectors:
          - matches:
              - path:
                  type: Exact
                  value: /api/v3/user/login
                method: GET
status: {}
```

##### Generate a RateLimitPolicy

```bash
kuadrantctl generate kuadrant ratelimitpolicy --oas openapi.yaml
```

This command outputs the following `RateLimitPolicy`:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: petstore
  namespace: petstore
  creationTimestamp: null
  labels:
    deployment: petstore
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: petstore
    namespace: petstore
  limits:
    GETstoreinventory:
      routeSelectors:
        - matches:
            - path:
                type: Exact
                value: /api/v3/store/inventory
              method: GET
      rates:
        - limit: 10
          duration: 10
          unit: second
status: {}
```

### Step 5 - Applying resources to the app

> **Note:** By default, the `oc` and `kubectl` commands in Dev Spaces target the cluster running Dev Spaces. If you want to apply resources to another cluster, you must log in with `oc` or `kubectl` to another cluster, and pass a different `--context` to these commands to apply resources to another cluster.

You can now apply these policies to a running app by using `kubectl` or `oc`. If Dev Spaces is running on a cluster where Kuadrant is also installed, you can apply these resources as follows:


```bash
kuadrantctl generate gatewayapi httproute --oas openapi.yaml | kubectl apply -f -
kuadrantctl generate kuadrant authpolicy --oas openapi.yaml | kubectl apply -f -
kuadrantctl generate kuadrant ratelimitpolicy --oas openapi.yaml | kubectl apply -f -
```

Alternatively, you can use `kuadrantctl` as part of a CI/CD pipeline. For more details, see the [kuadrantctl CI/CD guide](./kuadrantctl-ci-cd.md).

If you completed the optional Git configuration step, you can enter `git commit` to commit the these changes and push them to your fork.

## Additional resources

For more details, see the following documentation on using `x-kuadrant` OAS extensions with `kuadrantctl`:

- [OpenAPI 3.0.x Kuadrant extensions](./openapi-kuadrant-extensions.md)
- [Generate Gateway API HTTPRoutes with `kuadrantctl`](./generate-gateway-api-httproute.md)
- [Generate Kuadrant AuthPolicy with `kuadrantctl`](./generate-kuadrant-auth-policy.md)
- [Generate Kuadrant RateLimitPolicy with `kuadrantctl`](./generate-kuadrant-rate-limit-policy.md)
- [kuadrantctl CI/CD guide](./kuadrantctl-ci-cd.md)
