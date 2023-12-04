// Module included in the following assemblies:
//
// * /serverless/eventing/tuning/serverless-ha.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-config-replicas-kafka_{context}"]
= Configuring high availability replicas for the Knative broker implementation for Apache Kafka

High availability (HA) is available by default for the Knative broker implementation for Apache Kafka components `kafka-controller` and `kafka-webhook-eventing`, which are configured to have two each replicas by default. You can change the number of replicas for these components by modifying the `spec.high-availability.replicas` value in the `KnativeKafka` custom resource (CR).

.Prerequisites

ifdef::openshift-enterprise[]
* You have access to an {product-title} account with cluster administrator access.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have access to an {product-title} account with cluster administrator or dedicated administrator access.
endif::[]

* The {ServerlessOperatorName} and Knative broker for Apache Kafka are installed on your cluster.

.Procedure

. In the {product-title} web console *Administrator* perspective, navigate to *OperatorHub* -> *Installed Operators*.

. Select the `knative-eventing` namespace.

. Click *Knative Kafka* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Kafka* tab.

. Click *knative-kafka*, then go to the *YAML* tab in the *knative-kafka* page.
+
image::kafka-YAML-HA.png[Knative Kafka YAML]

. Modify the number of replicas in the `KnativeKafka` CR:
+
.Example YAML
[source,yaml]
----
apiVersion: operator.serverless.openshift.io/v1alpha1
kind: KnativeKafka
metadata:
  name: knative-kafka
  namespace: knative-eventing
spec:
  high-availability:
    replicas: 3
----
