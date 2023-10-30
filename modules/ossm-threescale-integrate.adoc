// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-threescale-integrate_{context}"]
= Integrate the 3scale adapter with {SMProductName}

You can use these examples to configure requests to your services using the 3scale Istio Adapter.


.Prerequisites:

* {SMProductName} version 2.x
* A working 3scale account (link:https://www.3scale.net/signup/[SaaS] or link:https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.9/html/installing_3scale/install-threescale-on-openshift-guide[3scale 2.9 On-Premises])
* Enabling backend cache requires 3scale 2.9 or greater
* {SMProductName} prerequisites
* Ensure Mixer policy enforcement is enabled. Update Mixer policy enforcement section provides instructions to check the current Mixer policy enforcement status and enable policy enforcement.
* Mixer policy and telemetry must be enabled if you are using a mixer plugin.
** You will need to properly configure the Service Mesh Control Plane (SMCP) when upgrading.

[NOTE]
====
To configure the 3scale Istio Adapter, refer to {SMProductName} custom resources for instructions on adding adapter parameters to the custom resource file.
====


[NOTE]
====
Pay particular attention to the `kind: handler` resource. You must update this with your 3scale account credentials. You can optionally add a `service_id` to a handler, but this is kept for backwards compatibility only, since it would render the handler only useful for one service in your 3scale account. If you add `service_id` to a handler, enabling 3scale for other services requires you to create more handlers with different `service_ids`.
====

Use a single handler per 3scale account by following the steps below:

.Procedure

. Create a handler for your 3scale account and specify your account credentials. Omit any service identifier.
+
[source,yaml]
----
  apiVersion: "config.istio.io/v1alpha2"
  kind: handler
  metadata:
   name: threescale
  spec:
   adapter: threescale
   params:
     system_url: "https://<organization>-admin.3scale.net/"
     access_token: "<ACCESS_TOKEN>"
   connection:
     address: "threescale-istio-adapter:3333"
----
+
Optionally, you can provide a `backend_url` field within the _params_ section to override the URL provided by the 3scale configuration. This may be useful if the adapter runs on the same cluster as the 3scale on-premise instance, and you wish to leverage the internal cluster DNS.
+
. Edit or patch the Deployment resource of any services belonging to your 3scale account as follows:
.. Add the `"service-mesh.3scale.net/service-id"` label with a value corresponding to a valid `service_id`.
.. Add the `"service-mesh.3scale.net/credentials"` label with its value being the _name of the handler resource_ from step 1.
. Do step 2 to link it to your 3scale account credentials and to its service identifier, whenever you intend to add more services.
. Modify the rule configuration with your 3scale configuration to dispatch the rule to the threescale handler.
+
.Rule configuration example
[source,yaml]
----
  apiVersion: "config.istio.io/v1alpha2"
  kind: rule
  metadata:
    name: threescale
  spec:
    match: destination.labels["service-mesh.3scale.net"] == "true"
    actions:
      - handler: threescale.handler
        instances:
          - threescale-authorization.instance
----
