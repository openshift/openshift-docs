:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-kafka-admin"]
= Configuring Knative broker for Apache Kafka
:context: serverless-kafka-admin

toc::[]

The Knative broker implementation for Apache Kafka provides integration options for you to use supported versions of the Apache Kafka message streaming platform with {ServerlessProductName}. Kafka provides options for event source, channel, broker, and event sink capabilities.

// OCP
ifdef::openshift-enterprise[]
In addition to the Knative Eventing components that are provided as part of a core {ServerlessProductName} installation, cluster administrators can install the `KnativeKafka` custom resource (CR).
endif::[]

// OSD and ROSA
ifdef::openshift-dedicated,openshift-rosa[]
In addition to the Knative Eventing components that are provided as part of a core {ServerlessProductName} installation, cluster or dedicated administrators can install the `KnativeKafka` custom resource (CR).
endif::[]

The `KnativeKafka` CR provides users with additional options, such as:

* Kafka source
* Kafka channel
* Kafka broker
* Kafka sink