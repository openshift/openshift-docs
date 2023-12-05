// Module included in the following assemblies:
//
// * support/remote_health_monitoring/using-insights-to-identify-issues-with-your-cluster.adoc

:_mod-docs-content-type: CONCEPT
[id="insights-operator-advisor-recommendations_{context}"]
= Understanding Insights Advisor recommendations

Insights Advisor bundles information about various cluster states and component configurations that can negatively affect the service availability, fault tolerance, performance, or security of your clusters. This information set is called a recommendation in Insights Advisor and includes the following information:

* *Name:* A concise description of the recommendation
* *Added:* When the recommendation was published to the Insights Advisor archive
* *Category:* Whether the issue has the potential to negatively affect service availability, fault tolerance, performance, or security
* *Total risk:* A value derived from the _likelihood_ that the condition will negatively affect your infrastructure, and the _impact_ on operations if that were to happen
* *Clusters:* A list of clusters on which a recommendation is detected
* *Description:* A brief synopsis of the issue, including how it affects your clusters
* *Link to associated topics:* More information from Red Hat about the issue
