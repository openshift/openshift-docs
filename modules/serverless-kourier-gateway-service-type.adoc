// Module included in the following assemblies
//
// * serverless/knative-serving/external-ingress-routing/kourier-gateway-service-type.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-kourier-gateway-service-type_{context}"]
= Setting the Kourier Gateway service type
// should probably be a procedure but this is out of scope for the abstracts PR

You can override the default service type to use a load balancer service type instead by modifying the `service-type` spec:

.LoadBalancer override spec
[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: LoadBalancer
...
----
