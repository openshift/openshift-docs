// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE

[id="resolver-hub-config_{context}"]
= Configuring the hub resolver

You can change the default hub for pulling a resource, and the default catalog settings, by configuring the hub resolver.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
. In the `TektonConfig` custom resource, edit the `pipeline.hub-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    hub-resolver-config:
      default-tekton-hub-catalog: Tekton # <1>
      default-artifact-hub-task-catalog: tekton-catalog-tasks # <2>
      default-artifact-hub-pipeline-catalog: tekton-catalog-pipelines # <3>
      defailt-kind: pipeline # <4>
      default-type: tekton # <5>
      tekton-hub-api: "https://my-custom-tekton-hub.example.com" # <6>
      artifact-hub-api: "https://my-custom-artifact-hub.example.com" # <7>
----
<1> The default {tekton-hub} catalog for pulling a resource.
<2> The default {artifact-hub} catalog for pulling a task resource.
<3> The default {artifact-hub} catalog for pulling a pipeline resource.
<4> The default object kind for references.
<5> The default hub for pulling a resource, either `artifact` for {artifact-hub} or `tekton` for {tekton-hub}.
<6> The {tekton-hub} API used, if the `default-type` option is set to `tekton`.
<7> Optional: The {artifact-hub} API used, if the `default-type` option is set to `artifact`.
+
[IMPORTANT]
====
If you set the `default-type` option to `tekton`, you must configure your own instance of the {tekton-hub} by setting the `tekton-hub-api` value.

If you set the `default-type` option to `artifact` then the resolver uses the public hub API at https://artifacthub.io/ by default. You can configure your own {artifact-hub} API by setting the `artifact-hub-api` value.
====
