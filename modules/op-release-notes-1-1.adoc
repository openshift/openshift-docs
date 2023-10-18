// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-1_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.1

[id="new-features-1-1_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.1 is now available on {product-title} 4.5. {pipelines-title} TP 1.1 is updated to support:

* Tekton Pipelines 0.14.3
* Tekton `tkn` CLI 0.11.0
* Tekton Triggers 0.6.1
* cluster tasks based on Tekton Catalog 0.14

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.1.

[id="pipeline-new-features-1-1_{context}"]
=== Pipelines

* Workspaces can now be used instead of pipeline resources. It is recommended that you use workspaces in {pipelines-shortname}, as pipeline resources are difficult to debug, limited in scope, and make tasks less reusable. For more details on workspaces, see the Understanding {pipelines-shortname} section.
* Workspace support for volume claim templates has been added:
** The volume claim template for a pipeline run and task run can now be added as a volume source for workspaces. The tekton-controller then creates a persistent volume claim (PVC) using the template that is seen as a PVC for all task runs in the pipeline. Thus you do not need to define the PVC configuration every time it binds a workspace that spans multiple tasks.
** Support to find the name of the PVC when a volume claim template is used as a volume source is now available using variable substitution.
* Support for improving audits:
** The `PipelineRun.Status` field now contains the status of every task run in the pipeline and the pipeline specification used to instantiate a pipeline run to monitor the progress of the pipeline run.
** Pipeline results have been added to the pipeline specification and `PipelineRun` status.
** The `TaskRun.Status` field now contains the exact task specification used to instantiate the `TaskRun` resource.
* Support to apply the default parameter to conditions.
* A task run created by referencing a cluster task now adds the `tekton.dev/clusterTask` label instead of the `tekton.dev/task` label.
* The kube config writer now adds the `ClientKeyData` and the `ClientCertificateData` configurations in the resource structure to enable replacement of the pipeline resource type cluster with the kubeconfig-creator task.
* The names of the `feature-flags` and the `config-defaults` config maps are now customizable.
* Support for the host network in the pod template used by the task run is now available.
* An Affinity Assistant is now available to support node affinity in task runs that share workspace volume. By default, this is disabled on {pipelines-shortname}.
* The pod template has been updated to specify `imagePullSecrets` to identify secrets that the container runtime should use to authorize container image pulls when starting a pod.
* Support for emitting warning events from the task run controller if the controller fails to update the task run.
* Standard or recommended k8s labels have been added to all resources to identify resources belonging to an application or component.
* The `Entrypoint` process is now notified for signals and these signals are then propagated using a dedicated PID Group of the `Entrypoint` process.
* The pod template can now be set on a task level at runtime using task run specs.
* Support for emitting Kubernetes events:
** The controller now emits events for additional task run lifecycle events - `taskrun started` and `taskrun running`.
** The pipeline run controller now emits an event every time a pipeline starts.
* In addition to the default Kubernetes events, support for cloud events for task runs is now available. The controller can be configured to send any task run events, such as create, started, and failed, as cloud events.
* Support for using the `$context.<task|taskRun|pipeline|pipelineRun>.name` variable to reference the appropriate name when in pipeline runs and task runs.
* Validation for pipeline run parameters is now available to ensure that all the parameters required by the pipeline are provided by the pipeline run. This also allows pipeline runs to provide extra parameters in addition to the required parameters.
* You can now specify tasks within a pipeline that will always execute before the pipeline exits, either after finishing all tasks successfully or after a task in the pipeline failed, using the `finally` field in the pipeline YAML file.
* The `git-clone` cluster task is now available.

[id="cli-new-features-1-1_{context}"]
=== Pipelines CLI

* Support for embedded trigger binding is now available to the `tkn evenlistener describe` command.
* Support to recommend subcommands and make suggestions if an incorrect subcommand is used.
* The `tkn task describe` command now auto selects the task if only one task is present in the pipeline.
* You can now start a task using default parameter values by specifying the `--use-param-defaults` flag in the `tkn task start` command.
* You can now specify a volume claim template for pipeline runs or task runs using the `--workspace` option with the  `tkn pipeline start` or  `tkn task start` commands.
* The `tkn pipelinerun logs` command now displays logs for the final tasks listed in the `finally` section.
* Interactive mode support has now been provided to the `tkn task start` command and the `describe` subcommand for the following `tkn` resources:  `pipeline`, `pipelinerun`, `task`, `taskrun`, `clustertask`, and `pipelineresource`.
* The `tkn version` command now displays the version of the triggers installed in the cluster.
* The `tkn pipeline describe` command now displays parameter values and timeouts specified for tasks used in the pipeline.
* Support added for the `--last` option for the `tkn pipelinerun describe` and the `tkn taskrun describe` commands to describe the most recent pipeline run or task run, respectively.
* The `tkn pipeline describe` command now displays the conditions applicable to the tasks in the pipeline.
* You can now use the `--no-headers` and `--all-namespaces` flags with the `tkn resource list` command.

[id="triggers-new-features-1-1_{context}"]
=== Triggers
* The following Common Expression Language (CEL) functions are now available:
** `parseURL`  to parse and extract portions of a URL
** `parseJSON` to parse JSON value types embedded in a string in the `payload` field of the `deployment` webhook
* A new interceptor for webhooks from Bitbucket has been added.
* Event listeners now display the `Address URL` and the `Available status` as additional fields when listed with the `kubectl get` command.
* trigger template params now use the `$(tt.params.<paramName>)` syntax instead of `$(params.<paramName>)` to reduce the confusion between trigger template and resource templates params.
* You can now add `tolerations` in the `EventListener` CRD to ensure that event listeners are deployed with the same configuration even if all nodes are tainted due to security or management issues.
* You can now add a Readiness Probe for event listener Deployment at `URL/live`.
* Support for embedding `TriggerBinding` specifications in event listener triggers is now added.
* Trigger resources are now annotated with the recommended `app.kubernetes.io` labels.


[id="deprecated-features-1-1_{context}"]
== Deprecated features
The following items are deprecated in this release:

* The `--namespace` or `-n` flags for all cluster-wide commands, including the `clustertask` and `clustertriggerbinding` commands, are deprecated. It will be removed in a future release.
* The `name` field in `triggers.bindings` within an event listener has been deprecated in favor of the `ref` field and will be removed in a future release.
* Variable interpolation in trigger templates using `$(params)` has been deprecated in favor of using `$(tt.params)` to reduce confusion with the pipeline variable interpolation syntax. The `$(params.<paramName>)` syntax will be removed in a future release.
* The `tekton.dev/task` label is deprecated on cluster tasks.
* The `TaskRun.Status.ResourceResults.ResourceRef` field is deprecated and will be removed.
* The `tkn pipeline create`, `tkn task create`, and `tkn resource create -f` subcommands have been removed.
* Namespace validation has been removed from `tkn` commands.
* The default timeout of `1h` and the  `-t` flag for the `tkn ct start` command have been removed.
* The `s2i` cluster task has been deprecated.


[id="known-issues-1-1_{context}"]
== Known issues
* Conditions do not support workspaces.
* The `--workspace` option and the interactive mode is not supported for the `tkn clustertask start` command.
* Support of backward compatibility for `$(params.<paramName>)` syntax forces you to use trigger templates with pipeline specific params as the trigger s webhook is unable to differentiate trigger  params from pipelines params.
* Pipeline metrics report incorrect values when you run a  promQL query for `tekton_taskrun_count`  and `tekton_taskrun_duration_seconds_count`.
* pipeline runs and task runs continue to be in the `Running` and `Running(Pending)` states respectively even when a non existing PVC name is given to a workspace.

[id="fixed-issues-1-1_{context}"]
== Fixed issues
* Previously, the `tkn task delete <name> --trs` command would delete both the task and cluster task if the name of the task and cluster task were the same. With this fix, the command deletes only the task runs that are created by the task `<name>`.
* Previously the  `tkn pr delete -p <name> --keep 2` command would disregard the `-p` flag when used with the `--keep` flag and would delete all the pipeline runs except the latest two. With this fix, the command deletes only the pipeline runs that are created by the pipeline `<name>`, except for the latest two.
* The `tkn triggertemplate describe` output now displays resource templates in a table format instead of YAML format.
* Previously the `buildah` cluster task failed when a new user was added to a container. With this fix, the issue has been resolved.
