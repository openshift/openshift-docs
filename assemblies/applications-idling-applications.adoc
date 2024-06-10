:_mod-docs-content-type: ASSEMBLY
[id="idling-applications"]
= Idling applications
include::_attributes/common-attributes.adoc[]
:context: idling-applications

toc::[]

Cluster administrators can idle applications to reduce resource consumption. This is useful when the cluster is deployed on a public cloud where cost is related to resource consumption.

If any scalable resources are not in use, {product-title} discovers and idles them by scaling their replicas to `0`. The next time network traffic is directed to the resources, the resources are unidled by scaling up the replicas, and normal operation continues.

Applications are made of services, as well as other scalable resources, such as deployment configs. The action of idling an application involves idling all associated resources.

include::modules/idle-idling-applications.adoc[leveloffset=+1]
include::modules/idle-unidling-applications.adoc[leveloffset=+1]
