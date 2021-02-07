// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-monitoring-prometheus.adoc

[id="osdk-monitoring-prometheus-operator-support_{context}"]
= Prometheus Operator support

link:https://prometheus.io/[Prometheus] is an open-source systems monitoring and alerting toolkit. The Prometheus Operator creates, configures, and manages Prometheus clusters running on Kubernetes-based clusters, such as {product-title}.

Helper functions exist in the Operator SDK by default to automatically set up metrics in any generated Go-based Operator for use on clusters where the Prometheus Operator is deployed.
