// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-taints-tolerations.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-scheduler-taints-tolerations-removing_{context}"]
= Removing taints and tolerations

You can remove taints from nodes and tolerations from pods as needed. You should add the toleration to the pod first, then add the taint to the node to avoid pods being removed from the node before you can add the toleration.

.Procedure

To remove taints and tolerations:

. To remove a taint from a node:
+
[source,terminal]
----
$ oc adm taint nodes <node-name> <key>-
----
+
For example:
+
[source,terminal]
----
$ oc adm taint nodes ip-10-0-132-248.ec2.internal key1-
----
+
.Example output
[source,terminal]
----
node/ip-10-0-132-248.ec2.internal untainted
----

. To remove a toleration from a pod, edit the `Pod` spec to remove the toleration:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key2"
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
----
