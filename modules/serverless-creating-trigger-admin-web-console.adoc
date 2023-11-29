// Module included in the following assemblies:
//
// * serverless/admin_guide/serverless-cluster-admin-eventing.adoc
// * serverless/eventing/triggers/create-trigger-admin.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-creating-trigger-admin-web-console_{context}"]
= Creating a trigger by using the Administrator perspective

Using the {product-title} web console provides a streamlined and intuitive user interface to create a trigger. After Knative Eventing is installed on your cluster and you have created a broker, you can create a trigger by using the web console.


.Prerequisites

* The {ServerlessOperatorName} and Knative Eventing are installed on your {product-title} cluster.

* You have logged in to the web console and are in the *Administrator* perspective.

ifdef::openshift-enterprise[]
* You have cluster administrator permissions for {product-title}.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have cluster or dedicated administrator permissions for {product-title}.
endif::[]

* You have created a Knative broker.

* You have created a Knative service to use as a subscriber.

.Procedure

. In the *Administrator* perspective of the {product-title} web console, navigate to *Serverless* -> *Eventing*.
. In the *Broker* tab, select the Options menu {kebab} for the broker that you want to add a trigger to.
. Click *Add Trigger* in the list.
. In the *Add Trigger* dialogue box, select a *Subscriber* for the trigger. The subscriber is the Knative service that will receive events from the broker.
. Click *Add*.
