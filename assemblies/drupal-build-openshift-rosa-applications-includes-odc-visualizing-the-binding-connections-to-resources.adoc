// Module included in the following assemblies:
//
// * applications/connecting_applications_to_services/odc-connecting-an-application-to-a-service-using-the-developer-perspective.adoc

:_mod-docs-content-type: PROCEDURE
[id="odc-visualizing-the-binding-connections-to-resources_{context}"]
= Visualizing the binding connections to resources

As a user, use *Label Selector* in the *Topology* view to visualize a service binding and simplify the process of binding applications to backing services. When creating `ServiceBinding` resources, specify labels by using *Label Selector* to find and connect applications instead of using the name of the application. The Service Binding Operator then consumes these `ServiceBinding` resources and specified labels to find the applications to create a service binding with.


[TIP]
====
To navigate to a list of all connected resources, click the label selector associated with the `ServiceBinding` resource.
====

To view the *Label Selector*, consider the following approaches:

** After you import a `ServiceBinding` resource, view the *Label Selector* associated with the service binding on the *ServiceBinding details* page.

+
.ServiceBinding details page
image::odc-label-selector-sb-details.png[]

[NOTE]
====
To use *Label Selector* and to create one or more connections at once, you must import the YAML file of the `ServiceBinding` resource.
====

** After the connection is established and when you click the binding connector, the service binding connector *Details* side panel appears. You can view the *Label Selector* associated with the service binding on this panel.

+
.Topology label selector side panel
image::odc-label-selector-topology-side-panel.png[]

+
[NOTE]
====
When you delete a binding connector (a single connection within *Topology* along with a service binding), the action removes all connections that are tied to the deleted service binding. While deleting a binding connector, a confirmation dialog appears, which informs that all connectors will be deleted.

.Delete ServiceBinding confirmation dialog
image::odc-delete-service-binding.png[]

====