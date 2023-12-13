// Module is included in the following assemblies:
//
// * serverless/serverless-tracing.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-jaeger-config_{context}"]
= Configuring Jaeger to enable distributed tracing

To enable distributed tracing using Jaeger, you must install and configure Jaeger as a standalone integration.

.Prerequisites

ifdef::openshift-enterprise[]
* You have access to an {product-title} account with cluster administrator access.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have access to an {product-title} account with cluster or dedicated administrator access.
endif::[]

* You have installed the {ServerlessOperatorName}, Knative Serving, and Knative Eventing.
* You have installed the {JaegerName} Operator.
* You have installed the OpenShift CLI (`oc`).
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

. Create and apply a `Jaeger` custom resource (CR) that contains the following:
+
.Jaeger CR
[source,yaml]
----
apiVersion: jaegertracing.io/v1
kind: Jaeger
metadata:
  name: jaeger
  namespace: default
----

. Enable tracing for Knative Serving, by editing the `KnativeServing` CR and adding a YAML configuration for tracing:
+
.Tracing YAML example for Serving
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
  namespace: knative-serving
spec:
  config:
    tracing:
      sample-rate: "0.1" <1>
      backend: zipkin <2>
      zipkin-endpoint: "http://jaeger-collector.default.svc.cluster.local:9411/api/v2/spans" <3>
      debug: "false" <4>
----
+
<1> The `sample-rate` defines sampling probability. Using `sample-rate: "0.1"` means that 1 in 10 traces are sampled.
<2> `backend` must be set to `zipkin`.
<3> The `zipkin-endpoint` must point to your `jaeger-collector` service endpoint. To get this endpoint, substitute the namespace where the Jaeger CR is applied.
<4> Debugging should be set to `false`. Enabling debug mode by setting `debug: "true"` allows all spans to be sent to the server, bypassing sampling.

. Enable tracing for Knative Eventing by editing the `KnativeEventing` CR:
+
.Tracing YAML example for Eventing
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
  name: knative-eventing
  namespace: knative-eventing
spec:
  config:
    tracing:
      sample-rate: "0.1" <1>
      backend: zipkin <2>
      zipkin-endpoint: "http://jaeger-collector.default.svc.cluster.local:9411/api/v2/spans" <3>
      debug: "false" <4>
----
+
<1> The `sample-rate` defines sampling probability. Using `sample-rate: "0.1"` means that 1 in 10 traces are sampled.
<2> Set `backend` to `zipkin`.
<3> Point the `zipkin-endpoint` to your `jaeger-collector` service endpoint. To get this endpoint, substitute the namespace where the Jaeger CR is applied.
<4> Debugging should be set to `false`. Enabling debug mode by setting `debug: "true"` allows all spans to be sent to the server, bypassing sampling.

.Verification

You can access the Jaeger web console to see tracing data, by using the `jaeger` route.

. Get the `jaeger` route's hostname by entering the following command:
+
[source,terminal]
----
$ oc get route jaeger -n default
----
+
.Example output
[source,terminal]
----
NAME     HOST/PORT                         PATH   SERVICES       PORT    TERMINATION   WILDCARD
jaeger   jaeger-default.apps.example.com          jaeger-query   <all>   reencrypt     None
----

. Open the endpoint address in your browser to view the console.
