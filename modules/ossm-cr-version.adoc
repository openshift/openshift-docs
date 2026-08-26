// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-reference-smcp.adoc

:_mod-docs-content-type: REFERENCE
[id="ossm-cr-version_{context}"]
= version parameter

The {SMProductName} Operator supports installation of different versions of the `ServiceMeshControlPlane`. You use the version parameter to specify what version of the {SMProductShortName} control plane to install. If you do not specify a version parameter when creating your SMCP, the Operator sets the value to the latest version: ({MaistraVersion}). Existing `ServiceMeshControlPlane` objects keep their version setting during upgrades of the Operator.
