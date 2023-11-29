:_mod-docs-content-type: ASSEMBLY
[id="odc-exporting-applications"]
= Exporting applications
include::_attributes/common-attributes.adoc[]
:context: odc-exporting-applications

toc::[]

As a developer, you can export your application in the ZIP file format. Based on your needs, import the exported application to another project in the same cluster or a different cluster by using the *Import YAML* option in the *+Add* view. Exporting your application helps you to reuse your application resources and saves your time.

[id="prerequisites_odc-exporting-applications"]
== Prerequisites

* You have installed the gitops-primer Operator from the OperatorHub.
+
[NOTE]
====
The *Export application* option is disabled in the *Topology* view even after installing the gitops-primer Operator.
====

* You have created an application in the *Topology* view to enable *Export application*.

[id="odc-exporting-applications-procedure"]
== Procedure

. In the developer perspective, perform one of the following steps:
.. Navigate to the *+Add* view and click *Export application* in the *Application portability* tile.
.. Navigate to the *Topology* view and click *Export application*.

. Click *OK* in the *Export Application* dialog box. A notification opens to confirm that the export of resources from your project has started.

. Optional steps that you might need to perform in the following scenarios:
+
* If you have started exporting an incorrect application, click  *Export application* -> *Cancel Export*.
* If your export is already in progress and you want to start a fresh export, click  *Export application* -> *Restart Export*.
* If you want to view logs associated with exporting an application, click  *Export application* and the *View Logs* link.
+
image::export-application-dialog-box.png[]

. After a successful export, click *Download* in the dialog box to download application resources in ZIP format onto your machine.
