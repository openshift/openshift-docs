:_mod-docs-content-type: ASSEMBLY
[id="ossm-dist-trac"]
= Distributed tracing
include::_attributes/common-attributes.adoc[]
:context: ossm-dist-trac

toc::[]

#DRAFT ASSEMBLY - Not currently listed on the Topic Map#
//All of this content currently resides in the Observability Assembly

Distributed Tracing is the process of tracking the performance of individual services in an application by tracing the path of the service calls in the application. Each time a user takes action in an application, a request is executed that might require many services to interact to produce a response. The path of this request is called a distributed transaction.

As a developer, you can use the {JaegerShortName} to visualize call flows in a microservice application with {SMProductName}.

include::modules/ossm-config-sampling.adoc[leveloffset=+1]

include::modules/ossm-config-external-jaeger.adoc[leveloffset=+1]
