// Module included in the following assemblies:
//
// * /serverless/eventing/event-sources/serverless-pingsource.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-pingsource-odc_{context}"]
= Creating a ping source by using the web console

After Knative Eventing is installed on your cluster, you can create a ping source by using the web console. Using the {product-title} web console provides a streamlined and intuitive user interface to create an event source.

.Prerequisites

* You have logged in to the {product-title} web console.
* The {ServerlessOperatorName}, Knative Serving and Knative Eventing are installed on the cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

. To verify that the ping source is working, create a simple Knative
service that dumps incoming messages to the logs of the service.

.. In the *Developer* perspective, navigate to *+Add* -> *YAML*.
.. Copy the example YAML:
+
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: event-display
spec:
  template:
    spec:
      containers:
        - image: quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
.. Click *Create*.

. Create a ping source in the same namespace as the service created in the previous step, or any other sink that you want to send events to.

.. In the *Developer* perspective, navigate to *+Add* -> *Event Source*. The  *Event Sources* page is displayed.
.. Optional: If you have multiple providers for your event sources, select the required provider from the *Providers* list to filter the available event sources from the provider.
.. Select *Ping Source* and then click *Create Event Source*. The *Create Event Source* page is displayed.
+
[NOTE]
====
You can configure the *PingSource* settings by using the *Form view* or *YAML view* and can switch between the views. The data is persisted when switching between the views.
====
.. Enter a value for *Schedule*. In this example, the value is `*/2 * * * *`, which creates a PingSource that sends a message every two minutes.
.. Optional: You can enter a value for *Data*, which is the message payload.
.. Select a *Sink*. This can be either a *Resource* or a *URI*. In this example, the `event-display` service created in the previous step is used as the *Resource* sink.
.. Click *Create*.

.Verification

You can verify that the ping source was created and is connected to the sink by viewing the *Topology* page.

. In the *Developer* perspective, navigate to *Topology*.
. View the ping source and sink.
+
image::verify-pingsource-ODC.png[View the ping source and service in the Topology view]

.Deleting the ping source
// move to separate procedure, out of scope for this PR

. Navigate to the *Topology* view.
. Right-click the API server source and select *Delete Ping Source*.
