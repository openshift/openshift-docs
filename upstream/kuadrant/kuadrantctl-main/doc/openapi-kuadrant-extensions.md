# OpenAPI 3.0.x Kuadrant extensions

This reference information shows examples of how to add Kuadrant extensions at the `info`, path, and operation level in an OpenAPI 3.0.x definition. 

## Info-level Kuadrant extension

You can add a Kuadrant extension at the `info` level of an OpenAPI definition. The following example shows an extension added for a `petstore` app:

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

## Path-level Kuadrant extension

You can add a Kuadrant extension at the path level of an OpenAPI definition.
This configuration at the path level is the default when there is no operation-level configuration. 
The following example shows an extension added for a `/cat` path:

```yaml
paths:
  /cat:
    x-kuadrant:  ## Path-level Kuadrant extension
      disable: true  ## Remove from the HTTPRoute. Optional. Default: false
      pathMatchType: Exact ## Specifies how to match against the path value. Valid values: [Exact;PathPrefix]. Optional. Default: Exact
      backendRefs:  ## Backend references to be included in the HTTPRoute. []gateway.networking.k8s.io/v1beta1.HTTPBackendRef. Optional.
        - name: petstore
          port: 80
          namespace: petstore
      rate_limit:  ## Rate limit configuration. Optional.
        rates:   ## Kuadrant API []github.com/kuadrant/kuadrant-operator/api/v1beta2.Rate
          - limit: 1
            duration: 10
            unit: second
        counters:   ## Kuadrant API []github.com/kuadrant/kuadrant-operator/api/v1beta2.CountextSelector
          - auth.identity.username
        when:   ## Kuadrant API []github.com/kuadrant/kuadrant-operator/api/v1beta2.WhenCondition
          - selector: metadata.filter_metadata.envoy\.filters\.http\.ext_authz.identity.userid
            operator: eq
            value: alice
```

## Operation-level Kuadrant extension

You can add a Kuadrant extension at the operation level of an OpenAPI definition. This extension uses the same schema as the path-level Kuadrant extension. The following example shows an extension added for a `get` operation:

```yaml
paths:
  /cat:
    get:
      x-kuadrant:  ## Operation-level Kuadrant extension
        disable: true  ## Remove from the HTTPRoute. Optional. Default: path level "disable" value.
        pathMatchType: Exact ## Specifies how to match against the path value. Valid values: [Exact;PathPrefix]. Optional. Default: Exact.
        backendRefs:  ## Backend references to be included in the HTTPRoute. Optional.
          - name: petstore
            port: 80
            namespace: petstore
        rate_limit:  ## Rate limit configuration. Optional.
          rates:   ## Kuadrant API github.com/kuadrant/kuadrant-operator/api/v1beta2.Rate
            - limit: 1
              duration: 10
              unit: second
          counters:   ## Kuadrant API github.com/kuadrant/kuadrant-operator/api/v1beta2.CountextSelector
            - auth.identity.username
          when:   ## Kuadrant API github.com/kuadrant/kuadrant-operator/api/v1beta2.WhenCondition
            - selector: metadata.filter_metadata.envoy\.filters\.http\.ext_authz.identity.userid
              operator: eq
              value: alice
```
