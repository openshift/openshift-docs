:_mod-docs-content-type: PROCEDURE
[id="odc-adding-services-to-your-application_{context}"]
= Adding services to your application

To add a service to your application use the *+Add* actions using the context menu in the topology *Graph view*.

[NOTE]
====
In addition to the context menu, you can add services by using the sidebar or hovering and dragging the dangling arrow from the application group.
====

.Procedure

1. Right-click an application group in the topology *Graph view* to display the context menu.
+
.Add resource context menu
image::odc_context_menu.png[]

2. Use *Add to Application* to select a method for adding a service to the application group, such as *From Git*, *Container Image*, *From Dockerfile*, *From Devfile*, *Upload JAR file*, *Event Source*, *Channel*, or *Broker*.

3. Complete the form for the method you choose and click *Create*. For example, to add a service based on the source code in your Git repository, choose the *From Git* method, fill in the *Import from Git* form, and click *Create*.
