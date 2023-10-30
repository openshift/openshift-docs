// Module included in the following assemblies:
//
// * serverless/develop/serverless-traffic-management.adoc

:_mod-docs-content-type: PROCEDURE
[id="odc-splitting-traffic-between-revisions-using-developer-perspective_{context}"]
= Managing traffic between revisions by using the {product-title} web console

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have logged in to the {product-title} web console.

.Procedure

To split traffic between multiple revisions of an application in the *Topology* view:

. Click the Knative service to see its overview in the side panel.
. Click the *Resources* tab, to see a list of *Revisions* and *Routes* for the service.
+
.Serverless application
image::odc-serverless-app.png[]

. Click the service, indicated by the *S* icon at the top of the side panel, to see an overview of the service details.
. Click the *YAML* tab and modify the service configuration in the YAML editor, and click *Save*. For example, change the `timeoutseconds` from 300 to 301 . This change in the configuration triggers a new revision. In the *Topology* view, the latest revision is displayed and the *Resources* tab for the service now displays the two revisions.
. In the *Resources* tab, click btn:[Set Traffic Distribution] to see the traffic distribution dialog box:
.. Add the split traffic percentage portion for the two revisions in the *Splits* field.
.. Add tags to create custom URLs for the two revisions.
.. Click *Save* to see two nodes representing the two revisions in the Topology view.
+
.Serverless application revisions
image::odc-serverless-revisions.png[]
