// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: REFERENCE
[id="op-optional-configuration-fields_{context}"]
= Optional configuration fields

The following fields do not have a default value, and are considered only if you configure them. By default, the Operator does not add and configure these fields in the `TektonConfig` custom resource (CR).

* `default-timeout-minutes`: This field sets the default timeout for the `TaskRun` and `PipelineRun` resources, if none is specified when creating them. If a task run or pipeline run takes more time than the set number of minutes for its execution, then the task run or pipeline run is timed out and cancelled. For example, `default-timeout-minutes: 60` sets 60 minutes as default.

* `default-managed-by-label-value`: This field contains the default value given to the `app.kubernetes.io/managed-by` label that is applied to all `TaskRun` pods, if none is specified. For example, `default-managed-by-label-value: tekton-pipelines`.

* `default-pod-template`: This field sets the default `TaskRun` and `PipelineRun` pod templates, if none is specified.

* `default-cloud-events-sink`: This field sets the default `CloudEvents` sink that is used for the `TaskRun` and `PipelineRun` resources, if none is specified.

* `default-task-run-workspace-binding`: This field contains the default workspace configuration for the workspaces that a `Task` resource declares, but a `TaskRun` resource does not explicitly declare.

* `default-affinity-assistant-pod-template`: This field sets the default `PipelineRun` pod template that is used for affinity assistant pods, if none is specified.

* `default-max-matrix-combinations-count`: This field contains the default maximum number of combinations generated from a matrix, if none is specified.
