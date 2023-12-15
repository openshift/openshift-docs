// Module included in the following assemblies:
//
// * networking/multiple_networks/configuring-multi-network-policy.adoc
// * networking/network_policy/creating-network-policy.adoc

:name: network
:role: admin
ifeval::["{context}" == "configuring-multi-network-policy"]
:multi:
:name: multi-network
:role: cluster-admin
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="nw-networkpolicy-deny-all-multi-network-policy_{context}"]
= Creating a default deny all {name} policy

This is a fundamental policy, blocking all cross-pod networking other than network traffic allowed by the configuration of other deployed network policies. This procedure enforces a default `deny-by-default` policy.

[NOTE]
====
If you log in with a user with the `cluster-admin` role, then you can create a network policy in any namespace in the cluster.
====

.Prerequisites

* Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin or the OpenShift SDN network plugin with `mode: NetworkPolicy` set. This mode is the default for OpenShift SDN.
* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `{role}` privileges.
* You are working in the namespace that the {name} policy applies to.

.Procedure

. Create the following YAML that defines a `deny-by-default` policy to deny ingress from all pods in all namespaces. Save the YAML in the `deny-by-default.yaml` file:
+
[source,yaml]
----
ifdef::multi[]
apiVersion: k8s.cni.cncf.io/v1beta1
kind: MultiNetworkPolicy
metadata:
  name: deny-by-default
  namespace: default <1>
  annotations:
    k8s.v1.cni.cncf.io/policy-for: <network_name> <2>
spec:
  podSelector: {} <3>
  ingress: [] <4>
endif::multi[]
ifndef::multi[]
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: deny-by-default
  namespace: default <1>
spec:
  podSelector: {} <2>
  ingress: [] <3>
endif::multi[]
----
ifdef::multi[]
<1> `namespace: default` deploys this policy to the `default` namespace.
<2> `network_name`: specifies the name of a network attachment definition.
<3> `podSelector:` is empty, this means it matches all the pods. Therefore, the policy applies to all pods in the default namespace.
<4> There are no `ingress` rules specified. This causes incoming traffic to be dropped to all pods.
endif::multi[]
ifndef::multi[]
<1> `namespace: default` deploys this policy to the `default` namespace.
<2> `podSelector:` is empty, this means it matches all the pods. Therefore, the policy applies to all pods in the default namespace.
<3> There are no `ingress` rules specified. This causes incoming traffic to be dropped to all pods.
endif::multi[]
+
. Apply the policy by entering the following command:
+
[source,terminal]
----
$ oc apply -f deny-by-default.yaml
----
+
.Example output
[source,terminal]
----
ifndef::multi[]
networkpolicy.networking.k8s.io/deny-by-default created
endif::multi[]
ifdef::multi[]
multinetworkpolicy.k8s.cni.cncf.io/deny-by-default created
endif::multi[]
----

ifdef::multi[]
:!multi:
endif::multi[]
:!name:
:!role:
