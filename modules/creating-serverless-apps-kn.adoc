// Module included in the following assemblies:
//
// * serverless/develop/serverless-applications.adoc
// * serverless/reference/kn-serving-ref.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-serverless-apps-kn_{context}"]
= Creating serverless applications by using the Knative CLI

Using the Knative (`kn`) CLI to create serverless applications provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service create` command to create a basic serverless application.

.Prerequisites

* {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

* Create a Knative service:
+
[source,terminal]
----
$ kn service create <service-name> --image <image> --tag <tag-value>
----
+
Where:
+
** `--image` is the URI of the image for the application.
** `--tag` is an optional flag that can be used to add a tag to the initial revision that is created with the service.
+
.Example command
[source,terminal]
----
$ kn service create event-display \
    --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
+
.Example output
[source,terminal]
----
Creating service 'event-display' in namespace 'default':

  0.271s The Route is still working to reflect the latest desired specification.
  0.580s Configuration "event-display" is waiting for a Revision to become ready.
  3.857s ...
  3.861s Ingress has not yet been reconciled.
  4.270s Ready to serve.

Service 'event-display' created with latest revision 'event-display-bxshg-1' and URL:
http://event-display-default.apps-crc.testing
----
