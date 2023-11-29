:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-creating-channels"]
= Creating channels
:context: serverless-creating-channels

toc::[]

include::snippets/serverless-channels-intro.adoc[]

// Channel
include::modules/serverless-creating-channel-admin-web-console.adoc[leveloffset=+1]
include::modules/serverless-create-channel-odc.adoc[leveloffset=+1]
include::modules/serverless-create-channel-kn.adoc[leveloffset=+1]
include::modules/serverless-create-default-channel-yaml.adoc[leveloffset=+1]
include::modules/serverless-create-kafka-channel-yaml.adoc[leveloffset=+1]

[id="next-steps_serverless-creating-channels"]
== Next steps

* After you have created a channel, you can xref:../../../serverless/eventing/channels/connecting-channels-sinks.adoc#connecting-channels-sinks[connect the channel to a sink] so that the sink can receive events.
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-configuring-event-delivery-examples_serverless-event-delivery[Examples of configuring event delivery parameters].
