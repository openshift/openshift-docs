// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-trigger.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-trigger-cpu_{context}"]
= Understanding the CPU trigger

You can scale pods based on CPU metrics. This trigger uses cluster metrics as the source for metrics.

The custom metrics autoscaler scales the pods associated with an object to maintain the CPU usage that you specify. The autoscaler increases or decreases the number of replicas between the minimum and maximum numbers to maintain the specified CPU utilization across all pods. The memory trigger considers the memory utilization of the entire pod. If the pod has multiple containers, the memory trigger considers the total memory utilization of all containers in the pod.

[NOTE]
====
* This trigger cannot be used with the `ScaledJob` custom resource.
* When using a memory trigger to scale an object, the object does not scale to `0`, even if you are using multiple triggers.
====

.Example scaled object with a CPU target
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cpu-scaledobject
  namespace: my-namespace
spec:
# ...
  triggers:
  - type: cpu <1>
    metricType: Utilization <2>
    metadata:
      value: '60' <3>
  minReplicaCount: 1 <4>
----
<1> Specifies CPU as the trigger type.
<2> Specifies the type of metric to use, either `Utilization` or `AverageValue`.
<3> Specifies the value that triggers scaling. Must be specified as a quoted string value.
* When using `Utilization`, the target value is the average of the resource metrics across all relevant pods, represented as a percentage of the requested value of the resource for the pods.
* When using `AverageValue`, the target value is the average of the metrics across all relevant pods.
<4> Specifies the minimum number of replicas when scaling down. For a CPU trigger, enter a value of `1` or greater, because the HPA cannot scale to zero if you are using only CPU metrics.
