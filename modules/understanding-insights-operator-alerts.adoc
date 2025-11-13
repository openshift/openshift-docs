// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-operator.adoc


:_mod-docs-content-type: CONCEPT
[id="understanding-insights-operator-alerts_{context}"]
= Understanding Insights Operator alerts

The Insights Operator declares alerts through the Prometheus monitoring system to the Alertmanager. You can view these alerts in the Alerting UI in the {product-title} web console by using one of the following methods:

* In the *Administrator* perspective, click *Observe* -> *Alerting*.
* In the *Developer* perspective, click *Observe* -> <project_name> -> *Alerts* tab.

Currently, Insights Operator sends the following alerts when the conditions are met:

.Insights Operator alerts
[options="header"]
|====
|Alert|Description
|`InsightsDisabled`|Insights Operator is disabled.
|`SimpleContentAccessNotAvailable`|Simple content access is not enabled in Red Hat Subscription Management.
|`InsightsRecommendationActive`|Insights has an active recommendation for the cluster.
|====
