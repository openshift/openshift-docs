// Module included in the following assemblies:
//
// * /serverless/eventing/brokers/serverless-using-brokers.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-describe-broker-kn_{context}"]
= Describing an existing broker by using the Knative CLI

Using the Knative (`kn`) CLI to describe brokers provides a streamlined and intuitive user interface. You can use the `kn broker describe` command to print information about existing brokers in your cluster by using the Knative CLI.

.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your {product-title} cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* Describe an existing broker:
+
[source,terminal]
----
$ kn broker describe <broker_name>
----
+
.Example command using default broker
[source,terminal]
----
$ kn broker describe default
----
+
.Example output
[source,terminal]
----
Name:         default
Namespace:    default
Annotations:  eventing.knative.dev/broker.class=MTChannelBasedBroker, eventing.knative.dev/creato ...
Age:          22s

Address:
  URL:    http://broker-ingress.knative-eventing.svc.cluster.local/default/default

Conditions:
  OK TYPE                   AGE REASON
  ++ Ready                  22s
  ++ Addressable            22s
  ++ FilterReady            22s
  ++ IngressReady           22s
  ++ TriggerChannelReady    22s
----
