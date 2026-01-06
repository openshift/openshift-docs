# TLS

A Kuadrant TLSPolicy custom resource:

1. Targets Gateway API networking resources [Gateways](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.Gateway) to provide tls for gateway listeners by managing the lifecycle of tls certificates using [`CertManager`](https://cert-manager.io).

## How it works

[//]: # (ToDo mnairn)

### The TLSPolicy custom resource

#### Overview

[//]: # (ToDo mnairn)

The `TLSPolicy` spec includes the following parts:

* A reference to an existing Gateway API resource (`spec.targetRef`)

#### High-level example and field definition

[//]: # (ToDo mnairn)

```yaml
apiVersion: kuadrant.io/v1alpha1
kind: TLSPolicy
metadata:
  name: my-tls-policy
spec:
  # reference to an existing networking resource to attach the policy to
  # it can only be a Gateway API Gateway resource
  # it can only refer to objects in the same namespace as the TLSPolicy
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: mygateway
```

Check out the [API reference](reference/tlspolicy.md) for a full specification of the TLSPolicy CRD.

## Using the TLSPolicy

[//]: # (ToDo mnairn)

### Targeting a Gateway networking resource

When a TLSPolicy targets a Gateway, the policy will be enforced on all gateway listeners that have a valid TLS section.

Target a Gateway by setting the `spec.targetRef` field of the TLSPolicy as follows:

```yaml
apiVersion: kuadrant.io/v1beta2
kind: TLSPolicy
metadata:
  name: <TLSPolicy name>
spec:
  targetRef:
    group: gateway.networking.k8s.io
    kind: Gateway
    name: <Gateway Name>
```

### Examples

Check out the following user guides for examples of using the Kuadrant TLSPolicy:

[//]: # (ToDo mnairn)

### Known limitations

[//]: # (ToDo mnairn)
