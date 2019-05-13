// Module included in the following assemblies:
//
// * monitoring/configuring-monitoring-stack.adoc

[id="dead-mans-switch_{context}"]
== Dead man's switch

{product-title} Monitoring ships with a "Dead man's switch" to ensure the availability of the monitoring infrastructure.

The "Dead man's switch" is a simple Prometheus alerting rule that always triggers. The Alertmanager continuously sends notifications for the dead man's switch to the notification provider that supports this functionality. This also ensures that communication between the Alertmanager and the notification provider is working.

This mechanism is supported by PagerDuty to issue alerts when the monitoring system itself is down.

