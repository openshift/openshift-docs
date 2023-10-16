// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

[id="nw-network-flows-object_{context}"]
= Network object configuration for tracking network flows

The fields for configuring network flows collectors in the Cluster Network Operator (CNO) are shown in the following table:

.Network flows configuration
[cols=".^2,.^2,.^6a",options="header"]
|====
|Field|Type|Description

|`metadata.name`
|`string`
|The name of the CNO object. This name is always `cluster`.

|`spec.exportNetworkFlows`
|`object`
|One or more of `netFlow`, `sFlow`, or `ipfix`.

|`spec.exportNetworkFlows.netFlow.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.

|`spec.exportNetworkFlows.sFlow.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.

|`spec.exportNetworkFlows.ipfix.collectors`
|`array`
|A list of IP address and network port pairs for up to 10 collectors.
|====

After applying the following manifest to the CNO, the Operator configures Open vSwitch (OVS) on each node in the cluster to send network flows records to the NetFlow collector that is listening at `192.168.1.99:2056`.

.Example configuration for tracking network flows
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  exportNetworkFlows:
    netFlow:
      collectors:
        - 192.168.1.99:2056
----
