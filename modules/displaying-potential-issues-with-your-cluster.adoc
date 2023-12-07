// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

:_mod-docs-content-type: PROCEDURE
[id="displaying-potential-issues-with-your-cluster_{context}"]
= Displaying potential issues with your cluster

This section describes how to display the Insights report in *Insights Advisor* on {cluster-manager-url}.

Note that Insights repeatedly analyzes your cluster and shows the latest results. These results can change, for example, if you fix an issue or a new issue has been detected.

.Prerequisites

* Your cluster is registered on {cluster-manager-url}.
* Remote health reporting is enabled, which is the default.
* You are logged in to {cluster-manager-url}.

.Procedure

. Navigate to *Advisor* -> *Recommendations* on {cluster-manager-url}.
+
Depending on the result, Insights Advisor displays one of the following:
+
* *No matching recommendations found*, if Insights did not identify any issues.
+
* A list of issues Insights has detected, grouped by risk (low, moderate, important, and critical).
+
* *No clusters yet*, if Insights has not yet analyzed the cluster. The analysis starts shortly after the cluster has been installed, registered, and connected to the internet.

. If any issues are displayed, click the *>* icon in front of the entry for more details.
+
Depending on the issue, the details can also contain a link to more information from Red Hat about the issue.
