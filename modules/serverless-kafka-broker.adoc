// Module included in the following assemblies:
//
// * serverless/eventing/brokers/serverless-using-brokers.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-kafka-broker_{context}"]
= Creating an Apache Kafka broker by using YAML

Creating Knative resources by using YAML files uses a declarative API, which enables you to describe applications declaratively and in a reproducible manner. To create a Kafka broker by using YAML, you must create a YAML file that defines a `Broker` object, then apply it by using the `oc apply` command.

.Prerequisites

* The {ServerlessOperatorName}, Knative Eventing, and the `KnativeKafka` custom resource are installed on your {product-title} cluster.

* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

* You have installed the OpenShift CLI (`oc`).

.Procedure

. Create a Kafka-based broker as a YAML file:
+
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Broker
metadata:
  annotations:
    eventing.knative.dev/broker.class: Kafka <1>
  name: example-kafka-broker
spec:
  config:
    apiVersion: v1
    kind: ConfigMap
    name: kafka-broker-config <2>
    namespace: knative-eventing
----
<1> The broker class. If not specified, brokers use the default class as configured by cluster administrators. To use the Kafka broker, this value must be `Kafka`.
<2> The default config map for Knative brokers for Apache Kafka. This config map is created when the Kafka broker functionality is enabled on the cluster by a cluster administrator.

. Apply the Kafka-based broker YAML file:
+
[source,terminal]
----
$ oc apply -f <filename>
----
