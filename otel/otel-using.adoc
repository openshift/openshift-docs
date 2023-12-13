:_mod-docs-content-type: ASSEMBLY
[id="otel-temp"]
= Using the {OTELShortName}
include::_attributes/common-attributes.adoc[]
:context: otel-temp

toc::[]

You can set up and use the {OTELShortName} to send traces to the OpenTelemetry Collector or the TempoStack.

include::modules/otel-forwarding.adoc[leveloffset=+1]

[id="otel-send-traces-and-metrics-to-otel-collector_{context}"]
== Sending traces and metrics to the OpenTelemetry Collector

Sending tracing and metrics to the OpenTelemetry Collector is possible with or without sidecar injection.

include::modules/otel-send-traces-and-metrics-to-otel-collector-with-sidecar.adoc[leveloffset=+2]

include::modules/otel-send-traces-and-metrics-to-otel-collector-without-sidecar.adoc[leveloffset=+2]
