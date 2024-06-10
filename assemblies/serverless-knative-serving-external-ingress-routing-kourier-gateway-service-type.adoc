:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="kourier-gateway-service-type"]
= Kourier Gateway service type
:context: kourier-gateway-service-type

The Kourier Gateway is exposed by default as the `ClusterIP` service type. This service type is determined by the `service-type` ingress spec in the `KnativeServing` custom resource (CR).

.Default spec
[source,yaml]
----
...
spec:
  ingress:
    kourier:
      service-type: ClusterIP
...
----

// Kourier Gateway service type
include::modules/serverless-kourier-gateway-service-type.adoc[leveloffset=+1]