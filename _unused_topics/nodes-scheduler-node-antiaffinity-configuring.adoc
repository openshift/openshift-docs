// Module included in the following assemblies:
//
// * nodes/nodes-scheduler-node-affinity.adoc

[id="nodes-scheduler-node-affinity-configuring_{context}"]
= Configuring node affinity rules

You can configure two types of node affinity rules: required and preferred.

==  Configuring a required node affinity rule

Required rules *must* be met before a pod can be scheduled on a node.

.Procedure

The following steps demonstrate a simple configuration that creates a node and a pod that the scheduler is required to place on the node.

. Add a label to a node using the `oc label node` command:
+
----
$ oc label node node1 e2e-az-name=e2e-az1
----
+
[TIP]
====
You can alternatively apply the following YAML to add the label:

[source,yaml]
----
kind: Node
apiVersion: v1
metadata:
  name: <node_name>
  labels:
    e2e-az-name: e2e-az1
----
====

. In the pod specification, use the `nodeAffinity` stanza to configure the `requiredDuringSchedulingIgnoredDuringExecution` parameter:
+
.. Specify the key and values that must be met. If you want the new pod to be scheduled on the node you edited, use the same `key` and `value` parameters as the label in the node.
+
.. Specify an `operator`. The operator can be `In`, `NotIn`, `Exists`, `DoesNotExist`, `Lt`, or `Gt`. For example, use the operator `In` to require the label to be in the node:
+
----
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: e2e-az-name
            operator: In
            values:
            - e2e-az1
            - e2e-az2
----

. Create the pod:
+
----
$ oc create -f e2e-az2.yaml
----

== Configuring a Preferred Node Affinity Rule

Preferred rules specify that, if the rule is met, the scheduler tries to enforce the rules, but does not guarantee enforcement.

.Procedure

The following steps demonstrate a simple configuration that creates a node and a pod that the scheduler tries to place on the node.

. Add a label to a node using the `oc label node` command:
+
----
$ oc label node node1 e2e-az-name=e2e-az3
----

. In the pod specification, use the `nodeAffinity` stanza to configure the `preferredDuringSchedulingIgnoredDuringExecution` parameter:
+
.. Specify a weight for the node, as a number 1-100. The node with highest weight is preferred.
+
.. Specify the key and values that must be met. If you want the new pod to be scheduled on the node you edited, use the same `key` and `value` parameters as the label in the node:
+
----
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: e2e-az-name
            operator: In
            values:
            - e2e-az3
----

. Specify an `operator`. The operator can be `In`, `NotIn`, `Exists`, `DoesNotExist`, `Lt`, or `Gt`. For example, use the operator `In` to require the label to be in the node.

. Create the pod.
+
----
$ oc create -f e2e-az3.yaml
----
