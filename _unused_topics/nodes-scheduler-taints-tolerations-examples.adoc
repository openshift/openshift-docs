// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-taints-tolerations.adoc

[id="nodes-scheduler-taints-tolerations-examples_{context}"]
= Example taint and toleration scenarios

Taints and tolerations are a flexible way to steer pods away from nodes or evict pods that should not be running on a node. A few of typical scenarios are:

* Dedicating a node for a user
* Binding a user to a node
* Dedicating nodes with special hardware

[id="nodes-scheduler-taints-tolerations-examples-user_{context}"]
== Dedicating a Node for a User

You can specify a set of nodes for exclusive use by a particular set of users.

.Procedure

To specify dedicated nodes:

. Add a taint to those nodes:
+
For example:
+
----
$ oc adm taint nodes node1 dedicated=groupName:NoSchedule
----
+
[TIP]
====
You can alternatively apply the following YAML to add the taint:

[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    ...
spec:
  taints:
    - key: dedicated
      value: groupName
      effect: NoSchedule
    ...
----
====

. Add a corresponding toleration to the pods by writing a custom admission controller.
+
Only the pods with the tolerations are allowed to use the dedicated nodes.

[id="nodes-scheduler-taints-tolerations-examples-binding_{context}"]
== Binding a User to a Node

You can configure a node so that particular users can use only the dedicated nodes.

.Procedure

To configure a node so that users can use only that node:

. Add a taint to those nodes:
+
For example:
+
----
$ oc adm taint nodes node1 dedicated=groupName:NoSchedule
----
+
[TIP]
====
You can alternatively apply the following YAML to add the taint:

[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    ...
spec:
  taints:
    - key: dedicated
      value: groupName
      effect: NoSchedule
    ...
----
====

. Add a corresponding toleration to the pods by writing a custom admission controller.
+
The admission controller should add a node affinity to require that the pods can only schedule onto nodes labeled with the `key:value` label (`dedicated=groupName`).

. Add a label similar to the taint (such as the `key:value` label) to the dedicated nodes.

[id="nodes-scheduler-taints-tolerations-examples-special_{context}"]
== Nodes with Special Hardware

In a cluster where a small subset of nodes have specialized hardware (for example GPUs), you can use taints and tolerations to keep pods that do not need the specialized hardware off of those nodes, leaving the nodes for pods that do need the specialized hardware. You can also require pods that need specialized hardware to use specific nodes.

.Procedure

To ensure pods are blocked from the specialized hardware:

. Taint the nodes that have the specialized hardware using one of the following commands:
+
----
$ oc adm taint nodes <node-name> disktype=ssd:NoSchedule
$ oc adm taint nodes <node-name> disktype=ssd:PreferNoSchedule
----
+
[TIP]
====
You can alternatively apply the following YAML to add the taint:

[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    ...
spec:
  taints:
    - key: disktype
      value: ssd
      effect: PreferNoSchedule
    ...
----
====

. Adding a corresponding toleration to pods that use the special hardware using an admission controller.

For example, the admission controller could use some characteristic(s) of the pod to determine that the pod should be allowed to use the special nodes by adding a toleration.

To ensure pods can only use the specialized hardware, you need some additional mechanism. For example, you could label the nodes that have the special hardware and use node affinity on the pods that need the hardware.
