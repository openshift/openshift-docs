// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-pausing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-pausing-restart_{context}"]
= Restarting the custom metrics autoscaler for a scaled object

You can restart a paused custom metrics autoscaler by removing the `autoscaling.keda.sh/paused-replicas` annotation for that `ScaledObject`.

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

. Remove the `autoscaling.keda.sh/paused-replicas` annotation.
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
<1> Remove this annotation to restart a paused custom metrics autoscaler.
