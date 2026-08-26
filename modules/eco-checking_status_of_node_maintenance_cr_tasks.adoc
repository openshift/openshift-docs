// Module included in the following assemblies:
//
//nodes/nodes/eco-node-maintenance-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="eco-checking_status_of_node_maintenance_cr_tasks_{context}"]
= Checking status of current NodeMaintenance CR tasks

You can check the status of current `NodeMaintenance` CR tasks.

.Prerequisites

* Install the {product-title} CLI `oc`.
* Log in as a user with `cluster-admin` privileges.

.Procedure

* Check the status of current node maintenance tasks, for example the `NodeMaintenance` CR or `nm` object, by running the following command:
+
[source,terminal]
----
$ oc get nm -o yaml
----
+
.Example output
+
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: nodemaintenance.medik8s.io/v1beta1
  kind: NodeMaintenance
  metadata:
...
  spec:
    nodeName: node-1.example.com
    reason: Node maintenance
  status:
    drainProgress: 100   <1>
    evictionPods: 3   <2>
    lastError: "Last failure message" <3>
    lastUpdate: "2022-06-23T11:43:18Z" <4>
    phase: Succeeded
    totalpods: 5 <5>
...
----
<1> The percentage completion of draining the node.
<2> The number of pods scheduled for eviction.
<3> The latest eviction error, if any.
<4> The last time the status was updated.
<5> The total number of pods before the node entered maintenance mode.
