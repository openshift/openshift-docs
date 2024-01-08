// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-scale-to-zero-grace-period_{context}"]
= Configuring the scale-to-zero grace period

Knative Serving provides automatic scaling down to zero pods for applications. You can use the `scale-to-zero-grace-period` spec to define an upper bound time limit that Knative waits for scale-to-zero machinery to be in place before the last replica of an application is removed.

.Prerequisites

* You have installed {ServerlessOperatorName} and Knative Serving on your cluster.

ifdef::openshift-enterprise[]
* You have cluster administrator permissions.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have cluster or dedicated administrator permissions.
endif::[]

* You are using the default Knative Pod Autoscaler. The scale-to-zero feature is not available if you are using the Kubernetes Horizontal Pod Autoscaler.

.Procedure

* Modify the `scale-to-zero-grace-period` spec in the `KnativeServing` custom resource (CR):
+
.Example KnativeServing CR
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    autoscaler:
      scale-to-zero-grace-period: "30s" <1>
----
<1> The grace period time in seconds. The default value is 30 seconds.
