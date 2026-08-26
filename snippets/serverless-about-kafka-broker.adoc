// Text snippet included in the following modules and assemblies:
//
// * /modules/serverless-broker-types.adoc
// * /serverless/develop/kafka-broker.adoc

:_mod-docs-content-type: SNIPPET

For production-ready Knative Eventing deployments, Red Hat recommends using the Knative broker implementation for Apache Kafka. The broker is an Apache Kafka native implementation of the Knative broker, which sends CloudEvents directly to the Kafka instance.

The Knative broker has a native integration with Kafka for storing and routing events. This allows better integration with Kafka for the broker and trigger model over other broker types, and reduces network hops. Other benefits of the Knative broker implementation include:

* At-least-once delivery guarantees
* Ordered delivery of events, based on the CloudEvents partitioning extension
* Control plane high availability
* A horizontally scalable data plane

The  Knative broker implementation for Apache Kafka stores incoming CloudEvents as Kafka records, using the binary content mode. This means that all CloudEvent attributes and extensions are mapped as headers on the Kafka record, while the `data` spec of the CloudEvent corresponds to the value of the Kafka record.
