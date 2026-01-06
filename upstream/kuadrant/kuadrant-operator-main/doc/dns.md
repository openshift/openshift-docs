# Kuadrant DNS

A Kuadrant DNSPolicy custom resource:

1. Targets Gateway API networking resources [Gateways](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.Gateway) to provide dns management by managing the lifecycle of dns records in external dns providers such as AWS Route53 and Google DNS.

## How it works

A DNSPolicy and its targeted Gateway API networking resource contain all the statements to configure both the ingress gateway and the external DNS service. 
The needed dns names are gathered from the listener definitions and the IPAdresses | CNAME hosts are gathered from the status block of the gateway resource.

### The DNSPolicy custom resource

#### Overview

The `DNSPolicy` spec includes the following parts:

* A reference to an existing Gateway API resource (`spec.targetRef`)
* DNS Routing Strategy (`spec.routingStrategy`)
* LoadBalancing specification (`spec.loadBalancing`)
* HealthCheck specification (`spec.healthCheck`)

#### High-level example and field definition

```yaml
apiVersion: kuadrant.io/v1alpha1
kind: DNSPolicy
metadata:
  name: my-dns-policy
spec:
  # reference to an existing networking resource to attach the policy to
  # it can only be a Gateway API Gateway resource
  # it can only refer to objects in the same namespace as the DNSPolicy
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: mygateway
   
  # (optional) routing strategy to use when creating DNS records, defaults to `loadbalanced`
  # determines what DNS records are created in the DNS provider
  # check out Kuadrant RFC 0005 https://github.com/Kuadrant/architecture/blob/main/rfcs/0005-single-cluster-dnspolicy.md to learn more about the Routing Strategy field
  # One-of: simple, loadbalanced.
  routingStrategy: loadbalanced

  # (optional) loadbalancing specification
  # use it for providing the specification of how dns will be configured in order to provide balancing of load across multiple clusters when using the `loadbalanced` routing strategy
  # Primary use of this is for multi cluster deployments
  # check out Kuadrant RFC 0003 https://github.com/Kuadrant/architecture/blob/main/rfcs/0003-dns-policy.md to learn more about the options that can be used in this field
  loadBalancing:
    # (optional) weighted specification
    # use it to control the weight value applied to records
    weighted:
      # use it to change the weight of a record based on labels applied to the target meta resource i.e. Gateway in a single cluster context or ManagedCluster in multi cluster with OCM
      custom:
        - weight: 200
          selector:
            matchLabels:
              kuadrant.io/lb-attribute-custom-weight: AWS
      # (optional) weight value that will be applied to weighted dns records by default. Integer greater than 0 and no larger than the maximum value accepted by the target dns provider, defaults to `120` 
      defaultWeight: 100
    # (optional) geo specification
    # use it to control the geo value applied to records 
    geo:
      # (optional) default geo to be applied to records 
      defaultGeo: IE

  # (optional) health check specification
  # health check probes with the following specification will be created for each DNS target
  healthCheck:
    allowInsecureCertificates: true
    endpoint: /
    expectedResponses:
      - 200
      - 201
      - 301
    failureThreshold: 5
    port: 443
    protocol: https
```

Check out the [API reference](reference/dnspolicy.md) for a full specification of the DNSPolicy CRD.

## Using the DNSPolicy

### DNS Provider and ManagedZone Setup

A DNSPolicy acts against a target Gateway by processing its listeners for hostnames that it can create dns records for. 
In order for it to do this, it must know about dns providers, and what domains these dns providers are currently hosting.
This is done through the creation of ManagedZones and dns provider secrets containing the credentials for the dns provider account.

If for example a Gateway is created with a listener with a hostname of `echo.apps.hcpapps.net`:
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gw
spec:
  listeners:
    - allowedRoutes:
        namespaces:
          from: All
      name: api
      hostname: echo.apps.hcpapps.net
      port: 80
      protocol: HTTP
```

In order for the DNSPolicy to act upon that listener, a ManagedZone must exist for that hostnames' domain.

```yaml
apiVersion: kuadrant.io/v1alpha1
kind: ManagedZone
metadata:
  name: apps.hcpapps.net
spec:
  domainName: apps.hcpapps.net
  description: "apps.hcpapps.net managed domain"
  dnsProviderSecretRef:
    name: my-aws-credentials
```

The managed zone references a secret containing the external DNS provider services credentials.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-aws-credentials
  namespace: <ManagedZone Namespace>
data:
  AWS_ACCESS_KEY_ID: <AWS_ACCESS_KEY_ID>
  AWS_REGION: <AWS_REGION>
  AWS_SECRET_ACCESS_KEY: <AWS_SECRET_ACCESS_KEY>
type: kuadrant.io/aws
```

### Targeting a Gateway networking resource

When a DNSPolicy targets a Gateway, the policy will be enforced on all gateway listeners that have a matching ManagedZone.

Target a Gateway by setting the `spec.targetRef` field of the DNSPolicy as follows:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: DNSPolicy
metadata:
  name: <DNSPolicy name>
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: <Gateway Name>
```

### DNSRecord Resource

The DNSPolicy will create a DNSRecord resource for each listener hostname with a suitable ManagedZone configured. The DNSPolicy resource uses the status of the Gateway to determine what dns records need to be created based on the clusters it has been placed onto.

Given the following multi cluster gateway status:
```yaml
status:
  addresses:
    - type: kuadrant.io/MultiClusterIPAddress
      value: kind-mgc-workload-1/172.31.201.1
    - type: kuadrant.io/MultiClusterIPAddress
      value: kind-mgc-workload-2/172.31.202.1
  listeners:
    - attachedRoutes: 1
      conditions: []
      name: kind-mgc-workload-1.api
      supportedKinds: []
    - attachedRoutes: 1
      conditions: []
      name: kind-mgc-workload-2.api
      supportedKinds: []        
```

A DNSPolicy targeting this gateway would create an appropriate DNSRecord based on the routing strategy selected.

#### loadbalanced
```yaml
apiVersion: kuadrant.io/v1alpha1
kind: DNSRecord
metadata:
  name: echo.apps.hcpapps.net
  namespace: <Gateway Namespace>
spec:
  endpoints:
    - dnsName: 24osuu.lb-2903yb.echo.apps.hcpapps.net
      recordTTL: 60
      recordType: A
      targets:
        - 172.31.202.1
    - dnsName: default.lb-2903yb.echo.apps.hcpapps.net
      providerSpecific:
        - name: weight
          value: "120"
      recordTTL: 60
      recordType: CNAME
      setIdentifier: 24osuu.lb-2903yb.echo.apps.hcpapps.net
      targets:
        - 24osuu.lb-2903yb.echo.apps.hcpapps.net
    - dnsName: default.lb-2903yb.echo.apps.hcpapps.net
      providerSpecific:
        - name: weight
          value: "120"
      recordTTL: 60
      recordType: CNAME
      setIdentifier: lrnse3.lb-2903yb.echo.apps.hcpapps.net
      targets:
        - lrnse3.lb-2903yb.echo.apps.hcpapps.net
    - dnsName: echo.apps.hcpapps.net
      recordTTL: 300
      recordType: CNAME
      targets:
        - lb-2903yb.echo.apps.hcpapps.net
    - dnsName: lb-2903yb.echo.apps.hcpapps.net
      providerSpecific:
        - name: geo-country-code
          value: '*'
      recordTTL: 300
      recordType: CNAME
      setIdentifier: default
      targets:
        - default.lb-2903yb.echo.apps.hcpapps.net
    - dnsName: lrnse3.lb-2903yb.echo.apps.hcpapps.net
      recordTTL: 60
      recordType: A
      targets:
        - 172.31.201.1
  managedZone:
    name: apps.hcpapps.net   
```

After DNSRecord reconciliation the listener hostname should be resolvable through dns:

```bash
dig echo.apps.hcpapps.net +short
lb-2903yb.echo.apps.hcpapps.net.
default.lb-2903yb.echo.apps.hcpapps.net.
lrnse3.lb-2903yb.echo.apps.hcpapps.net.
172.31.201.1
```

#### simple
```yaml
apiVersion: kuadrant.io/v1alpha1
kind: DNSRecord
metadata:
  name: echo.apps.hcpapps.net
  namespace: <Gateway Namespace>
spec:
  endpoints:
    - dnsName: echo.apps.hcpapps.net
      recordTTL: 60
      recordType: A
      targets:
        - 172.31.201.1
        - 172.31.202.1
  managedZone:
    name: apps.hcpapps.net   
```

After DNSRecord reconciliation the listener hostname should be resolvable through dns:

```bash
dig echo.apps.hcpapps.net +short
172.31.201.1
```

### Examples

Check out the following user guides for examples of using the Kuadrant DNSPolicy:

[//]: # (ToDo mnairn)
[//]: # (* [Multicluster LoadBalanced DNSPolicy]&#40;../how-to/multicluster-loadbalanced-dnspolicy.md&#41;)

### Known limitations

* One Gateway can only be targeted by one DNSPolicy.
* DNSPolicies can only target Gateways defined within the same namespace of the DNSPolicy.
