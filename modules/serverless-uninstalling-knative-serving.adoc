// Module included in the following assemblies:
//
// * serverless/install/removing-openshift-serverless.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-uninstalling-knative-serving_{context}"]
= Uninstalling Knative Serving

.Prerequisites

ifdef::openshift-enterprise[]
* You have access to an {product-title} account with cluster administrator access.
endif::[]

ifdef::openshift-dedicated,openshift-rosa[]
* You have access to an {product-title} account with cluster administrator or dedicated administrator access.
endif::[]

* Install the OpenShift CLI (`oc`).

.Procedure

. Delete the `KnativeServing` CR:
+
[source,terminal]
----
$ oc delete knativeservings.operator.knative.dev knative-serving -n knative-serving
----

. After the command has completed and all pods have been removed from the `knative-serving` namespace, delete the namespace:
+
[source,terminal]
----
$ oc delete namespace knative-serving
----
