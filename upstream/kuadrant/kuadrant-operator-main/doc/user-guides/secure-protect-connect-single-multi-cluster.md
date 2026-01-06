# Secure, protect, and connect APIs with Kuadrant on OpenShift

## Overview

This guide walks you through using Kuadrant on OpenShift to secure, protect, and connect an API exposed by a Gateway that is based on Kubernetes Gateway API. You can use this walkthrough for a Gateway deployed on a single OpenShift cluster or a Gateway distributed across multiple OpenShift clusters with a shared listener hostname. This guide shows how the platform engineer and application developer user roles can each use Kuadrant to achieve their goals.

### What Kuadrant can do for you in a multicluster environment

You can leverage Kuadrant's capabilities in single or multiple clusters. The following features are designed to work across multiple clusters as well as in a single-cluster environment.

- **Multicluster ingress:** Kuadrant provides multicluster ingress connectivity using DNS to bring traffic to your Gateways by using a strategy defined in a `DNSPolicy`. 
- **Global rate limiting:** Kuadrant can enable global rate limiting use cases when configured to use a shared Redis store for counters based on limits defined by a `RateLimitPolicy`.
- **Global auth:** You can configure a Kuadrant `AuthPolicy` to leverage external auth providers to ensure that different clusters exposing the same API authenticate and authorize in the same way. 
- **Integration with federated metrics stores:** Kuadrant has example dashboards and metrics for visualizing your Gateways and observing traffic hitting those Gateways across multiple clusters. 

### User roles

- **Platform engineer**: This guide walks you through deploying a Gateway that provides secure communication and is protected and ready for use by application development teams to deploy an API. It then walks through using this Gateway in clusters in different geographic regions, leveraging Kuadrant to bring specific traffic to your geo-located Gateways. This approach reduces latency and distributes load, while still being protected and secured with global rate limiting and auth. 

- **Application developer**: This guide walks through how you can use the Kuadrant OpenAPI Specification (OAS) extensions and optional `kuadrantctl` CLI to generate an `HTTPRoute` for your API and to add specific auth and rate limiting requirements.

As an optional extra, this guide highlights how both user roles can observe and monitor these Gateways when the OpenShift user workload monitoring and observability stack is deployed. 

### Deployment management tooling

While this document uses `kubectl` commands for simplicity, working with multiple clusters is complex, and it is best to use a tool such as Argo CD to manage the deployment of resources to multiple clusters.

## Prerequisites

This guide expects that you have successfully installed Kuadrant on at least one OpenShift cluster:

- You have completed the steps in [Install Kuadrant on an OpenShift cluster](../install/install-openshift.md) for one or more clusters.
- For multicluster scenarios, you have installed Kuadrant on at least two different OpenShift clusters, and have a shared accessible Redis store.
- You have the `kubectl` or `oc` command installed.
- You have write access to the OpenShift namespaces shown in this guide. 
* You have an AWS account with Amazon Route 53 and one or more DNS zones for the examples in this guide. Google Cloud DNS and Microsoft Azure DNS are also supported as DNS providers. 
- Optional:
  - For multicluster global rate limiting, you have installed {prodname} on at least two clusters, and have a shared accessible Redis store. 
  - For Observability, OpenShift user workload monitoring is configured to remote write to a central storage system such as Thanos, as described in [Install Kuadrant on an OpenShift cluster](../install/install-openshift.md).

## Platform engineer workflow

NOTE: You must perform the following steps in each cluster individually, unless specifically excluded. 

### Step 1 - Set your environment variables

Set the following environment variables used for convenience in this guide:
```bash
export zid=change-this-to-your-zone-id
export rootDomain=example.com
export gatewayNS=api-gateway
export gatewayName=external
export devNS=toystore
export AWS_ACCESS_KEY_ID=xxxx
export AWS_SECRET_ACCESS_KEY=xxxx
export AWS_REGION=us-east-1
export clusterIssuerName=lets-encrypt
export EMAIL=foo@example.com
```

### Step 2 - Set up a managed DNS zone

The managed DNS zone declares a zone and credentials to access the zone that Kuadrant can use to set up DNS configuration.

#### Create the ManagedZone resource

Apply the following `ManagedZone` resource and AWS credentials to each cluster. Alternatively, if you are adding an additional cluster, add it to the new cluster:

```bash
kubectl create ns ${gatewayNS}
```

Create the zone credentials as follows:

```
kubectl -n ${gatewayNS} create secret generic aws-credentials \
  --type=kuadrant.io/aws \
  --from-literal=AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  --from-literal=AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

```

Then create a `ManagedZone` as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: ManagedZone
metadata:
  name: managedzone
  namespace: ${gatewayNS}
spec:
  id: ${zid}
  domainName: ${rootDomain}
  description: "Kuadrant managed zone"
  dnsProviderSecretRef:
    name: aws-credentials
EOF
```

Wait for the `ManagedZone` to be ready in each cluster as follows:

```bash
kubectl wait managedzone/managedzone --for=condition=ready=true -n ${gatewayNS}
```

### Step 3 - Add a TLS issuer

To secure communication to the Gateways, you will define a TLS issuer for TLS certificates. This example uses Let's Encrypt, but you can use any issuer supported by `cert-manager`.

The following example uses Let's Encrypt staging, which you must also apply to all clusters:

```bash
kubectl apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ${clusterIssuerName}
spec:
  acme:
    email: ${EMAIL} 
    privateKeySecretRef:
      name: le-secret
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    solvers:
      - dns01:
          route53:
            hostedZoneID: ${zid}
            region: ${AWS_REGION}
            accessKeyIDSecretRef:
              key: AWS_ACCESS_KEY_ID
              name: aws-credentials
            secretAccessKeySecretRef:
              key: AWS_SECRET_ACCESS_KEY
              name: aws-credentials
EOF
```

Then wait for the `ClusterIssuer` to become ready as follows:

```bash
kubectl wait clusterissuer/${clusterIssuerName} --for=condition=ready=true
```

### Step 4 - Set up a Gateway

For Kuadrant to balance traffic using DNS across two or more clusters, you must define a Gateway with a shared host. You will define this by using an HTTPS listener with a wildcard hostname based on the root domain. As mentioned earlier, you must apply these resources to all clusters. 

NOTE: For now, the Gateway is set to accept an `HTTPRoute` from the same namespace only. This allows you to restrict who can use the Gateway until it is ready for general use.

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: ${gatewayName}
  namespace: ${gatewayNS}
  labels:
    kuadrant.io/gateway: "true"
spec:
    gatewayClassName: istio
    listeners:
    - allowedRoutes:
        namespaces:
          from: Same
      hostname: "*.${rootDomain}"
      name: api
      port: 443
      protocol: HTTPS
      tls:
        certificateRefs:
        - group: ""
          kind: Secret
          name: api-${gatewayName}-tls
        mode: Terminate
EOF
```

Check the status of your Gateway as follows:

```bash
kubectl get gateway ${gatewayName} -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Accepted")].message}'
kubectl get gateway ${gatewayName} -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Programmed")].message}'
```

Your Gateway should be accepted and programmed, which means valid and assigned an external address). However, if you check your listener status as follows, you will see that it is not yet programmed or ready to accept traffic due to bad TLS configuration:

```bash
kubectl get gateway ${gatewayName} -n ${gatewayNS} -o=jsonpath='{.status.listeners[0].conditions[?(@.type=="Programmed")].message}'
```

Kuadrant can help with this by using a TLSPolicy.

### Step 5 - Secure and protect the Gateway with auth, TLS, rate limit, and DNS policies

While your Gateway is now deployed, it has no exposed endpoints and your listener is not programmed. Next, you can set up a `TLSPolicy` that leverages your CertificateIssuer to set up your listener certificates. 

You will also define an `AuthPolicy` that will set up a default `403` response for any unprotected endpoints, as well as a `RateLimitPolicy` that will set up a default artificially low global limit to further protect any endpoints exposed by this Gateway.

#### Set the Auth policy

Set a default, deny-all `AuthPolicy` for your Gateway as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: AuthPolicy
metadata:
  name: ${gatewayName}-auth
  namespace: ${gatewayNS}
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: ${gatewayName}
  defaults:
    rules:
      authorization:
        "deny":
          opa:
            rego: "allow = false"
EOF
```

Check that your auth policy was accepted by the controller as follows:

```bash
kubectl get authpolicy ${gatewayName}-auth -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Accepted")].message}'

```

#### Set the TLS policy

Set the `TLSPolicy` for your Gateway as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: TLSPolicy
metadata:
  name: ${gatewayName}-tls
  namespace: ${gatewayNS}
spec:
  targetRef:
    name: ${gatewayName}
    group: gateway.networking.k8s.io
    kind: Gateway
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: ${clusterIssuerName}
EOF
```

Check that your TLS policy was accepted by the controller as follows:

```bash
kubectl get tlspolicy ${gatewayName}-tls -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Accepted")].message}'
```

#### Set the rate limit policy

Set the default `RateLimitPolicy` for your Gateway as follows:

```bash
kubectl apply -f  - <<EOF
apiVersion: kuadrant.io/v1beta2
kind: RateLimitPolicy
metadata:
  name: ${gatewayName}-rlp
  namespace: ${gatewayNS}
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: ${gatewayName}
  defaults:
    limits:
      "low-limit":
        rates:
        - limit: 2
          duration: 10
          unit: second
EOF
```

To check your rate limits have been accepted, enter the following command:

```bash
kubectl get ratelimitpolicy ${gatewayName}-rlp -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Accepted")].message}'
```

#### Set the DNS policy

Set the `DNSPolicy` for your Gateway as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: kuadrant.io/v1alpha1
kind: DNSPolicy
metadata:
  name: ${gatewayName}-dnspolicy
  namespace: ${gatewayNS}
spec:
  routingStrategy: loadbalanced
  loadBalancing:
    geo: 
      defaultGeo: US 
    weighted:
      defaultWeight: 120 
  targetRef:
    name: ${gatewayName}
    group: gateway.networking.k8s.io
    kind: Gateway
EOF
```    

NOTE:  The `DNSPolicy` will leverage the `ManagedZone` that you defined earlier based on the listener hosts defined in the Gateway.

Check that your `DNSPolicy` has been accepted as follows:

```bash
kubectl get dnspolicy ${gatewayName}-dnspolicy -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Accepted")].message}'
```

#### Create an HTTP route

Create an `HTTPRoute` for your Gateway as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: test
  namespace: ${gatewayNS}
spec:
  parentRefs:
  - name: ${gatewayName}
    namespace: ${gatewayNS}
  hostnames:
  - "test.${rootDomain}"
  rules:
  - backendRefs:
    - name: toystore
      port: 80
EOF
```

Check your Gateway policies are enforced as follows:

```bash
kubectl get dnspolicy ${gatewayName}-dnspolicy -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Enforced")].message}'
kubectl get authpolicy ${gatewayName}-auth -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Enforced")].message}'
kubectl get ratelimitpolicy ${gatewayName}-rlp -n ${gatewayNS} -o=jsonpath='{.status.conditions[?(@.type=="Enforced")].message}'
```

Check your listener is ready as follows:

```
kubectl get gateway ${gatewayName} -n ${gatewayNS} -o=jsonpath='{.status.listeners[0].conditions[?(@.type=="Programmed")].message}'
```

### Step 6 - Test connectivity and deny all auth 

You can use `curl` to hit your endpoint. You should see a `403`. Because this example uses Let's Encrypt staging, you can pass the `-k` flag:

```bash
curl -k -w "%{http_code}" https://$(kubectl get httproute test -n ${gatewayNS} -o=jsonpath='{.spec.hostnames[0]}')
```

### Step 7 - Opening up the Gateway for other namespaces

Because you have configured the Gateway, secured it with Kuadrant policies, and tested it, you can now open it up for use by other teams in other namespaces:

```bash
kubectl patch gateway ${gatewayName} -n ${gatewayNS} --type='json' -p='[{"op": "replace", "path": "/spec/listeners/0/allowedRoutes/namespaces/from", "value":"All"}]'
```

### Step 8 - Extending this Gateway to multiple clusters and configuring geo-based routing

To distribute this Gateway across multiple clusters, repeat this setup process for each cluster. By default, this will implement a round-robin DNS strategy to distribute traffic evenly across the different clusters. Setting up your Gateways to serve clients based on their geographic location is straightforward with your current configuration.

Assuming that you have deployed Gateway instances across multiple clusters as per this guide, the next step involves updating the DNS controller with the geographic regions of the visible Gateways.

For instance, if you have one cluster in North America and another in the EU, you can direct traffic to these Gateways based on their location by applying the appropriate labels:

For your North American cluster, enter the following command:

```bash
kubectl label --overwrite gateway ${gatewayName} kuadrant.io/lb-attribute-geo-code=US -n ${gatewayNS}
```

## Application developer workflow

This section of the walkthrough focuses on using an OpenAPI Specification (OAS) to define an API. You will use Kuadrant OAS extensions to specify the routing, authentication, and rate limiting requirements. Next, you will use the `kuadrantctl` tool to generate an `AuthPolicy`, an `HTTPRoute`, and a `RateLimitPolicy`, which you will then apply to your cluster to enforce the settings defined in your OAS.

NOTE: While this section uses the `kuadrantctl` tool, this is not essential. You can also create and apply an `AuthPolicy`, `RateLimitPolicy`, and `HTTPRoute` by using the `oc` or `kubectl` commands.

### Prerequisites

- You have installed `kuadrantctl`. You can find a compatible binary and download it from the [kuadrantctl releases page](https://github.com/Kuadrant/kuadrantctl/releases/tag/v0.2.2).
- In multicluster environments, you have the correct permissions to distribute the generated resources to multiple clusters.


### Step 1 - Deploy the toystore app

To begin, deploy a new version of the `toystore` app to a developer namespace as follows:

```bash
kubectl apply -f https://raw.githubusercontent.com/Kuadrant/Kuadrant-operator/main/examples/toystore/toystore.yaml -n ${devNS}
```


### Step 2 - Set up HTTPRoute and backend

Copy at least one of the following example OAS to a local location:

- [Sample OAS for rate limiting with API key](../../examples/oas-apikey.yaml)

- [Sample OAS for rate limiting with OIDC](../../examples/oas-oidc.yaml)

Set up some new environment variables as follows:

```bash
export oasPath=examples/oas-apikey.yaml
# Ensure you still have these environment variables setup from the start of this guide:
export rootDomain=example.com
export gatewayNS=api-gateway
```

### Step 3 - Use OAS to define your HTTPRoute rules

You can generate Kuadrant and Gateway API resources directly from OAS documents by using an `x-kuadrant` extension.

NOTE: For a more in-depth look at the OAS extension, see the [kuadrantctl documentation](https://docs.kuadrant.io/kuadrantctl/).

You will use `kuadrantctl` to generate your `HTTPRoute`.

NOTE: The sample OAS has some placeholders for namespaces and domains. You will inject valid values into these placeholders based on your previous environment variables.

Generate the resource from your OAS as follows, (`envsubst` will replace the placeholders):

```bash
cat $oasPath | envsubst | kuadrantctl generate gatewayapi httproute --oas - | kubectl apply -f -
```

```bash
kubectl get httproute toystore -n ${devNS} -o=yaml
```

You should see that this route is affected by the `AuthPolicy` and `RateLimitPolicy` defined as defaults on the Gateway in the Gateway namespace.

```yaml
- lastTransitionTime: "2024-04-26T13:37:43Z"
        message: Object affected by AuthPolicy demo/external
        observedGeneration: 2
        reason: Accepted
        status: "True"
        type: kuadrant.io/AuthPolicyAffected
- lastTransitionTime: "2024-04-26T14:07:28Z"
        message: Object affected by RateLimitPolicy demo/external
        observedGeneration: 1
        reason: Accepted
        status: "True"
        type: kuadrant.io/RateLimitPolicyAffected        
```

### Step 4 - Test connectivity and deny-all auth 

You can use `curl` to hit an endpoint in the toystore app. Because you are using Let's Encrypt staging in this example, you can pass the `-k` flag as follows:

```bash
curl -s -k -o /dev/null -w "%{http_code}" "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

You are getting a `403` because of the existing default, deny-all `AuthPolicy` applied at the Gateway. You can override this for your `HTTPRoute`.

Choose one of the following options:

- API key auth flow
- OpenID Connect auth flow 

### Step 5 - Set up API key auth flow

Set up an example API key in each cluster as follows:

```bash
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: toystore-api-key
  namespace: ${devNS}
  labels:
    authorino.kuadrant.io/managed-by: authorino
    kuadrant.io/apikeys-by: api_key
stringData:
  api_key: secret
type: Opaque
EOF
```

Next, generate an `AuthPolicy` that uses secrets in your cluster as API keys as follows:

```bash
cat $oasPath | envsubst | kuadrantctl generate kuadrant authpolicy --oas -
```

From this, you can see an `AuthPolicy` generated based on your OAS that will look for API keys in secrets labeled `api_key` and look for that key in the header `api_key`. You can now apply this to the Gateway as follows:

```bash
cat $oasPath | envsubst | kuadrantctl generate kuadrant authpolicy --oas -  | kubectl apply -f -
```

You should get a `200` from the following `GET` because it has no auth requirement:

```bash
curl -s -k -o /dev/null -w "%{http_code}" "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

You should get a `401` for the following `POST` request because it does not have any auth requirements:

```bash
curl -XPOST -s -k -o /dev/null -w "%{http_code}" "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

Finally, if you add your API key header, with a valid key as follows, you should get a `200` response:

```bash
curl -XPOST -H 'api_key: secret' -s -k -o /dev/null -w "%{http_code}" "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

### Optional: Step 6 - Set up OpenID Connect auth flow (skip if using API key only)

This section of the walkthrough uses the `kuadrantctl` tool to create an `AuthPolicy` that integrates with an OpenID provider and a `RateLimitPolicy` that leverages JWT values for per-user rate limiting. It is important to note that OpenID requires an external provider. Therefore, you should adapt the following example to suit your specific needs and provider.

The platform engineer workflow established default policies for authentication and rate limiting at your Gateway. The new developer-defined policies, which you will create, are intended to target your HTTPRoute and will supersede the existing policies for requests to your API endpoints, similar to your previous API key example.

The example OAS uses Kuadrant-based extensions. These extensions enable you to define routing and service protection requirements. For more details, see [OpenAPI Kuadrant extensions](https://docs.kuadrant.io/kuadrantctl/doc/openapi-kuadrant-extensions/).

#### Prerequisites

- You have installed and configured an OpenID Connect provider, such as <https://www.keycloak.org/>. 
- You have a realm, client, and users set up. This example assumes a realm in a Keycloak instance called `toystore`.
- Copy the OAS from [sample OAS for rate-limiting and OIDC](../../examples/oas-oidc.yaml) to a local location.

#### Set up an OpenID AuthPolicy

Set the following environment variables:

```bash
export openIDHost=some.keycloak.com
export oasPath=examples/oas-oidc.yaml
```

NOTE: The sample OAS has some placeholders for namespaces and domains. You will inject valid values into these placeholders based on your previous environment variables.

You can use your OAS and `kuadrantctl` to generate an `AuthPolicy` to replace the default on the Gateway as follows:

```bash
cat $oasPath | envsubst | kuadrantctl generate kuadrant authpolicy --oas -
```

If you are happy with the generated resource, you can apply it to the cluster as follows:

```bash
cat $oasPath | envsubst | kuadrantctl generate kuadrant authpolicy --oas - | kubectl apply -f -
```

You should see in the status of the `AuthPolicy` that it has been accepted and enforced:

```bash
kubectl get authpolicy -n ${devNS} toystore -o=jsonpath='{.status.conditions}'
```

On your `HTTPRoute`, you should also see it now affected by this `AuthPolicy` in the toystore namespace:

```bash
kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.status.parents[0].conditions[?(@.type=="kuadrant.io/AuthPolicyAffected")].message}'
```

#### Test your OpenID AuthPolicy

You can test your `AuthPolicy` as follows:

```bash
export ACCESS_TOKEN=$(curl -k -H "Content-Type: application/x-www-form-urlencoded" \
        -d 'grant_type=password' \
        -d 'client_id=toystore' \
        -d 'scope=openid' \
        -d 'username=bob' \
        -d 'password=p' "https://${openIDHost}/auth/realms/toystore/protocol/openid-connect/token" | jq -r '.access_token')
```        

```bash
curl -k -XPOST --write-out '%{http_code}\n' --silent --output /dev/null "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

You should see a `401` response code. Make a request with a valid bearer token as follows:

```bash
curl -k -XPOST --write-out '%{http_code}\n' --silent --output /dev/null -H "Authorization: Bearer $ACCESS_TOKEN" "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
```

You should see a `200` response code.

### Step 7 - Set up rate limiting

Lastly, you can generate your `RateLimitPolicy` to add your rate limits, based on your OAS file. Rate limiting is simplified for this walkthrough and is based on either the bearer token or the API key value. There are more advanced examples in the How-to guides on the Kuadrant documentation site, for example: [Authenticated rate limiting with JWTs and Kubernetes RBAC](https://docs.kuadrant.io/kuadrant-operator/doc/user-guides/authenticated-rl-with-jwt-and-k8s-authnz/).

 You can continue to use this sample OAS document, which includes both authentication and a rate limit:

```bash
export oasPath=examples/oas-oidc.yaml

```

Again, you should see the rate limit policy accepted and enforced:

```bash
kubectl get ratelimitpolicy -n ${devNS} toystore -o=jsonpath='{.status.conditions}'
```

On your `HTTRoute`, you should now see it is affected by the `RateLimitPolicy` in the same namespace:

```bash
kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.status.parents[0].conditions[?(@.type=="kuadrant.io/RateLimitPolicyAffected")].message}'
```

#### Test your RateLimitPolicy

You can now test your rate limiting as follows:

NOTE: You might need to wait a minute for the new rate limits to be applied. With the following requests, you should see a number of 429 responses.

##### API Key auth

```bash
for i in {1..3}
do
printf "request $i "
curl -XPOST -H 'api_key:secret' -s -k -o /dev/null -w "%{http_code}"  "https://$(kubectl get httproute toystore -n ${devNS} -o=jsonpath='{.spec.hostnames[0]}')/v1/toys"
printf "\n -- \n"
done 
```
##### OpenID Connect auth

```bash
export ACCESS_TOKEN=$(curl -k -H "Content-Type: application/x-www-form-urlencoded" \
        -d 'grant_type=password' \
        -d 'client_id=toystore' \
        -d 'scope=openid' \
        -d 'username=bob' \
        -d 'password=p' "https://${openIDHost}/auth/realms/toystore/protocol/openid-connect/token" | jq -r '.access_token')
```      

```bash
for i in {1..3}
do
curl -k -XPOST --write-out '%{http_code}\n' --silent --output /dev/null -H "Authorization: Bearer $ACCESS_TOKEN" https://$(kubectl get httproute toystore -n ${devNS}-o=jsonpath='{.spec.hostnames[0]}')/v1/toys
done
```

## Conclusion

You have completed the secure, protect, and connect walkthrough. To learn more about Kuadrant, visit <https://docs.kuadrant.io>.
