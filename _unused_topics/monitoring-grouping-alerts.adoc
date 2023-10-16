// Module included in the following assemblies:
//
// * monitoring/configuring-monitoring-stack.adoc

[id="grouping-alerts_{context}"]
== Grouping alerts

Once alerts are firing against the Alertmanager, it must be configured to know how to logically group them. This procedure shows how to configure alert grouping:

.Procedure

_FIXME get missing info and complete the procedure_

For this example, a new route will be added to reflect alert routing of the "frontend" team.

. Add new routes. Multiple routes may be added beneath the original route, typically to define the receiver for the notification. This example uses a matcher to ensure that only alerts coming from the service `example-app` are used:
+
  global:
    resolve_timeout: 5m
  route:
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 12h
    receiver: default
    routes:
    - match:
        alertname: DeadMansSwitch
      repeat_interval: 5m
      receiver: deadmansswitch
    - match:
        service: example-app
      routes:
      - match:
          severity: critical
        receiver: team-frontend-page
  receivers:
  - name: default
  - name: deadmansswitch
+
The sub-route matches only on alerts that have a severity of `critical`, and sends them via the receiver called `team-frontend-page`. As the name indicates, someone should be paged for alerts that are critical.


