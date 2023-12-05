// Module included in the following assemblies:
//
// serverless/knative-serving/external-ingress-routing/using-http2-gRPC.adoc

:_mod-docs-content-type: PROCEDURE
[id="interacting-serverless-apps-http2-grpc_{context}"]
= Interacting with a serverless application using HTTP2 and gRPC

[IMPORTANT]
====
This method applies to {product-title} 4.10 and later. For older versions, see the following section.
====

.Prerequisites

* Install {ServerlessOperatorName} and Knative Serving on your cluster.
* Install the OpenShift CLI (`oc`).
* Create a Knative service.
* Upgrade {product-title} 4.10 or later.
* Enable HTTP/2 on OpenShift Ingress controller.

.Procedure

. Add the `serverless.openshift.io/default-enable-http2=true` annotation to the `KnativeServing` Custom Resource:
+
[source,terminal]
----
$ oc annotate knativeserving <your_knative_CR> -n knative-serving serverless.openshift.io/default-enable-http2=true
----

. After the annotation is added, you can verify that the `appProtocol` value of the Kourier service is `h2c`:
+
[source,terminal]
----
$ oc get svc -n knative-serving-ingress kourier -o jsonpath="{.spec.ports[0].appProtocol}"
----
+
.Example output
+
[source,terminal]
----
h2c
----

. Now you can use the gRPC framework over the HTTP/2 protocol for external traffic, for example:
+
[source,golang]
----
import "google.golang.org/grpc"

grpc.Dial(
   YOUR_URL, <1>
   grpc.WithTransportCredentials(insecure.NewCredentials())), <2>
)
----
<1> Your `ksvc` URL.
<2> Your certificate.
