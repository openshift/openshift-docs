// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: REFERENCE
[id="op-modifiable-fields-with-default-values_{context}"]
= Modifiable fields with default values

The following list includes all modifiable fields with their default values in the `TektonConfig` CR:

* `running-in-environment-with-injected-sidecars` (default: `true`): Set this field to `false` if pipelines run in a cluster that does not use injected sidecars, such as Istio. Setting it to `false` decreases the time a pipeline takes for a task run to start.
+
[NOTE]
====
For clusters that use injected sidecars, setting this field to `false` can lead to an unexpected behavior.
====

* `await-sidecar-readiness` (default: `true`): Set this field to `false` to stop {pipelines-shortname} from waiting for `TaskRun` sidecar containers to run before it begins to operate. This allows tasks to be run in environments that do not support the `downwardAPI` volume type.

* `default-service-account` (default: `pipeline`): This field contains the default service account name to use for the `TaskRun` and `PipelineRun` resources, if none is specified.

* `require-git-ssh-secret-known-hosts` (default: `false`): Setting this field to `true` requires that any Git SSH secret must include the `known_hosts` field.

** For more information about configuring Git SSH secrets, see  _Configuring SSH authentication for Git_ in the _Additional resources_ section.

* `enable-tekton-oci-bundles` (default: `false`): Set this field to `true` to enable the use of an experimental alpha feature named Tekton OCI bundle.

* `enable-api-fields` (default: `stable`): Setting this field determines which features are enabled. Acceptable value is `stable`, `beta`, or `alpha`.
+
[NOTE]
====
{pipelines-title} does not support the `alpha` value.
====

* `enable-provenance-in-status` (default: `false`): Set this field to `true` to enable populating the `provenance` field in `TaskRun` and `PipelineRun` statuses. The `provenance` field contains metadata about resources used in the task run and pipeline run, such as the source from where a remote task or pipeline definition was fetched.

* `enable-custom-tasks` (default: `true`): Set this field to `false` to disable the use of custom tasks in pipelines.

* `disable-creds-init` (default: `false`): Set this field to `true` to prevent {pipelines-shortname} from scanning attached service accounts and injecting any credentials into your steps.

* `disable-affinity-assistant` (default: `true`): Set this field to `false` to enable affinity assistant for each `TaskRun` resource sharing a persistent volume claim workspace.

.Metrics options
You can modify the default values of the following metrics fields in the `TektonConfig` CR:

* `metrics.taskrun.duration-type` and `metrics.pipelinerun.duration-type` (default: `histogram`): Setting these fields determines the duration type for a task or pipeline run. Acceptable value is `gauge` or `histogram`.

* `metrics.taskrun.level` (default: `task`): This field determines the level of the task run metrics. Acceptable value is `taskrun`, `task`, or `namespace`.

* `metrics.pipelinerun.level` (default: `pipeline`): This field determines the level of the pipeline run metrics. Acceptable value is `pipelinerun`, `pipeline`, or `namespace`.
