// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-pipelines-as-code-resolver_{context}"]
= Using the {pac} resolver

[role="_abstract"]
The {pac} resolver ensures that a running pipeline run does not conflict with others.

To split your pipeline and pipeline run, store the files in the `.tekton/` directory or its subdirectories.

If {pac} observes a pipeline run with a reference to a task or a pipeline in any YAML file located in the `.tekton/` directory, {pac} automatically resolves the referenced task to provide a single pipeline run with an embedded spec in a `PipelineRun` object.

If {pac} cannot resolve the referenced tasks in the `Pipeline` or `PipelineSpec` definition, the run fails before applying any changes to the cluster. You can see the issue on your Git provider platform and inside the events of the target namespace where the `Repository` CR is located.

The resolver skips resolving if it observes the following type of tasks:

* A reference to a cluster task.
* A task or pipeline bundle.
* A custom task with an API version that does not have a `tekton.dev/` prefix.

The resolver uses such tasks literally, without any transformation.

To test your pipeline run locally before sending it in a pull request, use the `tkn pac resolve` command.

You can also reference remote pipelines and tasks.
