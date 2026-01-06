# Authenticated Rate Limiting with JWTs and Kubernetes RBAC

This user guide walks you through an example of how to use Kuadrant to protect an application with policies to enforce:

- authentication based OpenId Connect (OIDC) ID tokens (signed JWTs), issued by a Keycloak server;
- alternative authentication method by Kubernetes Service Account tokens;
- authorization delegated to Kubernetes RBAC system;
- rate limiting by user ID.

In this example, we will protect a sample REST API called **Toy Store**. In reality, this API is just an echo service that echoes back to the user whatever attributes it gets in the request.

The API listens to requests at the hostnames `*.toystore.com`, where it exposes the endpoints `GET /toy*`, `POST /admin/toy` and `DELETE /amind/toy`, respectively, to mimic operations of reading, creating, and deleting toy records.

Any authenticated user/service account can send requests to the Toy Store API, by providing either a valid Keycloak-issued access token or Kubernetes token.

Privileges to execute the requested operation (read, create or delete) will be granted according to the following RBAC rules, stored in the Kubernetes authorization system:

| Operation | Endpoint            | Required role     |
|-----------|---------------------|-------------------|
| Read      | `GET /toy*`         | `toystore-reader` |
| Create    | `POST /admin/toy`   | `toystore-write`  |
| Delete    | `DELETE /admin/toy` | `toystore-write`  |

Each user will be entitled to a maximum of 5rp10s (5 requests every 10 seconds).

## Requirements

- [Docker](https://www.docker.com/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line tool
- [jq](https://stedolan.github.io/jq/)

## Run the guide ① → ⑥

### ① Setup a cluster with Kuadrant

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

Deploy the application in the `default` namespace:

```sh
kubectl apply -f examples/toystore/toystore.yaml
```

Route traffic to the application:

```sh
kubectl apply -f examples/toystore/httproute.yaml
```

#### API lifecycle

![Lifecycle](http://www.plantuml.com/plantuml/png/hP7DIWD1383l-nHXJ_PGtFuSIsaH1F5WGRtjPJgJjg6pcPB9WFNf7LrXV_Ickp0Gyf5yIJPHZMXgV17Fn1SZfW671vEylk2RRZqTkK5MiFb1wL4I4hkx88m2iwee1AqQFdg4ShLVprQt-tNDszq3K8J45mcQ0NGrj_yqVpNFgmgU7aim0sPKQzxMUaQRXFGAqPwmGJW40JqXv1urHpMA3eZ1C9JbDkbf5ppPQrdMV9CY2XmC-GWQmEGaif8rYfFEPLdDu9K_aq7e7TstLPyUcot-RERnI0fVVjxOSuGBIaCnKk21sWBkW-p9EUJMgnCTIot_Prs3kJFceEiu-VM2uLmKlIl2TFrZVQCu8yD9kg1Dvf8RP9SQ_m40)

#### Try the API unprotected

Export the gateway hostname and port:

```sh
export INGRESS_HOST=$(kubectl get gtw istio-ingressgateway -n istio-system -o jsonpath='{.status.addresses[0].value}')
export INGRESS_PORT=$(kubectl get gtw istio-ingressgateway -n istio-system -o jsonpath='{.spec.listeners[?(@.name=="http")].port}')
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
```

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 200 OK
```

It should return `200 OK`.

> **Note**: If the command above fails to hit the Toy Store API on your environment, try forwarding requests to the service and accessing over localhost:
>
> ```sh
> kubectl port-forward -n istio-system service/istio-ingressgateway-istio 9080:80 2>&1 >/dev/null &
> export GATEWAY_URL=localhost:9080
> ```
> ```sh
> curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
> # HTTP/1.1 200 OK
> ```

### ③ Deploy Keycloak

Create the namesapce:

```sh
kubectl create namespace keycloak
```

Deploy Keycloak with a [bootstrap](https://github.com/kuadrant/authorino-examples#keycloak) realm, users, and clients:

```sh
kubectl apply -n keycloak -f https://raw.githubusercontent.com/Kuadrant/authorino-examples/main/keycloak/keycloak-deploy.yaml
```

> **Note:** The Keycloak server may take a couple of minutes to be ready.

### ④ Enforce authentication and authorization for the Toy Store API

Create a Kuadrant `AuthPolicy` to configure authentication and authorization:

```sh
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: AuthPolicy
metadata:
  name: toystore-protection
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: toystore
  rules:
    authentication:
      "keycloak-users":
        jwt:
          issuerUrl: http://keycloak.keycloak.svc.cluster.local:8080/realms/kuadrant
      "k8s-service-accounts":
        kubernetesTokenReview:
          audiences:
          - https://kubernetes.default.svc.cluster.local
        overrides:
          "sub":
            selector: auth.identity.user.username
    authorization:
      "k8s-rbac":
        kubernetesSubjectAccessReview:
          user:
            selector: auth.identity.sub
    response:
      success:
        dynamicMetadata:
          "identity":
            json:
              properties:
                "userid":
                  selector: auth.identity.sub
EOF
```

#### Try the API missing authentication

```sh
curl -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 401 Unauthorized
# www-authenticate: Bearer realm="keycloak-users"
# www-authenticate: Bearer realm="k8s-service-accounts"
# x-ext-auth-reason: {"k8s-service-accounts":"credential not found","keycloak-users":"credential not found"}
```

#### Try the API without permission

Obtain an access token with the Keycloak server:

```sh
ACCESS_TOKEN=$(kubectl run token --attach --rm --restart=Never -q --image=curlimages/curl -- http://keycloak.keycloak.svc.cluster.local:8080/realms/kuadrant/protocol/openid-connect/token -s -d 'grant_type=password' -d 'client_id=demo' -d 'username=john' -d 'password=p' -d 'scope=openid' | jq -r .access_token)
```

Send a request to the API as the Keycloak-authenticated user while still missing permissions:

```sh
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 403 Forbidden
```

Create a Kubernetes Service Account to represent a consumer of the API associated with the alternative source of identities `k8s-service-accounts`:

```sh
kubectl apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: client-app-1
EOF
```

Obtain an access token for the `client-app-1` service account:

```sh
SA_TOKEN=$(kubectl create token client-app-1)
```

Send a request to the API as the service account while still missing permissions:

```sh
curl -H "Authorization: Bearer $SA_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 403 Forbidden
```

### ⑤ Grant access to the Toy Store API for user and service account

Create the `toystore-reader` and `toystore-writer` roles:

```sh
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: toystore-reader
rules:
- nonResourceURLs: ["/toy*"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: toystore-writer
rules:
- nonResourceURLs: ["/admin/toy"]
  verbs: ["post", "delete"]
EOF
```

Add permissions to the user and service account:

| User         | Kind                        | Roles                                |
|--------------|-----------------------------|--------------------------------------|
| john         | User registered in Keycloak | `toystore-reader`, `toystore-writer` |
| client-app-1 | Kuberentes Service Account  | `toystore-reader`                    |

```sh
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: toystore-readers
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: toystore-reader
subjects:
- kind: User
  name: $(jq -R -r 'split(".") | .[1] | @base64d | fromjson | .sub' <<< "$ACCESS_TOKEN")
- kind: ServiceAccount
  name: client-app-1
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: toystore-writers
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: toystore-writer
subjects:
- kind: User
  name: $(jq -R -r 'split(".") | .[1] | @base64d | fromjson | .sub' <<< "$ACCESS_TOKEN")
EOF
```

<details markdown="1">
  <summary><i>Q:</i> Can I use <code>Roles</code> and <code>RoleBindings</code> instead of <code>ClusterRoles</code> and <code>ClusterRoleBindings</code>?</summary>

  Yes, you can.

  The example above is for non-resource URL Kubernetes roles. For using `Roles` and `RoleBindings` instead of
  `ClusterRoles` and `ClusterRoleBindings`, thus more flexible resource-based permissions to protect the API,
  see the spec for [Kubernetes SubjectAccessReview authorization](https://docs.kuadrant.io/authorino/docs/features/#kubernetes-subjectaccessreview-authorizationkubernetessubjectaccessreview)
  in the Authorino docs.
</details>

#### Try the API with permission

Send requests to the API as the Keycloak-authenticated user:

```sh
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 200 OK
```

```sh
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: api.toystore.com' -X POST http://$GATEWAY_URL/admin/toy -i
# HTTP/1.1 200 OK
```

Send requests to the API as the Kubernetes service account:

```sh
curl -H "Authorization: Bearer $SA_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy -i
# HTTP/1.1 200 OK
```

```sh
curl -H "Authorization: Bearer $SA_TOKEN" -H 'Host: api.toystore.com' -X POST http://$GATEWAY_URL/admin/toy -i
# HTTP/1.1 403 Forbidden
```

### ⑥ Enforce rate limiting on requests to the Toy Store API

Create a Kuadrant `RateLimitPolicy` to configure rate limiting:

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
    "per-user":
      rates:
      - limit: 5
        duration: 10
        unit: second
      counters:
      - metadata.filter_metadata.envoy\.filters\.http\.ext_authz.identity.userid
EOF
```

> **Note:** It may take a couple of minutes for the RateLimitPolicy to be applied depending on your cluster.

#### Try the API rate limited

Each user should be entitled to a maximum of 5 requests every 10 seconds.

> **Note:** If the tokens have expired, you may need to refresh them first.

Send requests as the Keycloak-authenticated user:

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H "Authorization: Bearer $ACCESS_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy | grep -E --color "\b(429)\b|$"; sleep 1; done
```

Send requests as the Kubernetes service account:

```sh
while :; do curl --write-out '%{http_code}\n' --silent --output /dev/null -H "Authorization: Bearer $SA_TOKEN" -H 'Host: api.toystore.com' http://$GATEWAY_URL/toy | grep -E --color "\b(429)\b|$"; sleep 1; done
```

## Cleanup

```sh
make local-cleanup
```
