// Module is included in the following assemblies:
//
// serverless/about/about-knative-eventing.adoc

:_mod-docs-content-type: CONCEPT
[id="serverless-kafka-developer_{context}"]
= Using the Knative broker for Apache Kafka


THe Knative broker implementation for Apache Kafka provides integration options for you to use supported versions of the Apache Kafka message streaming platform with {ServerlessProductName}. Kafka provides options for event source, channel, broker, and event sink capabilities.


// OCP
ifdef::openshift-enterprise[]
[NOTE]
====
The Knative broker implementation for Apache Kafka is not currently supported for {ibm-z-name} and {ibm-power-name}.
====
endif::[]

Knative broker for Apache Kafka provides additional options, such as:

* Kafka source
* Kafka channel
* Kafka broker
* Kafka sink
