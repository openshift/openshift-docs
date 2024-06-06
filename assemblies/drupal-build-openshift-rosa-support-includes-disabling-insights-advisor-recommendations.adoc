// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="disabling-insights-advisor-recommendations_{context}"]
= Disabling Insights Advisor recommendations

You can disable specific recommendations that affect your clusters, so that they no longer appear in your reports. It is possible to disable a recommendation for a single cluster or all of your clusters.

[NOTE]
====
Disabling a recommendation for all of your clusters also applies to any future clusters.
====

.Prerequisites

* Remote health reporting is enabled, which is the default.
* Your cluster is registered on {cluster-manager-url}.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
. Optional: Use the *Clusters Impacted* and *Status* filters as needed.
. Disable an alert by using one of the following methods:
+
* To disable an alert:
.. Click the *Options* menu {kebab} for that alert, and then click *Disable recommendation*.
.. Enter a justification note and click *Save*.
+
* To view the clusters affected by this alert before disabling the alert:
.. Click the name of the recommendation to disable. You are directed to the single recommendation page.
.. Review the list of clusters in the *Affected clusters* section.
.. Click *Actions* -> *Disable recommendation* to disable the alert for all of your clusters.
.. Enter a justification note and click *Save*.
