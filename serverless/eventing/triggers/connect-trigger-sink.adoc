:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="connect-trigger-sink"]
= Connecting a trigger to a sink
:context: connect-trigger-sink


You can connect a trigger to a sink, so that events from a broker are filtered before they are sent to the sink. A sink that is connected to a trigger is configured as a `subscriber` in the `Trigger` object's resource spec.

.Example of a `Trigger` object connected to an Apache Kafka sink
[source,yaml]
----
apiVersion: eventing.knative.dev/v1
kind: Trigger
metadata:
  name: <trigger_name> <1>
spec:
...
  subscriber:
    ref:
      apiVersion: eventing.knative.dev/v1alpha1
      kind: KafkaSink
      name: <kafka_sink_name> <2>
----
<1> The name of the trigger being connected to the sink.
<2> The name of a `KafkaSink` object.
