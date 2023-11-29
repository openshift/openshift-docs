// Module included in the following assemblies
//
// * serverless/knative-serving/external-ingress-routing/url-scheme-external-routes.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-url-scheme-external-routes_{context}"]
= Setting the URL scheme for external routes
// should probably be a procedure, but this is out of scope for the abstracts PR

.Default spec
[source,yaml]
----
...
spec:
  config:
    network:
      default-external-scheme: "https"
...
----

You can override the default spec to use HTTP by modifying the `default-external-scheme` key:

.HTTP override spec
[source,yaml]
----
...
spec:
  config:
    network:
      default-external-scheme: "http"
...
----
