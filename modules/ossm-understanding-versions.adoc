// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc
// * service_mesh/v2x/ossm-troubleshooting.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-versions_{context}"]
= Understanding Service Mesh versions

In order to understand what version of {SMProductName} you have deployed on your system, you need to understand how each of the component versions is managed.

* *Operator* version - The most current Operator version is {SMProductVersion}. The Operator version number only indicates the version of the currently installed Operator. Because the {SMProductName} Operator supports multiple versions of the {SMProductShortName} control plane, the version of the Operator does not determine the version of your deployed `ServiceMeshControlPlane` resources.
+
[IMPORTANT]
====
Upgrading to the latest Operator version automatically applies patch updates, but does not automatically upgrade your {SMProductShortName} control plane to the latest minor version.
====
+
* *ServiceMeshControlPlane* version - The `ServiceMeshControlPlane` version determines what version of {SMProductName} you are using. The value of the `spec.version` field in the `ServiceMeshControlPlane` resource controls the architecture and configuration settings that are used to install and deploy {SMProductName}. When you create the {SMProductShortName} control plane you can set the version in one of two ways:

** To configure in the Form View, select the version from the *Control Plane Version* menu.

** To configure in the YAML View, set the value for `spec.version` in the YAML file.

Operator Lifecycle Manager (OLM) does not manage {SMProductShortName} control plane upgrades, so the version number for your Operator and `ServiceMeshControlPlane` (SMCP) may not match, unless you have manually upgraded your SMCP.
