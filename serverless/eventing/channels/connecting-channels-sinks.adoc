:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="connecting-channels-sinks"]
= Connecting channels to sinks
:context: connecting-channels-sinks
toc::[]

Events that have been sent to a channel from an event source or producer can be forwarded to one or more sinks by using _subscriptions_.
You can create subscriptions by configuring a `Subscription` object, which specifies the channel and the sink (also known as a _subscriber_) that consumes the events sent to that channel.

include::modules/serverless-creating-subscriptions-odc.adoc[leveloffset=+1]
include::modules/serverless-creating-subscriptions-yaml.adoc[leveloffset=+1]
include::modules/serverless-creating-subscriptions-kn.adoc[leveloffset=+1]
include::modules/serverless-creating-subscription-admin-web-console.adoc[leveloffset=+1]

[id="next-steps_connecting-channels-sinks"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-configuring-event-delivery-examples_serverless-event-delivery[Examples of configuring event delivery parameters].