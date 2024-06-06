// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-upgrading-smcp_{context}"]
= Upgrading the Service Mesh control plane

To upgrade {SMProductName}, you must update the version field of the {SMProductName} `ServiceMeshControlPlane` v2 resource. Then, once it is configured and applied, restart the application pods to update each sidecar proxy and its configuration.

.Prerequisites

* You are running {product-title} 4.9 or later.
* You have the latest {SMProductName} Operator.

.Procedure

. Switch to the project that contains your `ServiceMeshControlPlane` resource. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.
+
[source,terminal]
----
$ oc project istio-system
----

. Check your v2 `ServiceMeshControlPlane` resource configuration to verify it is valid.
+
.. Run the following command to view your `ServiceMeshControlPlane` resource as a v2 resource.
+
[source,terminal]
----
$ oc get smcp -o yaml
----
+
[TIP]
====
Back up your {SMProductShortName} control plane configuration.
====

. Update the `.spec.version` field and apply the configuration.
+
For example:
+
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  version: v{MaistraVersion}
----
+
Alternatively, instead of using the command line, you can use the web console to edit the {SMProductShortName} control plane. In the {product-title} web console, click *Project* and select the project name you just entered.
+
.. Click *Operators* -> *Installed Operators*.
.. Find your `ServiceMeshControlPlane` instance.
.. Select *YAML view* and update text of the YAML file, as shown in the previous example.
.. Click *Save*.
