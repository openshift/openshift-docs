:_mod-docs-content-type: ASSEMBLY
[id="serverless-config-tls"]
= Configuring TLS authentication
include::_attributes/common-attributes.adoc[]
:context: serverless-config-tls

toc::[]

You can use _Transport Layer Security_ (TLS) to encrypt Knative traffic and for authentication.

TLS is the only supported method of traffic encryption for Knative Kafka. Red Hat recommends using both SASL and TLS together for Knative broker for Apache Kafka resources.

[NOTE]
====
If you want to enable internal TLS with a {SMProductName} integration, you must enable {SMProductShortName} with mTLS instead of the internal encryption explained in the following procedure.
ifndef::openshift-dedicated[]
{nbsp}See the documentation for xref:../../../serverless/integrations/serverless-ossm-setup.adoc#serverless-ossm-enabling-serving-metrics_serverless-ossm-setup[Enabling Knative Serving metrics when using Service Mesh with mTLS].
endif::[]
====

include::modules/serverless-enabling-tls-internal-traffic.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../../serverless/eventing/brokers/kafka-broker.adoc#serverless-kafka-broker-tls-default-config_kafka-broker[Configuring TLS authentication for the Knative broker for Apache Kafka]
* xref:../../../serverless/eventing/channels/serverless-kafka-admin-security-channels.adoc#serverless-kafka-tls-channels_serverless-kafka-admin-security-channels[Configuring TLS authentication for channels for Apache Kafka]
ifndef::openshift-dedicated[]
* xref:../../../serverless/integrations/serverless-ossm-setup.adoc#serverless-ossm-enabling-serving-metrics_serverless-ossm-setup[Enabling Knative Serving metrics when using Service Mesh with mTLS]
endif::[]
