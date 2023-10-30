// Module included in the following assemblies:
//
// * serverless/eventing/brokers/kafka-broker.adoc

:_mod-docs-content-type: CONCEPT
[id="serverless-kafka-broker-with-isolated-dataplane_{context}"]
= Knative Broker implementation for Apache Kafka with isolated data plane

:FeatureName: The Knative Broker implementation for Apache Kafka with isolated data plane
include::snippets/technology-preview.adoc[leveloffset=+2]

The Knative Broker implementation for Apache Kafka has 2 planes:

Control plane:: Consists of controllers that talk to the Kubernetes API, watch for custom objects, and manage the data plane.

Data plane:: The collection of components that listen for incoming events, talk to Apache Kafka, and send events to the event sinks. The Knative Broker implementation for Apache Kafka data plane is where events flow. The implementation consists of `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments.

When you configure a Broker class of `Kafka`, the Knative Broker implementation for Apache Kafka uses a shared data plane. This means that the `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments in the `knative-eventing` namespace are used for all Apache Kafka Brokers in the cluster.

However, when you configure a Broker class of `KafkaNamespaced`, the Apache Kafka broker controller creates a new data plane for each namespace where a broker exists. This data plane is used by all `KafkaNamespaced` brokers in that namespace. This provides isolation between the data planes, so that the `kafka-broker-receiver` and `kafka-broker-dispatcher` deployments in the user namespace are only used for the broker in that namespace.

[IMPORTANT]
====
As a consequence of having separate data planes, this security feature creates more deployments and uses more resources. Unless you have such isolation requirements, use a *regular* Broker with a class of `Kafka`.
====
