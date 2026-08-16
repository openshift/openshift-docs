:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-triggers"]
= Triggers overview
:context: serverless-triggers



include::snippets/serverless-brokers-intro.adoc[]

If you are using a Knative broker for Apache Kafka, you can configure the delivery order of events from triggers to event sinks. See xref:../../../serverless/eventing/triggers/serverless-triggers.adoc#trigger-event-delivery-config_serverless-triggers[Configuring event delivery ordering for triggers].



// event delivery config
include::modules/trigger-event-delivery-config.adoc[leveloffset=+1]

[id="next-steps_serverless-triggers"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-configuring-event-delivery-examples_serverless-event-delivery[Examples of configuring event delivery parameters].
