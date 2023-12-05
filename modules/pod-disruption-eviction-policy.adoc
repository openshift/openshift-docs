// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring
// * post_installation_configuration/cluster-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="pod-disruption-eviction-policy_{context}"]
= Specifying the eviction policy for unhealthy pods

When you use pod disruption budgets (PDBs) to specify how many pods must be available simultaneously, you can also define the criteria for how unhealthy pods are considered for eviction.

You can choose one of the following policies:

IfHealthyBudget:: Running pods that are not yet healthy can be evicted only if the guarded application is not disrupted.

AlwaysAllow:: Running pods that are not yet healthy can be evicted regardless of whether the criteria in the pod disruption budget is met. This policy can help evict malfunctioning applications, such as ones with pods stuck in the `CrashLoopBackOff` state or failing to report the `Ready` status.
+
[NOTE]
====
It is recommended to set the `unhealthyPodEvictionPolicy` field to `AlwaysAllow` in the `PodDisruptionBudget` object to support the eviction of misbehaving applications during a node drain. The default behavior is to wait for the application pods to become healthy before the drain can proceed.
====

.Procedure

. Create a YAML file that defines a `PodDisruptionBudget` object and specify the unhealthy pod eviction policy:
+
.Example `pod-disruption-budget.yaml` file
[source,yaml]
----
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: my-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      name: my-pod
  unhealthyPodEvictionPolicy: AlwaysAllow <1>
----
<1> Choose either `IfHealthyBudget` or `AlwaysAllow` as the unhealthy pod eviction policy. The default is `IfHealthyBudget` when the `unhealthyPodEvictionPolicy` field is empty.

. Create the `PodDisruptionBudget` object by running the following command:
+
[source,terminal]
----
$ oc create -f pod-disruption-budget.yaml
----

With a PDB that has the `AlwaysAllow` unhealthy pod eviction policy set, you can now drain nodes and evict the pods for a malfunctioning application guarded by this PDB.
