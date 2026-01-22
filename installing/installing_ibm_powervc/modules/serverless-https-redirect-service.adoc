// Module is included in the following assemblies:
//
// * serverless/knative-serving/external-ingress-routing/https-redirect-per-service.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-https-redirect-service_{context}"]
= Redirecting HTTPS for a service

// need better details from eng team about use case to update this topic
The following example shows how you can use this annotation in a Knative `Service` YAML object:

[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example
  namespace: default
  annotations:
    networking.knative.dev/http-option: "redirected"
spec:
  ...
----
