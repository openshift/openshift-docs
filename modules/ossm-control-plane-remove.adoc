// Module included in the following assemblies:
//
// * service_mesh/v1x/installing-ossm.adoc
// * service_mesh/v2x/installing-ossm.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-control-plane-remove_{context}"]
= Removing the {SMProductName} control plane

To uninstall {SMProductShortName} from an existing {product-title} instance, first you delete the {SMProductShortName} control plane and the Operators. Then, you run commands to remove residual resources.

[id="ossm-control-plane-remove-operatorhub_{context}"]
== Removing the {SMProductShortName} control plane using the web console

You can remove the {SMProductName} control plane by using the web console.

.Procedure

. Log in to the {product-title} web console.

. Click the *Project* menu and select the project where you installed the {SMProductShortName} control plane, for example *istio-system*.

. Navigate to *Operators* -> *Installed Operators*.

. Click *Service Mesh Control Plane* under *Provided APIs*.

. Click the `ServiceMeshControlPlane` menu {kebab}.

. Click *Delete Service Mesh Control Plane*.

. Click *Delete* on the confirmation dialog window to remove the `ServiceMeshControlPlane`.

[id="ossm-control-plane-remove-cli_{context}"]
== Removing the {SMProductShortName} control plane using the CLI

You can remove the {SMProductName} control plane by using the CLI.  In this example, `istio-system` is the name of the control plane project.

.Procedure

. Log in to the {product-title} CLI.

. Run the following command to delete the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc delete smmr -n istio-system default
----

. Run this command to retrieve the name of the installed `ServiceMeshControlPlane`:
+
[source,terminal]
----
$ oc get smcp -n istio-system
----

. Replace `<name_of_custom_resource>` with the output from the previous command, and run this command to remove the custom resource:
+
[source,terminal]
----
$ oc delete smcp -n istio-system <name_of_custom_resource>
----
