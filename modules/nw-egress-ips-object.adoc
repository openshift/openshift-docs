// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/assigning-egress-ips-ovn.adoc

[id="nw-egress-ips-object_{context}"]
= EgressIP object

The following YAML describes the API for the `EgressIP` object. The scope of the object is cluster-wide; it is not created in a namespace.

[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: <name> <1>
spec:
  egressIPs: <2>
  - <ip_address>
  namespaceSelector: <3>
    ...
  podSelector: <4>
    ...
----
<1> The name for the `EgressIPs` object.

<2> An array of one or more IP addresses.

<3> One or more selectors for the namespaces to associate the egress IP addresses with.

<4> Optional: One or more selectors for pods in the specified namespaces to associate egress IP addresses with. Applying these selectors allows for the selection of a subset of pods within a namespace.

The following YAML describes the stanza for the namespace selector:

.Namespace selector stanza
[source,yaml]
----
namespaceSelector: <1>
  matchLabels:
    <label_name>: <label_value>
----
<1> One or more matching rules for namespaces. If more than one match rule is provided, all matching namespaces are selected.

The following YAML describes the optional stanza for the pod selector:

.Pod selector stanza
[source,yaml]
----
podSelector: <1>
  matchLabels:
    <label_name>: <label_value>
----
<1> Optional: One or more matching rules for pods in the namespaces that match the specified `namespaceSelector` rules. If specified, only pods that match are selected. Others pods in the namespace are not selected.

In the following example, the `EgressIP` object associates the `192.168.126.11` and `192.168.126.102` egress IP addresses with pods that have the `app` label set to `web` and are in the namespaces that have the `env` label set to `prod`:

.Example `EgressIP` object
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group1
spec:
  egressIPs:
  - 192.168.126.11
  - 192.168.126.102
  podSelector:
    matchLabels:
      app: web
  namespaceSelector:
    matchLabels:
      env: prod
----

In the following example, the `EgressIP` object associates the `192.168.127.30` and `192.168.127.40` egress IP addresses with any pods that do not have the `environment` label set to `development`:

.Example `EgressIP` object
[source,yaml]
----
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group2
spec:
  egressIPs:
  - 192.168.127.30
  - 192.168.127.40
  namespaceSelector:
    matchExpressions:
    - key: environment
      operator: NotIn
      values:
      - development
----
