// Module included in the following assemblies:
// 
// * otel/otel-configuring.adoc

:_mod-docs-content-type: PROCEDURE
[id="gathering-observability-data-from-different-clusters_{context}"]
= Gathering the observability data from different clusters with the OpenTelemetry Collector

For a multicluster configuration, you can create one OpenTelemetry
Collector instance in each one of the remote clusters and forward all the telemetry
data to one OpenTelemetry Collector instance.

.Prerequisites

* The {OTELOperator} is installed.
* The {TempoOperator} is installed.
* A TempoStack is deployed on the cluster.

.Procedure

. Create a service account for the OpenTelemetry Collector.
+
.Example ServiceAccount
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: otel-collector-deployment
----

. Create a cluster role for the service account.
+
.Example ClusterRole
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: otel-collector
rules:
  # <1>
  # <2>
- apiGroups: ["", "config.openshift.io"]
  resources: ["pods", "namespaces", "infrastructures", "infrastructures/status"]
  verbs: ["get", "watch", "list"]
----
<1> The `k8sattributesprocessor` requires permissions for pods and namespace resources.
<2> The `resourcedetectionprocessor` requires permissions for infrastructures and status.

. Bind the cluster role to the service account.
+
.Example ClusterRoleBinding
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: otel-collector
subjects:
- kind: ServiceAccount
  name: otel-collector-deployment
  namespace: otel-collector-<example>
roleRef:
  kind: ClusterRole
  name: otel-collector
  apiGroup: rbac.authorization.k8s.io
----

. Create the YAML file to define the `OpenTelemetryCollector` custom resource (CR) in the edge clusters.
+
.Example `OpenTelemetryCollector` custom resource for the edge clusters
[source,yaml]
----
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: otel
  namespace: otel-collector-<example>
spec:
  mode: daemonset
  serviceAccount: otel-collector-deployment
  config: |
    receivers:
      jaeger:
        protocols:
          grpc:
          thrift_binary:
          thrift_compact:
          thrift_http:
      opencensus:
      otlp:
        protocols:
          grpc:
          http:
      zipkin:
    processors:
      batch:
      k8sattributes:
      memory_limiter:
        check_interval: 1s
        limit_percentage: 50
        spike_limit_percentage: 30
      resourcedetection:
        detectors: [openshift]
    exporters:
      otlphttp:
        endpoint: https://observability-cluster.com:443 # <1>
        insecure: false
        compression: on
        tls:
          cert_file: "/path/to/server-cert.pem"
          key_file: "/path/to/server-key.pem"
          client_ca_file: "/path/to/client-ca.pem"

    service:
      pipelines:
        traces:
          receivers: [jaeger, opencensus, otlp, zipkin]
          processors: [memory_limiter, k8sattributes, resourcedetection, batch]
          exporters: [otlp]
----
<1> The Collector exporter is configured to export OTLP HTTP and points to the OpenTelemetry Collector from the central cluster.

. Create the YAML file to define the `OpenTelemetryCollector` custom resource (CR) in the central cluster.
+
.Example `OpenTelemetryCollector` custom resource for the central cluster
[source,yaml]
----
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: otlp-receiver
  namespace: observability
spec:
  mode: "deployment"
  ingress:
    type: route
    hostname: "observability-cluster.com"
    route:
      termination: "edge"
  config: |
    receivers:
      otlp:
        protocols:
          http:
    exporters:
      logging:
      otlp:
        endpoint: "tempo-<simplest>-distributor:4317" # <1>
        tls:
          insecure: true
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: []
          exporters: [otlp]
----
<1> The Collector exporter is configured to export OTLP and points to the Tempo distributor endpoint, which in this example is `"tempo-simplest-distributor:4317"` and already created.
