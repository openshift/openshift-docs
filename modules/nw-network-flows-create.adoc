// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/tracking-network-flows.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-network-flows-create_{context}"]
= Adding destinations for network flows collectors

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to send network flows metadata about the pod network to a network flows collector.

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* You have a network flows collector and know the IP address and port that it listens on.

.Procedure

. Create a patch file that specifies the network flows collector type and the IP address and port information of the collectors:
+
[source,terminal]
----
spec:
  exportNetworkFlows:
    netFlow:
      collectors:
        - 192.168.1.99:2056
----

. Configure the CNO with the network flows collectors:
+
[source,terminal]
----
$ oc patch network.operator cluster --type merge -p "$(cat <file_name>.yaml)"
----
+
.Example output
[source,terminal]
----
network.operator.openshift.io/cluster patched
----

.Verification

Verification is not typically necessary. You can run the following command to confirm that Open vSwitch (OVS) on each node is configured to send network flows records to one or more collectors.

. View the Operator configuration to confirm that the `exportNetworkFlows` field is configured:
+
[source,terminal]
----
$ oc get network.operator cluster -o jsonpath="{.spec.exportNetworkFlows}"
----
+
.Example output
[source,terminal]
----
{"netFlow":{"collectors":["192.168.1.99:2056"]}}
----

. View the network flows configuration in OVS from each node:
+
[source,terminal]
----
$ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node -o jsonpath='{range@.items[*]}{.metadata.name}{"\n"}{end}');
  do ;
    echo;
    echo $pod;
    oc -n openshift-ovn-kubernetes exec -c ovnkube-controller $pod \
      -- bash -c 'for type in ipfix sflow netflow ; do ovs-vsctl find $type ; done';
done
----
+
.Example output
[source,terminal]
----
ovnkube-node-xrn4p
_uuid               : a4d2aaca-5023-4f3d-9400-7275f92611f9
active_timeout      : 60
add_id_to_interface : false
engine_id           : []
engine_type         : []
external_ids        : {}
targets             : ["192.168.1.99:2056"]

ovnkube-node-z4vq9
_uuid               : 61d02fdb-9228-4993-8ff5-b27f01a29bd6
active_timeout      : 60
add_id_to_interface : false
engine_id           : []
engine_type         : []
external_ids        : {}
targets             : ["192.168.1.99:2056"]-

...
----
