:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-kafka-developer-sink"]
= Sink for Apache Kafka
:context: serverless-kafka-developer-sink

toc::[]

Apache Kafka sinks are a type of xref:../../../serverless/eventing/event-sinks/serverless-event-sinks.adoc#serverless-event-sinks[event sink] that are available if a cluster administrator has enabled Apache Kafka on your cluster. You can send events directly from an xref:../../../serverless/eventing/event-sources/knative-event-sources.adoc#knative-event-sources[event source] to a Kafka topic by using a Kafka sink.

// Kafka sink via YAML
include::modules/serverless-kafka-sink.adoc[leveloffset=+1]

// Creating a Kafka sink via ODC
include::modules/serverless-creating-a-kafka-event-sink.adoc[leveloffset=+1]

// kafka sink security config
include::modules/serverless-kafka-sink-security-config.adoc[leveloffset=+1]