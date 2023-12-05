// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="enabling-monitoring-of-event-listeners-for-triggers-for-user-defined-projects_{context}"]
= Enabling monitoring of event listeners for Triggers for user-defined projects

As a cluster administrator, to gather event listener metrics for the `Triggers` service in a user-defined project and display them in the {product-title} web console, you can create a service monitor for each event listener. On receiving an HTTP request, event listeners for the `Triggers` service return three metrics -- `eventlistener_http_duration_seconds`, `eventlistener_event_count`, and `eventlistener_triggered_resources`.

.Prerequisites

* You have logged in to the {product-title} web console.
* You have installed the {pipelines-title} Operator.
* You have enabled monitoring for user-defined projects.

.Procedure

. For each event listener, create a service monitor. For example, to view the metrics for the `github-listener` event listener in the `test` namespace, create the following service monitor:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app.kubernetes.io/managed-by: EventListener
    app.kubernetes.io/part-of: Triggers
    eventlistener: github-listener
  annotations:
    networkoperator.openshift.io/ignore-errors: ""
  name: el-monitor
  namespace: test
spec:
  endpoints:
    - interval: 10s
      port: http-metrics
  jobLabel: name
  namespaceSelector:
    matchNames:
      - test
  selector:
    matchLabels:
      app.kubernetes.io/managed-by: EventListener
      app.kubernetes.io/part-of: Triggers
      eventlistener: github-listener
...
----
. Test the service monitor by sending a request to the event listener. For example, push an empty commit:
+
[source,terminal]
----
$ git commit -m "empty-commit" --allow-empty && git push origin main
----
. On the {product-title} web console, navigate to **Administrator** -> **Observe** -> **Metrics**.
. To view a metric, search by its name. For example, to view the details of the `eventlistener_http_resources` metric for the `github-listener` event listener, search using the `eventlistener_http_resources` keyword.
