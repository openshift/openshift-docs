// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-pausing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-pausing-workload_{context}"]
= Pausing a custom metrics autoscaler

You can pause the autoscaling of a scaled object by adding the `autoscaling.keda.sh/paused-replicas` annotation to the custom metrics autoscaler for that scaled object. The custom metrics autoscaler scales the replicas for that workload to the specified value and pauses autoscaling until the annotation is removed.

[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4"
# ...
----

.Procedure

. Use the following command to edit the `ScaledObject` CR for your workload:
+
[source,terminal]
----
$ oc edit ScaledObject scaledobject
----

. Add the `autoscaling.keda.sh/paused-replicas` annotation with any value:
+
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "4" <1>
  creationTimestamp: "2023-02-08T14:41:01Z"
  generation: 1
  name: scaledobject
  namespace: my-project
  resourceVersion: '65729'
  uid: f5aec682-acdf-4232-a783-58b5b82f5dd0
----
<1> Specifies that the Custom Metrics Autoscaler Operator is to scale the replicas to the specified value and stop autoscaling.

