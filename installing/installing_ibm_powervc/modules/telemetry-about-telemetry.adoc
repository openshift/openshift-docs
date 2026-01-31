// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

:_mod-docs-content-type: CONCEPT
[id="telemetry-about-telemetry_{context}"]
= About Telemetry

Telemetry sends a carefully chosen subset of the cluster monitoring metrics to Red Hat. The Telemeter Client fetches the metrics values every four minutes and thirty seconds and uploads the data to Red Hat. These metrics are described in this document.

This stream of data is used by Red Hat to monitor the clusters in real-time and to react as necessary to problems that impact our customers. It also allows Red Hat to roll out {product-title} upgrades to customers to minimize service impact and continuously improve the upgrade experience.

This debugging information is available to Red Hat Support and Engineering teams with the same restrictions as accessing data reported through support cases. All connected cluster information is used by Red Hat to help make {product-title} better and more intuitive to use.
