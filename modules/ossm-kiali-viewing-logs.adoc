////
Module included in the following assemblies:
* service_mesh/v2x/ossm-observability.adoc
////

:_mod-docs-content-type: PROCEDURE
[id="ossm-viewing-logs_{context}"]
= Viewing logs in the Kiali console

You can view logs for your workloads in the Kiali console.  The *Workload Detail* page includes a *Logs* tab which displays a unified logs view that displays both application and proxy logs. You can select how often you want the log display in Kiali to be refreshed.

To change the logging level on the logs displayed in Kiali, you change the logging configuration for the workload or the proxy.

.Prerequisites

* Service Mesh installed and configured.
* Kiali installed and configured.
* The address for the Kiali console.
* Application or Bookinfo sample application added to the mesh.

.Procedure

. Launch the Kiali console.

. Click *Log In With OpenShift*.
+
The Kiali Overview page displays namespaces that have been added to the mesh that you have permissions to view.
+
. Click *Workloads*.

. On the *Workloads* page, select the project from the *Namespace* menu.

. If necessary, use the filter to find the workload whose logs you want to view.  Click the workload *Name*.  For example, click *ratings-v1*.

. On the *Workload Details* page, click the *Logs* tab to view the logs for the workload.

[TIP]
====
If you do not see any log entries, you may need to adjust either the Time Range or the Refresh interval.
====
