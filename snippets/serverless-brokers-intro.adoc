// Text snippet included in the following modules and assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc
// * /serverless/develop/serverless-triggers.adoc
// * /modules/serverless-creating-broker-admin-web-console.adoc
// * /modules/serverless-creating-trigger-admin-web-console.adoc
// * /serverless/discover/serverless-brokers.adoc

:_mod-docs-content-type: SNIPPET

Brokers can be used in combination with triggers to deliver events from an event source to an event sink. Events are sent from an event source to a broker as an HTTP `POST` request. After events have entered the broker, they can be filtered by https://github.com/cloudevents/spec/blob/v1.0/spec.md#context-attributes[CloudEvent attributes] using triggers, and sent as an HTTP `POST` request to an event sink.

image::serverless-event-broker-workflow.png[Broker event delivery overview]
