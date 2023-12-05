// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="enabling-insights-advisor-recommendations_{context}"]
= Enabling a previously disabled Insights Advisor recommendation

When a recommendation is disabled for all clusters, you no longer see the recommendation in the Insights Advisor. You can change this behavior.

.Prerequisites

* Remote health reporting is enabled, which is the default.
* Your cluster is registered on {cluster-manager-url}.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
. Filter the recommendations to display on the disabled recommendations:
.. From the *Status* drop-down menu, select *Status*.
.. From the *Filter by status* drop-down menu, select *Disabled*.
.. Optional: Clear the *Clusters impacted* filter.
. Locate the recommendation to enable.
. Click the *Options* menu {kebab}, and then click *Enable recommendation*.
