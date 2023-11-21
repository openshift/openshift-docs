:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-using-brokers"]
= Creating brokers
:context: serverless-using-brokers

toc::[]

Knative provides a default, channel-based broker implementation. This channel-based broker can be used for development and testing purposes, but does not provide adequate event delivery guarantees for production environments.

If a cluster administrator has configured your {ServerlessProductName} deployment to use Apache Kafka as the default broker type, creating a broker by using the default settings creates a Knative broker for Apache Kafka.

If your {ServerlessProductName} deployment is not configured to use the Knative broker for Apache Kafka as the default broker type, the channel-based broker is created when you use the default settings in the following procedures.

include::modules/serverless-create-broker-kn.adoc[leveloffset=+1]
include::modules/serverless-creating-broker-annotation.adoc[leveloffset=+1]
include::modules/serverless-creating-broker-labeling.adoc[leveloffset=+1]
include::modules/serverless-deleting-broker-injection.adoc[leveloffset=+1]
include::modules/serverless-creating-a-broker-odc.adoc[leveloffset=+1]
// Brokers
include::modules/serverless-creating-broker-admin-web-console.adoc[leveloffset=+1]


[id="next-steps_serverless-using-brokers"]
== Next steps
* Configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. See xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-configuring-event-delivery-examples_serverless-event-delivery[Examples of configuring event delivery parameters].

[id="additional-resources_serverless-using-brokers"]
[role="_additional-resources"]
== Additional resources
* xref:../../../serverless/eventing/brokers/serverless-global-config-broker-class-default.adoc#serverless-global-config-broker-class-default[Configuring the default broker class]
* xref:../../../serverless/eventing/triggers/serverless-triggers.adoc#serverless-triggers[Triggers]
xref:../../../serverless/eventing/event-sources/knative-event-sources.adoc#knative-event-sources[Event sources]
* xref:../../../serverless/eventing/brokers/serverless-event-delivery.adoc#serverless-event-delivery[Event delivery]
