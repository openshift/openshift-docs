// Module included in the following assemblies:
//
// * service_mesh/v2x/customizing-installation-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-specifying-jaeger-configuration_{context}"]
= Specifying Jaeger configuration in the SMCP

You configure Jaeger under the `addons` section of the `ServiceMeshControlPlane` resource. However, there are some limitations to what you can configure in the SMCP.

When the SMCP passes configuration information to the {JaegerName} Operator, it triggers one of three deployment strategies: `allInOne`, `production`, or `streaming`.
