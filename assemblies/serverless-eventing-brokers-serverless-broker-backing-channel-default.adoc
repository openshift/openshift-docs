:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-broker-backing-channel-default"]
= Configuring the default broker backing channel
:context: serverless-broker-backing-channel-default

If you are using a channel-based broker, you can set the default backing channel type for the broker to either `InMemoryChannel` or `KafkaChannel`.

.Prerequisites

* You have administrator permissions on {product-title}.
* You have installed the {ServerlessOperatorName} and Knative Eventing on your cluster.
* You have installed the OpenShift (`oc`) CLI.
* If you want to use Apache Kafka channels as the default backing channel type, you must also install the `KnativeKafka` CR on your cluster.

.Procedure

. Modify the `KnativeEventing` custom resource (CR) to add configuration details for the `config-br-default-channel` config map:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeEventing
metadata:
  name: knative-eventing
  namespace: knative-eventing
spec:
  config: <1>
    config-br-default-channel:
      channel-template-spec: |
        apiVersion: messaging.knative.dev/v1beta1
        kind: KafkaChannel <2>
        spec:
          numPartitions: 6 <3>
          replicationFactor: 3 <4>
----
<1> In `spec.config`, you can specify the config maps that you want to add modified configurations for.
<2> The default backing channel type configuration. In this example, the default channel implementation for the cluster is `KafkaChannel`.
<3> The number of partitions for the Kafka channel that backs the broker.
<4> The replication factor for the Kafka channel that backs the broker.

. Apply the updated `KnativeEventing` CR:
+
[source,terminal]
----
$ oc apply -f <filename>
----
