// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-custom-metrics-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-creating-servicemonitor-resource-for-node-exporter_{context}"]
= Creating a ServiceMonitor resource for the node exporter service

You can use a Prometheus client library and scrape metrics from the `/metrics` endpoint to access and view the metrics exposed by the node-exporter service. Use a `ServiceMonitor` custom resource definition (CRD) to monitor the node exporter service.

.Prerequisites

* You have access to the cluster as a user with `cluster-admin` privileges or the `monitoring-edit` role.
* You have enabled monitoring for the user-defined project by configuring the node-exporter service.

.Procedure
. Create a YAML file for the `ServiceMonitor` resource configuration. In this example, the service monitor matches any service with the label `metrics` and queries the `exmet` port every 30 seconds.

+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    k8s-app: node-exporter-metrics-monitor
  name: node-exporter-metrics-monitor <1>
  namespace: dynamation <2>
spec:
  endpoints:
  - interval: 30s <3>
    port: exmet <4>
    scheme: http
  selector:
    matchLabels:
      servicetype: metrics

----
<1> The name of the `ServiceMonitor`.
<2> The namespace where the `ServiceMonitor` is created.
<3> The interval at which the port will be queried.
<4> The name of the port that is queried every 30 seconds

. Create the `ServiceMonitor` configuration for the node-exporter service.
+
[source,terminal]
----
$ oc create -f node-exporter-metrics-monitor.yaml
----
