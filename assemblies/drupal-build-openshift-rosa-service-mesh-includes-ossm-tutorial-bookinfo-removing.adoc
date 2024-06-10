////
This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc
////

:_mod-docs-content-type: PROCEDURE
[id="ossm-tutorial-bookinfo-removing_{context}"]
= Removing the Bookinfo application

Follow these steps to remove the Bookinfo application.

.Prerequisites

* {product-title} 4.1 or higher installed.
* {SMProductName} {SMProductVersion} installed.
* Access to the OpenShift CLI (`oc`).

[id="ossm-delete-bookinfo-project_{context}"]
== Delete the Bookinfo project

.Procedure

. Log in to the {product-title} web console.

. Click to *Home* -> *Projects*.

. Click the `bookinfo` menu {kebab}, and then click *Delete Project*.

. Type `bookinfo` in the confirmation dialog box, and then click *Delete*.
+
** Alternatively, you can run this command using the CLI to create the `bookinfo` project.
+
[source,terminal]
----
$ oc delete project bookinfo
----

[id="ossm-remove-bookinfo-smmr_{context}"]
== Remove the Bookinfo project from the {SMProductShortName} member roll

.Procedure

. Log in to the {product-title} web console.

. Click *Operators* -> *Installed Operators*.

. Click the *Project* menu and choose `istio-system` from the list.

. Click the *Istio Service Mesh Member Roll* link under *Provided APIS* for the *{SMProductName}* Operator.

. Click the `ServiceMeshMemberRoll` menu {kebab} and select *Edit Service Mesh Member Roll*.

. Edit the default Service Mesh Member Roll YAML and remove `bookinfo` from the *members* list.
+
** Alternatively, you can run this command using the CLI to remove the `bookinfo` project from the `ServiceMeshMemberRoll`. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
$ oc -n istio-system patch --type='json' smmr default -p '[{"op": "remove", "path": "/spec/members", "value":["'"bookinfo"'"]}]'
----

. Click *Save* to update Service Mesh Member Roll.
