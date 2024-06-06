// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring
// * post_installation_configuration/cluster-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-pod-disruption-configuring_{context}"]
= Specifying the number of pods that must be up with pod disruption budgets

You can use a `PodDisruptionBudget` object to specify the minimum number or
percentage of replicas that must be up at a time.

.Procedure

To configure a pod disruption budget:

. Create a YAML file with the an object definition similar to the following:
+
[source,yaml]
----
apiVersion: policy/v1 <1>
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2  <2>
  selector:  <3>
    matchLabels:
      name: my-pod
----
<1> `PodDisruptionBudget` is part of the `policy/v1` API group.
<2> The minimum number of pods that must be available simultaneously. This can
be either an integer or a string specifying a percentage, for example, `20%`.
<3> A label query over a set of resources. The result of `matchLabels` and
 `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project.
+
Or:
+
[source,yaml]
----
apiVersion: policy/v1 <1>
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  maxUnavailable: 25% <2>
  selector: <3>
    matchLabels:
      name: my-pod
----
<1> `PodDisruptionBudget` is part of the `policy/v1` API group.
<2> The maximum number of pods that can be unavailable simultaneously. This can
be either an integer or a string specifying a percentage, for example, `20%`.
<3> A label query over a set of resources. The result of `matchLabels` and
 `matchExpressions` are logically conjoined. Leave this parameter blank, for example `selector {}`, to select all pods in the project.

. Run the following command to add the object to project:
+
[source,terminal]
----
$ oc create -f </path/to/file> -n <project_name>
----
