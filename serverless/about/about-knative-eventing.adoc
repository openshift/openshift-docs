:_mod-docs-content-type: ASSEMBLY
[id="about-knative-eventing"]
= Knative Eventing
:context: about-knative-eventing
include::_attributes/common-attributes.adoc[]

toc::[]

Knative Eventing on {product-title} enables developers to use an link:https://www.redhat.com/en/topics/integration/what-is-event-driven-architecture[event-driven architecture] with serverless applications. An event-driven architecture is based on the concept of decoupled relationships between event producers and event consumers.

Event producers create events, and event _sinks_, or consumers, receive events. Knative Eventing uses standard HTTP POST requests to send and receive events between event producers and sinks. These events conform to the link:https://cloudevents.io[CloudEvents specifications], which enables creating, parsing, sending, and receiving events in any programming language.

Knative Eventing supports the following use cases:

Publish an event without creating a consumer:: You can send events to a broker as an HTTP POST, and use binding to decouple the destination configuration from your application that produces events.

Consume an event without creating a publisher:: You can use a trigger to consume events from a broker based on event attributes. The application receives events as an HTTP POST.

To enable delivery to multiple types of sinks, Knative Eventing defines the following generic interfaces that can be implemented by multiple Kubernetes resources:

Addressable resources:: Able to receive and acknowledge an event delivered over HTTP to an address defined in the `status.address.url` field of the event. The Kubernetes `Service` resource also satisfies the addressable interface.

Callable resources:: Able to receive an event delivered over HTTP and transform it, returning `0` or `1` new events in the HTTP response payload. These returned events may be further processed in the same way that events from an external event source are processed.

include::modules/serverless-kafka-developer.adoc[leveloffset=+1]

[id="additional-resources_about-knative-eventing"]
[role="_additional-resources"]
== Additional resources
* xref:../../serverless/install/installing-knative-eventing.adoc#serverless-install-kafka-odc_installing-knative-eventing[Installing the `KnativeKafka` custom resource].
* link:https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/amq_streams_on_openshift_overview/kafka-concepts_str#kafka-concepts-key_str[Red Hat AMQ Streams documentation]
* link:https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html-single/using_amq_streams_on_rhel/index#assembly-kafka-encryption-and-authentication-str[Red Hat AMQ Streams TLS and SASL on Apache Kafka documentation]
* xref:../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-event-delivery[Event delivery]
