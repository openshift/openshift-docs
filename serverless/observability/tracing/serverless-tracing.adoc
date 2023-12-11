:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-tracing"]
= Tracing requests
:context: serverless-tracing


toc::[]

Distributed tracing records the path of a request through the various services that make up an application. It is used to tie information about different units of work together, to understand a whole chain of events in a distributed transaction. The units of work might be executed in different processes or hosts.

ifdef::openshift-enterprise[]
include::modules/distr-tracing-product-overview.adoc[leveloffset=+1]
endif::[]

ifdef::openshift-enterprise[]
[id="additional-resources_serverless-tracing"]
[role="_additional-resources"]
== Additional resources
* xref:../../../distr_tracing/distr_tracing_arch/distr-tracing-architecture.adoc#distr-tracing-architecture[{DTProductName} architecture]
* xref:../../../distr_tracing/distr_tracing_install/distr-tracing-installing.adoc#installing-distributed-tracing[Installing distributed tracing]
endif::[]
