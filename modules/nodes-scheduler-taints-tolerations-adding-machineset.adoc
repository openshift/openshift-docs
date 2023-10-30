// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-taints-tolerations.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-scheduler-taints-tolerations-adding-machineset_{context}"]
= Adding taints and tolerations using a compute machine set

You can add taints to nodes using a compute machine set. All nodes associated with the `MachineSet` object are updated with the taint. Tolerations respond to taints added by a compute machine set in the same manner as taints added directly to the nodes.

.Procedure

. Add a toleration to a pod by editing the `Pod` spec to include a `tolerations` stanza:
+
.Sample pod configuration file with `Equal` operator
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
<2> The `tolerationSeconds` parameter specifies how long a pod is bound to a node before being evicted.
+
For example:
+
.Sample pod configuration file with `Exists` operator
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
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
----

. Add the taint to the `MachineSet` object:

.. Edit the `MachineSet` YAML for the nodes you want to taint or you can create a new `MachineSet` object:
+
[source,terminal]
----
$ oc edit machineset <machineset>
----

.. Add the taint to the `spec.template.spec` section:
+
.Example taint in a compute machine set specification
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: my-machineset
#...
spec:
#...
  template:
#...
    spec:
      taints:
      - effect: NoExecute
        key: key1
        value: value1
#...
----
+
This example places a taint that has the key `key1`, value `value1`, and taint effect `NoExecute` on the nodes.

.. Scale down the compute machine set to 0:
+
[source,terminal]
----
$ oc scale --replicas=0 machineset <machineset> -n openshift-machine-api
----
+
[TIP]
====
You can alternatively apply the following YAML to scale the compute machine set:

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 0
----
====
+
Wait for the machines to be removed.

.. Scale up the compute machine set as needed:
+
[source,terminal]
----
$ oc scale --replicas=2 machineset <machineset> -n openshift-machine-api
----
+
Or:
+
[source,terminal]
----
$ oc edit machineset <machineset> -n openshift-machine-api
----
+
Wait for the machines to start. The taint is added to the nodes associated with the `MachineSet` object.
