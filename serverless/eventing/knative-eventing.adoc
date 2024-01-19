:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="knative-eventing-overview"]
= Knative Eventing
:context: knative-eventing-overview

Knative Eventing on {product-title} enables developers to use an link:https://www.redhat.com/en/topics/integration/what-is-event-driven-architecture[event-driven architecture] with serverless applications. An event-driven architecture is based on the concept of decoupled relationships between event producers and event consumers.

Event producers create events, and event _sinks_, or consumers, receive events. Knative Eventing uses standard HTTP POST requests to send and receive events between event producers and sinks. These events conform to the link:https://cloudevents.io[CloudEvents specifications], which enables creating, parsing, sending, and receiving events in any programming language.

== Knative Eventing use cases:

Knative Eventing supports the following use cases:

Publish an event without creating a consumer:: You can send events to a broker as an HTTP POST, and use binding to decouple the destination configuration from your application that produces events.

Consume an event without creating a publisher:: You can use a trigger to consume events from a broker based on event attributes. The application receives events as an HTTP POST.

To enable delivery to multiple types of sinks, Knative Eventing defines the following generic interfaces that can be implemented by multiple Kubernetes resources:

Addressable resources:: Able to receive and acknowledge an event delivered over HTTP to an address defined in the `status.address.url` field of the event. The Kubernetes `Service` resource also satisfies the addressable interface.

Callable resources:: Able to receive an event delivered over HTTP and transform it, returning `0` or `1` new events in the HTTP response payload. These returned events may be further processed in the same way that events from an external event source are processed.
