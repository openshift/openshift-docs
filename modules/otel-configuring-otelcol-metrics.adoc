// Module included in the following assemblies:
//
// * otel/otel-configuring.adoc

:_mod-docs-content-type: PROCEDURE
[id="configuring-otelcol-metrics_{context}"]
= Configuring the OpenTelemetry Collector metrics

You can enable metrics and alerts of OpenTelemetry Collector instances.

.Prerequisites

* Monitoring for user-defined projects is enabled in the cluster.

.Procedure

* To enable metrics of a OpenTelemetry Collector instance, set the `spec.observability.metrics.enableMetrics` field to `true`:
+
[source,yaml]
----
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: <name>
spec:
  observability:
    metrics:
      enableMetrics: true
----

.Verification

You can use the *Administrator* view of the web console to verify successful configuration:

* Go to *Observe* -> *Targets*, filter by *Source: User*, and check that the *ServiceMonitors* in the `opentelemetry-collector-<instance_name>` format have the *Up* status.
