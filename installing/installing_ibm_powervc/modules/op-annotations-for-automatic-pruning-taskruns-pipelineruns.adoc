// This module is included in the following assembly:
//
// cicd/pipelines/automatic-pruning-taskrun-pipelinerun.adoc

:_mod-docs-content-type: REFERENCE
[id="annotations-for-automatic-pruning-taskruns-pipelineruns_{context}"]
= Annotations for automatically pruning task runs and pipeline runs

To modify the configuration for automatic pruning of task runs and pipeline runs in a namespace, you can set annotations in the namespace.

The following namespace annotations have the same meanings as the corresponding keys in the `TektonConfig` custom resource:

* `operator.tekton.dev/prune.schedule`
* `operator.tekton.dev/prune.resources`
* `operator.tekton.dev/prune.keep`
* `operator.tekton.dev/prune.prune-per-resource`
* `operator.tekton.dev/prune.keep-since`

[NOTE]
====
The `operator.tekton.dev/prune.resources` annotation accepts a comma-separated list. To prune both task runs and pipeline runs, set this annotation to `"taskrun, pipelinerun"`.
====

The following additional namespace annotations are available:

* `operator.tekton.dev/prune.skip`: When set to `true`, the namespace for which the annotation is configured is not pruned.
* `operator.tekton.dev/prune.strategy`: Set the value of this annotation to either `keep` or `keep-since`.

For example, the following annotations retain all task runs and pipeline runs created in the last five days and delete the older resources:

.Example of auto-pruning annotations
[source,yaml]
----
kind: Namespace
apiVersion: v1
# ...
spec:
  annotations:
    operator.tekton.dev/prune.resources: "taskrun, pipelinerun"
    operator.tekton.dev/prune.keep-since: 7200
# ...
----
