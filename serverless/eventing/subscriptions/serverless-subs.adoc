:_mod-docs-content-type: ASSEMBLY
[id="serverless-subs"]
= Creating subscriptions
include::_attributes/common-attributes.adoc[]
:context: serverless-subs

toc::[]

After you have created a channel and an event sink, you can create a subscription to enable event delivery. Subscriptions are created by configuring a `Subscription` object, which specifies the channel and the sink (also known as a _subscriber_) to deliver events to.


// Subscription
include::modules/serverless-creating-subscription-admin-web-console.adoc[leveloffset=+1]
include::modules/serverless-creating-subscriptions-odc.adoc[leveloffset=+1]
include::modules/serverless-creating-subscriptions-yaml.adoc[leveloffset=+1]
include::modules/serverless-creating-subscriptions-kn.adoc[leveloffset=+1]


[id="next-steps_serverless-subs"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-configuring-event-delivery-examples_serverless-event-delivery[Examples of configuring event delivery parameters].
