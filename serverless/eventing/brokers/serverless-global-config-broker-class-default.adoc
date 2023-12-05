:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-global-config-broker-class-default"]
= Configuring the default broker class
:context: serverless-global-config-broker-class-default


You can use the `config-br-defaults` config map to specify default broker class settings for Knative Eventing. You can specify the default broker class for the entire cluster or for one or more namespaces. Currently the `MTChannelBasedBroker` and `Kafka` broker types are supported.

.Prerequisites

* You have administrator permissions on {product-title}.
* You have installed the {ServerlessOperatorName} and Knative Eventing on your cluster.
* If you want to use the Knative broker for Apache Kafka as the default broker implementation, you must also install the `KnativeKafka` CR on your cluster.

.Procedure

* Modify the `KnativeEventing` custom resource to add configuration details for the `config-br-defaults` config map:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
  name: knative-eventing
  namespace: knative-eventing
spec:
  defaultBrokerClass: Kafka <1>
  config: <2>
    config-br-defaults: <3>
      default-br-config: |
        clusterDefault: <4>
          brokerClass: Kafka
          apiVersion: v1
          kind: ConfigMap
          name: kafka-broker-config <5>
          namespace: knative-eventing <6>
        namespaceDefaults: <7>
          my-namespace:
            brokerClass: MTChannelBasedBroker
            apiVersion: v1
            kind: ConfigMap
            name: config-br-default-channel <8>
            namespace: knative-eventing <9>
...
----
<1> The default broker class for Knative Eventing.
<2> In `spec.config`, you can specify the config maps that you want to add modified configurations for.
<3> The `config-br-defaults` config map specifies the default settings for any broker that does not specify `spec.config` settings or a broker class.
<4> The cluster-wide default broker class configuration. In this example, the default broker class implementation for the cluster is `Kafka`.
<5> The `kafka-broker-config` config map specifies default settings for the Kafka broker. See "Configuring Knative broker for Apache Kafka settings" in the "Additional resources" section.
<6> The namespace where the `kafka-broker-config` config map exists.
<7> The namespace-scoped default broker class configuration. In this example, the default broker class implementation for the `my-namespace` namespace is `MTChannelBasedBroker`. You can specify default broker class implementations for multiple namespaces.
<8> The `config-br-default-channel` config map specifies the default backing channel for the broker. See "Configuring the default broker backing channel" in the "Additional resources" section.
<9> The namespace where the `config-br-default-channel` config map exists.
+
[IMPORTANT]
====
Configuring a namespace-specific default overrides any cluster-wide settings.
====
