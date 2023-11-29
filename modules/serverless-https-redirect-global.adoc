// Module included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/https-redirect-global.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-https-redirect-global_{context}"]
= HTTPS redirection global settings

.Example `KnativeServing` CR that enables HTTPS redirection
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
  name: knative-serving
spec:
  config:
    network:
      httpProtocol: "redirected"
...
----
