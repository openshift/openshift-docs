// Text snippet included in the following modules and assemblies:
//
// * /serverless/eventing/event-sinks/serverless-event-sinks
// * /serverless/eventing/event-sinks/serverless-creating-sinks

:_mod-docs-content-type: SNIPPET

When you create an event source, you can specify an event sink where events are sent to from the source. An event sink is an addressable or a callable resource that can receive incoming events from other resources. Knative services, channels, and brokers are all examples of event sinks. There is also a specific Apache Kafka sink type available.