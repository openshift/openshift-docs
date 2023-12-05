////
This module included in the following assemblies:
-service_mesh/v2x/ossm-traffic-manage.adoc
////
:_mod-docs-content-type: PROCEDURE
[id="ossm-config-disable-networkpolicy_{context}"]
= Disabling automatic NetworkPolicy creation

If you want to disable the automatic creation and management of `NetworkPolicy` resources, for example to enforce company security policies, or to allow direct access to pods in the mesh, you can do so. You can edit the `ServiceMeshControlPlane` and set `spec.security.manageNetworkPolicy` to `false`.

[NOTE]
====
When you disable `spec.security.manageNetworkPolicy` {SMProductName} will not create *any* `NetworkPolicy` objects. The system administrator is responsible for managing the network and fixing any issues this might cause.
====

.Prerequisites

* {SMProductName} Operator version 2.1.1 or higher installed.
* `ServiceMeshControlPlane` resource updated to version 2.1 or higher.

.Procedure

. In the {product-title} web console, click *Operators* -> *Installed Operators*.

. Select the project where you installed the {SMProductShortName} control plane, for example `istio-system`, from the *Project* menu.

. Click the {SMProductName} Operator. In the *Istio Service Mesh Control Plane* column, click the name of your `ServiceMeshControlPlane`, for example `basic-install`.

. On the *Create ServiceMeshControlPlane Details* page, click `YAML` to modify your configuration.

. Set the `ServiceMeshControlPlane` field `spec.security.manageNetworkPolicy` to `false`, as shown in this example.
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
spec:
  security:
      manageNetworkPolicy: false
----
+
. Click *Save*.
