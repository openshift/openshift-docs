// Module included in the following assemblies:
//
// * /serverless/admin_guide/serverless-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-enable-scale-to-zero_{context}"]
= Enabling scale-to-zero

You can use the `enable-scale-to-zero` spec to enable or disable scale-to-zero globally for applications on the cluster.

.Prerequisites

* You have installed {ServerlessOperatorName} and Knative Serving on your cluster.

ifdef::openshift-enterprise[]
* You have cluster administrator permissions.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have cluster or dedicated administrator permissions.
endif::[]

* You are using the default Knative Pod Autoscaler. The scale to zero feature is not available if you are using the Kubernetes Horizontal Pod Autoscaler.

.Procedure

* Modify the `enable-scale-to-zero` spec in the `KnativeServing` custom resource (CR):
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
      enable-scale-to-zero: "false" <1>
----
<1> The `enable-scale-to-zero` spec can be either `"true"` or `"false"`. If set to true, scale-to-zero is enabled. If set to false, applications are scaled down to the configured _minimum scale bound_. The default value is `"true"`.
