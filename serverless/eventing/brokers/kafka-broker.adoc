:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="kafka-broker"]
= Knative broker implementation for Apache Kafka
:context: kafka-broker

toc::[]

include::snippets/serverless-about-kafka-broker.adoc[]


[id="creating-kafka-broker"]
== Creating an Apache Kafka broker when it is not configured as the default broker type

If your {ServerlessProductName} deployment is not configured to use Kafka broker as the default broker type, you can use one of the following procedures to create a Kafka-based broker.

include::modules/serverless-kafka-broker.adoc[leveloffset=+2]
include::modules/serverless-kafka-broker-with-kafka-topic.adoc[leveloffset=+2]
include::modules/serverless-kafka-broker-with-isolated-dataplane.adoc[leveloffset=+2]
include::modules/serverless-create-kafka-namespaced-broker.adoc[leveloffset=+2]

// kafka broker general configmap
include::modules/serverless-kafka-broker-configmap.adoc[leveloffset=+1]


[id="serverless-kafka-admin-security"]
== Security configuration for the Knative broker implementation for Apache Kafka

Kafka clusters are generally secured by using the TLS or SASL authentication methods. You can configure a Kafka broker or channel to work against a protected Red Hat AMQ Streams cluster by using TLS or SASL.

[NOTE]
====
Red Hat recommends that you enable both SASL and TLS together.
====

// kafka broker security config
include::modules/serverless-kafka-broker-tls-default-config.adoc[leveloffset=+2]
include::modules/serverless-kafka-broker-sasl-default-config.adoc[leveloffset=+2]


[id="additional-resources_serverless-kafka-admin"]
[role="_additional-resources"]
== Additional resources
* link:https://access.redhat.com/documentation/en-us/red_hat_amq/7.6/html/amq_streams_on_openshift_overview/kafka-concepts_str#kafka-concepts-key_str[Red Hat AMQ Streams documentation]
* link:https://access.redhat.com/documentation/en-us/red_hat_amq/7.5/html-single/using_amq_streams_on_rhel/index#assembly-kafka-encryption-and-authentication-str[TLS and SASL on Kafka]
