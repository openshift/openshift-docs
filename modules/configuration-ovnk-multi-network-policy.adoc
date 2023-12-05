// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-additional-network.adoc

:_mod-docs-content-type: CONCEPT
[id="compatibility-with-multi-network-policy_{context}"]
= Compatibility with multi-network policy

The multi-network policy API, which is provided by the `MultiNetworkPolicy` custom resource definition (CRD) in the `k8s.cni.cncf.io` API group, is compatible with an OVN-Kubernetes secondary network. When defining a network policy, the network policy rules that can be used depend on whether the OVN-Kubernetes secondary network defines the `subnets` field. Refer to the following table for details:

.Supported multi-network policy selectors based on `subnets` CNI configuration
[cols=".^3,.^7",options="header"]
|====
a|`subnets` field specified|Allowed multi-network policy selectors

|
Yes
a|
* `podSelector` and `namespaceSelector`
* `ipBlock`

|
No
a|
* `ipBlock`

|====

For example, the following multi-network policy is valid only if the `subnets` field is defined in the additional network CNI configuration for the additional network named `blue2`:

.Example multi-network policy that uses a pod selector
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: allow-same-namespace
  annotations:
    k8s.v1.cni.cncf.io/policy-for: blue2
spec:
  podSelector:
  ingress:
  - from:
    - podSelector: {}
----

The following example uses the `ipBlock` network policy selector, which is always valid for an OVN-Kubernetes additional network:

.Example multi-network policy that uses an IP block selector
[source,yaml]
----
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name:  ingress-ipblock
  annotations:
    k8s.v1.cni.cncf.io/policy-for: default/flatl2net
spec:
  podSelector:
    matchLabels:
      name: access-control
  policyTypes:
  - Ingress
  ingress:
  - from:
    - ipBlock:
        cidr: 10.200.0.0/30
----
