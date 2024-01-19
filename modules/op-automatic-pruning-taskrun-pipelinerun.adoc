// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-automatic-pruning-taskrun-pipelinerun_{context}"]
= Automatic pruning of task runs and pipeline runs

Stale `TaskRun` and `PipelineRun` objects and their executed instances occupy physical resources that can be used for active runs. For optimal utilization of these resources, {pipelines-title} provides a pruner component that automatically removes unused objects and their instances in various namespaces.

[NOTE]
====
You can configure the pruner for your entire installation by using the `TektonConfig` custom resource and modify configuration for a namespace by using namespace annotations. However, you cannot selectively auto-prune an individual task run or pipeline run in a namespace.
====
