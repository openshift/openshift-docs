// Module included in the following assemblies:
//
// serverless/knative-serving/external-ingress-routing/using-http2-gRPC.adoc

:_mod-docs-content-type: PROCEDURE
[id="interacting-serverless-apps-http2-grpc-up-to-4-9_{context}"]
= Interacting with a serverless application using HTTP2 and gRPC in {product-title} 4.9 and older

[IMPORTANT]
====
This method needs to expose Kourier Gateway using the `LoadBalancer` service type. You can configure this by adding the following YAML to your `KnativeServing` custom resource definition (CRD):

[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: LoadBalancer
...
----
====

.Prerequisites

* Install {ServerlessOperatorName} and Knative Serving on your cluster.
* Install the OpenShift CLI (`oc`).
* Create a Knative service.

.Procedure

. Find the application host. See the instructions in _Verifying your serverless application deployment_.

. Find the ingress gateway's public address:
+
[source,terminal]
----
$ oc -n knative-serving-ingress get svc kourier
----
+
.Example output
+
[source,terminal]
----
NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP                                                             PORT(S)                                                                                                                                      AGE
kourier   LoadBalancer   172.30.51.103   a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com   80:31380/TCP,443:31390/TCP   67m
----
+
The public address is surfaced in the `EXTERNAL-IP` field, and in this case is `a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com`.

. Manually set the host header of your HTTP request to the application's host, but direct the request itself against the public address of the ingress gateway.
+
[source,terminal]
----
$ curl -H "Host: hello-default.example.com" a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com
----
+
.Example output
[source,terminal]
----
Hello Serverless!
----
+
You can also make a direct gRPC request against the ingress gateway:
+
[source,golang]
----
import "google.golang.org/grpc"

grpc.Dial(
    "a83e86291bcdd11e993af02b7a65e514-33544245.us-east-1.elb.amazonaws.com:80",
    grpc.WithAuthority("hello-default.example.com:80"),
    grpc.WithInsecure(),
)
----
+
[NOTE]
====
Ensure that you append the respective port, 80 by default, to both hosts as shown in the previous example.
====
