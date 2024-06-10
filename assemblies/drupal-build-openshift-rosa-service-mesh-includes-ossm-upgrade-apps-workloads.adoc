// Module included in the following assemblies:
// * service_mesh/v2x/upgrading-ossm.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-upgrading-apps-workloads_{context}"]
= Updating your applications and workloads

To complete the migration, restart all of the application pods in the mesh to upgrade the Envoy sidecar proxies and their configuration.

To perform a rolling update of a deployment use the following command:

[source,terminal]
----
$ oc rollout restart <deployment>
----

You must perform a rolling update for all applications that make up the mesh.
