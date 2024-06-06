// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-threescale-routing_{context}"]
= Routing service traffic through the adapter
Follow these steps to drive traffic for your service through the 3scale adapter.

.Prerequisites

* Credentials and service ID from your 3scale administrator.

.Procedure

. Match the rule `destination.labels["service-mesh.3scale.net/credentials"] == "threescale"` that you previously created in the configuration, in the `kind: rule` resource.

. Add the above label to `PodTemplateSpec` on the Deployment of the target workload to integrate a service. the value, `threescale`, refers to the name of the generated handler. This handler stores the access token required to call 3scale.

. Add the `destination.labels["service-mesh.3scale.net/service-id"] == "replace-me"` label to the workload to pass the service ID to the adapter via the instance at request time.
