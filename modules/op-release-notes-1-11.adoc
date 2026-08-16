// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
:_mod-docs-content-type: REFERENCE
[id="op-release-notes-1-11_{context}"]
= Release notes for {pipelines-title} General Availability 1.11

With this update, {pipelines-title} General Availability (GA) 1.11 is available on {product-title} 4.12 and later versions.

[id="new-features-1-11_{context}"]
== New features

In addition to fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.11:

[NOTE]
====
Before upgrading to the {pipelines-title} Operator 1.11, ensure that you have at least installed the {product-title} 4.12.19 or 4.13.1 version on your cluster.
====

[id="pipelines-new-features-1-11_{context}"]
=== Pipelines

* With this update, you can use {pipelines-title} on the {product-title} cluster that runs on ARM hardware. You have support for the `ClusterTask` resources where images are available and the Tekton CLI tool on ARM hardware.

* This update adds support for results, object parameters, array results, and indexing into an array when you set the `enable-api-fields` feature flag to `beta` value in the `TektonConfig` CR.

* With this update, propagated parameters are now part of a stable feature. This feature enables interpolating parameters in embedded specifications to reduce verbosity in Tekton resources.

* With this update, propagated workspaces are now part of a stable feature. You can enable the propagated workspaces feature by setting the `enable-api-fields` feature flag to `alpha` or `beta` value.

* With this update, the `TaskRun` object fetches and displays the init container failure message to users when a pod fails to run.

* With this update, you can replace parameters, results, and the context of a pipeline task while configuring a matrix as per the following guidelines:
** Replace an array with an `array` parameter or a string with a `string`, `array`, or `object` parameter in the `matrix.params` configuration.
** Replace a string with a `string`, `array`, or `object` parameter in the `matrix.include` configuration.
** Replace the context of a pipeline task with another context in the `matrix.include` configuration.

* With this update, the `TaskRun` resource validation process also validates the `matrix.include` parameters. The validation checks whether all parameters have values and match the specified type, and object parameters have all the keys required.

* This update adds a new `default-resolver-type` field in the `default-configs` config map. You can set the value of this field to configure a default resolver.

* With this update, you can define and use a `PipelineRun` context variable in the `pipelineRun.workspaces.subPath` configuration.

* With this update, the `ClusterResolver`, `BundleResolver`, `HubResolver`, and `GitResolver` features are now available by default.


[id="triggers-new-features-1-11_{context}"]
=== Triggers

* With this update, Tekton Triggers support the `Affinity` and `TopologySpreadConstraints` values in the `EventListener` specification. You can use these values to configure Kubernetes and custom resources for an `EventListener` object.
* This update adds a Slack interceptor that allows you to extract fields by using a slash command in Slack. The extracted fields are sent in the form data section of an HTTP request.


[id="operator-new-features-1-11_{context}"]
=== Operator

* With this update, you can configure pruning for each `PipelineRun` or `TaskRun` resource by setting a `prune-per-resource` boolean field in the `TektonConfig` CR. You can also configure pruning for each `PipelineRun` or `TaskRun` resource in a  namespace by adding the `operator.tekton.dev/prune.prune-per-resource=true` annotation to that namespace.

* With this update, if there are any changes in the {product-title} cluster-wide proxy, Operator Lifecycle Manager (OLM) recreates the {pipelines-title} Operator.
* With this update, you can disable the pruner feature by setting the value of the `config.pruner.disabled` field to `true` in the `TektonConfig` CR.


[id="chains-new-features-1-11_{context}"]
=== {tekton-chains}

* With this update, {tekton-chains} is now generally available for use.

* With this update, you can use the skopeo tool with {tekton-chains} to generate keys, which are used in the `cosign` signing scheme.

* When you upgrade to the {pipelines-title} Operator 1.11, the previous {tekton-chains} configuration will be overwritten and you must set it again in the `TektonConfig` CR.


[id="tekton-hub-new-features-1-11_{context}"]
=== {tekton-hub}

:FeatureName: {tekton-hub}
include::snippets/technology-preview.adoc[]

* This update adds a new `resource/<catalog_name>/<kind>/<resource_name>/raw` endpoint and a new `resourceURLPath` field in the `resource` API response. This update helps you to obtain the latest raw YAML file of the resource.

[id="tekton-results-new-features-1-11_{context}"]
=== Tekton Results

:FeatureName: Tekton Results
include::snippets/technology-preview.adoc[]

* This update adds Tekton Results to the Tekton Operator as an optional component.


[id="pac-new-features-1-11_{context}"]
=== {pac}

* With this update, {pac} allows you to expand a custom parameter within your `PipelineRun` resource by using the `params` field. You can specify a value for the custom parameter inside the template of the `Repository` CR. The specified value replaces the custom parameter in your pipeline run. Also, you can define a custom parameter and use its expansion only when specified conditions are compatible with a Common Expression Language (CEL) filter.

* With this update, you can either rerun a specific pipeline or all pipelines by clicking the *Re-run all checks* button in the *Checks* tab of the GitHub interface.

* This update adds a new `tkn pac info` command to the {pac} CLI. As an administrator, you can use the `tkn pac info` command to obtain the following details about the {pac} installation:
** The location where {pac} is installed.
** The version number of {pac}.
** An overview of the `Repository` CR created on the cluster and the URL associated with the repository.
** Details of any installed GitHub applications.
+
With this command, you can also specify a custom GitHub API URL by using the `--github-api-url` argument.

* This update enables error detection for all `PipelineRun` resources by default. {pac} detects if a `PipelineRun` resource execution has failed and shows a snippet of the last few lines of the error. For a GitHub application, {pac} detects error messages in the container logs and exposes them as annotations on a pull request.

* With this update, you can fetch tasks from a private {tekton-hub} instance attached to a private Git repository. To enable this update, {pac} uses the internal raw URL of the private {tekton-hub} instance instead of using the GitHub raw URL.

* Before this update, {pac} provided logs that would not include the namespace detail. With this update, {pac} adds the namespace information to the pipeline logs so that you can filter them based on a namespace and debug easily.

* With this update, you can define the provenance source from where the `PipelineRun` resource definition is to be fetched. By default, {pac} fetches the `PipelineRun` resource definition from the branch where the event has been triggered. Now, you can configure the value of the `pipelinerun_provenance` setting to `default_branch` so that the `PipelineRun` resource definition is fetched from the default branch of the repository as configured on GitHub.

* With this update, you can extend the scope of the GitHub token at the following levels:
** Repository-level: Use this level to extend the scope to the repositories that exist in the same namespace in which the original repository exists.
** Global-level: Use this level to extend the scope to the repositories that exist in a different namespace.

* With this update, {pac} triggers a CI pipeline for a pull request created by a user who is not an owner, collaborator, or public member or is not listed in the `owner` file but has permission to push changes to the repository.

* With this update, the custom console setting allows you to use custom parameters from a `Repository` CR.

* With this update, {pac} changes all `PipelineRun` labels to `PipelineRun` annotations. You can use a `PipelineRun` annotation to mark a Tekton resource, instead of using a `PipelineRun` label.

* With this update, you can use the `pac-config-logging` config map for watcher and webhook resources, but not for the {pac} controller.


[id="breaking-changes-1-11_{context}"]
== Breaking changes

* This update replaces the `resource-verification-mode` feature flag with a new `trusted-resources-verification-no-match-policy` flag in the pipeline specification.

* With this update, you cannot edit the {tekton-chains} CR. Instead, edit the `TektonConfig` CR to configure {tekton-chains}.


[id="deprecated-features-1-11_{context}"]
== Deprecated and removed features

* This update removes support for the `PipelineResource` commands and references from Tekton CLI:
** Removal of pipeline resources from cluster tasks
** Removal of pipeline resources from tasks
** Removal of pipeline resources from pipelines
** Removal of resource commands
** Removal of input and output resources from the `clustertask describe` command

* This update removes support for the `full` embedded status from Tekton CLI.

* The `taskref.bundle` and `pipelineref.bundle` bundles are deprecated and will be removed in a future release.

* In {pipelines-title} 1.11, support for the `PipelineResource` CR has been removed, use the `Task` CR instead.

* In {pipelines-title} 1.11, support for the `v1alpha1.Run` objects has been removed. You must upgrade the objects from `v1alpha1.Run` to `v1beta1.CustomRun` before upgrading to this release.

* In {pipelines-title} 1.11, the `custom-task-version` feature flag has been removed.

* In {pipelines-title} 1.11, the `pipelinerun.status.taskRuns` and `pipelinerun.status.runs` fields have been removed along with the `embedded-status` feature flag. Use the `pipelinerun.status.childReferences` field instead.


[id="known-issues-1-11_{context}"]
== Known issues

* Setting the `prune-per-resource` boolean field does not delete `PipelineRun` or `TaskRun` resources if they were not part of any pipeline or task.

* Tekton CLI does not show logs of the `PipelineRun` resources that are created by using resolvers.

* When you filter your pipeline results based on the `order_by=created_time+desc&page_size=1` query, you get zero records without any `nextPageToken` value in the output.

* When you set the value of the `loglevel.pipelinesascode` field to `debug`, no debugging logs are generated in the {pac} controller pod. As a workaround, restart the {pac} controller pod.


[id="fixed-issues-1-11_{context}"]
== Fixed issues

* Before this update, {pac} failed to create a `PipelineRun` resource while detecting the `generateName` field in the `PipelineRun` CR. With this update, {pac} supports providing the `generateName` field in the `PipelineRun` CR.

* Before this update, when you created a `PipelineRun` resource from the web console, all annotations would be copied from the pipeline, causing issues for the running nodes. This update now resolves the issue.

* This update fixes the `tkn pr delete` command for the `keep` flag. Now, if the value of the `keep` flag is equal to the number of the associated task runs or pipeline runs, then the command returns the exit code `0` along with a message.

* Before this update, the Tekton Operator did not expose the performance configuration fields for any customizations. With this update, as a cluster administrator, you can customize the following performance configuration fields in the `TektonConfig` CR based on your needs:
** `disable-ha`
** `buckets`
** `kube-api-qps`
** `kube-api-burst`
** `threads-per-controller`

* This update fixes the remote bundle resolver to perform a case-insensitive comparison of the `kind` field with the `dev.tekton.image.kind` annotation value in the bundle.

* Before this update, pods for remote resolvers were terminated because of insufficient memory when you would clone a large Git repository. This update fixes the issue and increases the memory limit for deploying remote resolvers.

* With this update, task and pipeline resources of `v1` type are supported in remote resolution.

* This update reverts the removal of embedded `TaskRun` status from the API.  The embedded `TaskRun` status is now available as a deprecated feature to support compatibility with older versions of the client-server.

* Before this update, all annotations were merged into `PipelineRun` and `TaskRun` resources even if they were not required for the execution. With this update, when you merge annotations into `PipelineRun` and `TaskRun` resources, the `last-applied-configuration` annotation is skipped.

* This update fixes a regression issue and prevents the validation of a skipped task result in pipeline results. For example, if the pipeline result references a skipped `PipelineTask` resource, then the pipeline result is not emitted and the `PipelineRun` execution does not fail due to a missing result.

* This update uses the pod status message to determine the cause of a pod termination.

* Before this update, the default resolver was not set for the execution of the `finally` tasks. This update sets the default resolver for the `finally` tasks.

* With this update, {pipelines-title} avoids occasional failures of the `TaskRun` or `PipelineRun` execution when you use remote resolution.

* Before this update, a long pipeline run would be stuck in the running state on the cluster, even after the timeout. This update fixes the issue.

* This update fixes the `tkn pr delete` command for correctly using the `keep` flag. With this update, if the value of the `keep` flag equals the number of associated task runs or pipeline runs, the `tkn pr delete` command returns exit code `0` along with a message.

[id="release-notes-1-11-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.11.1

With this update, {pipelines-title} General Availability (GA) 1.11.1 is available on {product-title} 4.12 and later versions.

[id="fixed-issues-1-11-1_{context}"]
=== Fixed issues

* Before this update, a task run could fail with a mount path error message, when a running or pending pod was preempted. With this update, a task run does not fail when the cluster causes a pod to be deleted and re-created.

* Before this update, a shell script in a task had to be run as root. With this update, the shell script image has the non-root user ID set so that you can run a task that includes a shell script, such as the `git-clone` task, as a non-root user within the pod.

* Before this update, in {pipelines-title} 1.11.0, when a pipeline run is defined using {pac}, the definition in the Git repository references the `tekton.dev/v1beta1` API version and includes a `spec.pipelineRef.bundle` entry, the `kind` parameter for the bundle reference was wrongly set to `Task`. The issue did not exist in earlier versions of {pipelines-title}. With this update, the `kind` parameter is set correctly.

* Before this update, the `disable-ha` flag was not correctly passed to the `tekton-pipelines` controller, so the High Availability (HA) feature of {pipelines-title} could not be enabled. With this update, the `disable-ha` flag  is correctly passed and you can enable the HA feature as required.

* Before this update, you could not set the URL for {tekton-hub} and {artifact-hub} for the hub resolver, so you could use only the preset addresses of {tekton-hub} and {artifact-hub}. With this update, you can configure the URL for {tekton-hub} and {artifact-hub} for the hub resolver, for example, to use a custom {tekton-hub} instance that you installed.

* With this update, the SHA digest of the `git-init` image corresponds to version 1.10.5, which is the current released version of the image.

* Before this update, the `tekton-pipelines-controller` component used a config map named `config-leader-election`. This name is the default value for knative controllers, so the configuration process for {pipelines-shortname} could affect other controllers and vice versa. With this update, the component uses a unique config name, so the configuration process for {pipelines-shortname} does not affect other controllers and is not affected by other controllers.

* Before this update, when a user without write access to a GitHub repository opened a pull request, {pac} CI/CD actions would show as `skipped` in GitHub. With this update, {pac} CI/CD actions are shown as `Pending approval` in GitHub.

* Before this update, {pac} ran CI/CD actions for every pull request into a branch that matched a configured branch name. With this update, {pac} runs CI/CD actions only when the source branch of the pull request matches the exact configured branch name.

* Before this update, metrics for the {pac} controller were not visible in the {product-title} developer console. With this update, metrics for the {pac} controller are displayed in the developer console.

* Before this update, in {pipelines-title} 1.11.0, the Operator always installed {tekton-chains} and you could not disable installation of the {tekton-chains} component. With this update, you can set the value of the `disabled` parameter to `true` in the `TektonConfig` CR  to disable installation okindf {tekton-chains}.

* Before this update, if you configured {tekton-chains} on an older version of {pipelines-shortname} using the `TektonChain` CR and then upgraded to {pipelines-shortname} version 1.11.0, the configuration information was overwritten. With this update, if you upgrade from an older version of {pipelines-shortname} and {tekton-chains} was configured in the same namespace where the `TektonConfig` is installed (`openshift-pipelines`), {tekton-chains} configuration information is preserved.
