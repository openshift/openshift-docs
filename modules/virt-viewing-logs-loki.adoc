// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-viewing-logs-loki_{context}"]
= Viewing aggregated {VirtProductName} logs with the LokiStack

You can view aggregated logs for {VirtProductName} pods and containers by using the LokiStack in the web console.

.Prerequisites

* You deployed the LokiStack.

.Procedure

. Navigate to *Observe* -> *Logs* in the web console.
. Select *application*, for `virt-launcher` pod logs, or *infrastructure*, for {VirtProductName} control plane pods and containers, from the log type list.
. Click *Show Query* to display the query field.
. Enter the LogQL query in the query field and click *Run Query* to display the filtered logs.
