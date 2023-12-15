// Module included in the following assemblies:
//
// * applications/connecting_applications_to_services/odc-connecting-an-application-to-a-service-using-the-developer-perspective.adoc
:_mod-docs-content-type: PROCEDURE
[id="odc-verifying-the-status-of-your-service-binding-from-the-topology-view_{context}"]
= Verifying the status of your service binding from the Topology view

The *Developer* perspective helps you verify the status of your service binding through the *Topology* view.

.Procedure

. If a service binding was successful, click the binding connector. A side panel appears displaying the *Connected* status under the *Details* tab.
+
Optionally, you can view the *Connected* status on the following pages from the *Developer* perspective:
+
** The *ServiceBindings* page.
** The *ServiceBinding details* page. In addition, the page title displays a *Connected* badge.
. If a service binding was unsuccessful, the binding connector shows a red arrowhead and a red cross in the middle of the connection. Click this connector to view the *Error* status in the side panel under the *Details* tab. Optionally, click the *Error* status to view specific information about the underlying problem.
+
You can also view the *Error* status and a tooltip on the following pages from the *Developer* perspective:
+
** The *ServiceBindings* page.
** The *ServiceBinding details* page. In addition, the page title displays an *Error* badge.


[TIP]
====
In the *ServiceBindings* page, use the *Filter* dropdown to list the service bindings based on their status.
====

