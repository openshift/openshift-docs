// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-custom-event-sources.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-odc-create-containersource_{context}"]
= Creating a container source by using the web console

After Knative Eventing is installed on your cluster, you can create a container source by using the web console. Using the {product-title} web console provides a streamlined and intuitive user interface to create an event source.

.Prerequisites

* You have logged in to the {product-title} web console.
* The {ServerlessOperatorName}, Knative Serving, and Knative Eventing are installed on your {product-title} cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

. In the *Developer* perspective, navigate to *+Add* → *Event Source*. The  *Event Sources* page is displayed.

. Select *Container Source* and then click *Create Event Source*. The  *Create Event Source* page is displayed.

. Configure the *Container Source* settings by using the *Form view* or *YAML view*:
+
[NOTE]
====
You can switch between the *Form view* and *YAML view*. The data is persisted when switching between the views.
====
.. In the *Image* field, enter the URI of the image that you want to run in the container created by the container source.
.. In the *Name* field, enter the name of the image.
.. Optional: In the *Arguments* field, enter any arguments to be passed to the container.
// Optional? Add options and what they mean.
// Same for env variables...
.. Optional: In the *Environment variables* field, add any environment variables to set in the container.
.. In the *Sink* section, add a sink where events from the container source are routed to. If you are using the *Form* view, you can choose from the following options:
... Select *Resource* to use a channel, broker, or service as a sink for the event source.
... Select *URI* to specify where the events from the container source are routed to.

. After you have finished configuring the container source, click *Create*.
