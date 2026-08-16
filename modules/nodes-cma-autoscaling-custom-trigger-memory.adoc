// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-trigger.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-trigger-memory_{context}"]
= Understanding the memory trigger

You can scale pods based on memory metrics. This trigger uses cluster metrics as the source for metrics.

The custom metrics autoscaler scales the pods associated with an object to maintain the average memory usage that you specify. The autoscaler increases and decreases the number of replicas between the minimum and maximum numbers to maintain the specified memory utilization across all pods. The memory trigger considers the memory utilization of entire pod. If the pod has multiple containers, the memory utilization is the sum of all of the containers.

[NOTE]
====
* This trigger cannot be used with the `ScaledJob` custom resource.
* When using a memory trigger to scale an object, the object does not scale to `0`, even if you are using multiple triggers.
====

.Example scaled object with a memory target
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: memory-scaledobject
  namespace: my-namespace
spec:
# ...
  triggers:
  - type: memory <1>
    metricType: Utilization <2>
    metadata:
      value: '60' <3>
      containerName: api <4>
----
<1> Specifies memory as the trigger type.
<2> Specifies the type of metric to use, either `Utilization` or `AverageValue`.
<3> Specifies the value that triggers scaling. Must be specified as a quoted string value.
* When using `Utilization`, the target value is the average of the resource metrics across all relevant pods, represented as a percentage of the requested value of the resource for the pods.
* When using `AverageValue`, the target value is the average of the metrics across all relevant pods.
<4> Optional: Specifies an individual container to scale, based on the memory utilization of only that container, rather than the entire pod. In this example, only the container named `api` is to be scaled.

