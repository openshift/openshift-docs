// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-taints-tolerations.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-scheduler-taints-tolerations-adding_{context}"]
= Adding taints and tolerations

You add tolerations to pods and taints to nodes to allow the node to control which pods should or should not be scheduled on them. For existing pods and nodes, you should add the toleration to the pod first, then add the taint to the node to avoid pods being removed from the node before you can add the toleration.

.Procedure

. Add a toleration to a pod by editing the `Pod` spec to include a `tolerations` stanza:
+
.Sample pod configuration file with an Equal operator
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1" <1>
    value: "value1"
    operator: "Equal"
    effect: "NoExecute"
    tolerationSeconds: 3600 <2>
#...
----
<1> The toleration parameters, as described in the *Taint and toleration components* table.
<2> The `tolerationSeconds` parameter specifies how long a pod can remain bound to a node before being evicted.
+
For example:
+
.Sample pod configuration file with an Exists operator
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
   tolerations:
    - key: "key1"
      operator: "Exists" <1>
      effect: "NoExecute"
      tolerationSeconds: 3600
#...
----
<1> The `Exists` operator does not take a `value`.
+
This example places a taint on `node1` that has key `key1`, value `value1`, and taint effect `NoExecute`.

. Add a taint to a node by using the following command with the parameters described in the *Taint and toleration components* table:
+
[source,terminal]
----
$ oc adm taint nodes <node_name> <key>=<value>:<effect>
----
+
For example:
+
[source,terminal]
----
$ oc adm taint nodes node1 key1=value1:NoExecute
----
+
This command places a taint on `node1` that has key `key1`, value `value1`, and effect `NoExecute`.
+
[NOTE]
====
If you add a `NoSchedule` taint to a control plane node, the node must have the `node-role.kubernetes.io/master=:NoSchedule` taint, which is added by default.

For example:

[source,yaml]
----
apiVersion: v1
kind: Node
metadata:
  annotations:
    machine.openshift.io/machine: openshift-machine-api/ci-ln-62s7gtb-f76d1-v8jxv-master-0
    machineconfiguration.openshift.io/currentConfig: rendered-master-cdc1ab7da414629332cc4c3926e6e59c
  name: my-node
#...
spec:
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
#...
----
====
+
The tolerations on the pod match the taint on the node. A pod with either toleration can be scheduled onto `node1`.

