// Module included in the following assemblies:
//
//  * /serverless/develop/serverless-creating-channels.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-create-channel-odc_{context}"]
= Creating a channel by using the Developer perspective

Using the {product-title} web console provides a streamlined and intuitive user interface to create a channel. After Knative Eventing is installed on your cluster, you can create a channel by using the web console.

.Prerequisites

* You have logged in to the {product-title} web console.
* The {ServerlessOperatorName} and Knative Eventing are installed on your {product-title} cluster.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in {product-title}.

.Procedure

. In the *Developer* perspective, navigate to *+Add* -> *Channel*.
. Select the type of `Channel` object that you want to create in the *Type* list.
. Click *Create*.

.Verification

* Confirm that the channel now exists by navigating to the *Topology* page.
+
image::verify-channel-odc.png[View the channel in the Topology view]
