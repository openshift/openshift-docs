// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-0_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.0

[id="new-features-1-0_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.0 is now available on {product-title} 4.4. {pipelines-title} TP 1.0 is updated to support:

* Tekton Pipelines 0.11.3
* Tekton `tkn` CLI 0.9.0
* Tekton Triggers 0.4.0
* cluster tasks based on Tekton Catalog 0.11

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.0.

[id="pipeline-new-features-1-0_{context}"]
=== Pipelines
* Support for  v1beta1 API Version.
* Support for an improved limit range. Previously, limit range was specified exclusively for the task run and the pipeline run. Now there is no need to explicitly specify the limit range. The minimum limit range across the namespace is used.
* Support for sharing data between tasks using task results and task params.
* Pipelines can now be configured to not overwrite the `HOME` environment variable and the working directory of steps.
* Similar to task steps, `sidecars` now support script mode.
* You can now specify a different scheduler name in task run `podTemplate` resource.
* Support for variable substitution using Star Array Notation.
* Tekton controller can now be configured to monitor an individual namespace.
* A new description field is now added to the specification of pipelines, tasks, cluster tasks, resources, and conditions.
* Addition of proxy parameters to Git pipeline resources.

[id="cli-new-features-1-0_{context}"]
=== Pipelines CLI

* The `describe` subcommand is now added for the following `tkn` resources: `EventListener`, `Condition`, `TriggerTemplate`, `ClusterTask`, and `TriggerSBinding`.
* Support added for `v1beta1` to the following resources along with backward compatibility for `v1alpha1`: `ClusterTask`, `Task`, `Pipeline`, `PipelineRun`,  and `TaskRun`.
* The following commands can now list output from all namespaces using the `--all-namespaces` flag option: `tkn task list`, `tkn pipeline list`, `tkn taskrun list`, `tkn pipelinerun list`
+
The output of these commands is also enhanced to display information without headers using the `--no-headers` flag option.

* You can now start a pipeline using default parameter values by specifying `--use-param-defaults` flag in the `tkn pipelines start` command.
* Support for workspace is now added to `tkn pipeline start` and `tkn task start` commands.
* A new `clustertriggerbinding` command is now added with the following subcommands: `describe`, `delete`, and `list`.
* You can now directly start a pipeline run using a local or remote `yaml` file.
* The `describe` subcommand now displays an enhanced and detailed output. With the addition of new fields,  such as `description`, `timeout`, `param description`, and `sidecar status`, the command output now provides more detailed information about a specific `tkn` resource.
* The `tkn task log` command now displays logs directly if only one task is present in the namespace.

[id="triggers-new-features-1-0_{context}"]
=== Triggers
* Triggers can now create both `v1alpha1` and `v1beta1` pipeline resources.
* Support for new Common Expression Language (CEL) interceptor function - `compareSecret`. This function securely compares strings to secrets in CEL expressions.
* Support for authentication and authorization at the event listener trigger  level.


[id="deprecated-features-1-0_{context}"]
== Deprecated features
The following items are deprecated in this release:

* The environment variable `$HOME`, and variable `workingDir` in the `Steps` specification are deprecated and might be changed in a future release. Currently in a `Step` container, the `HOME` and  `workingDir` variables are overwritten to `/tekton/home` and `/workspace` variables, respectively.
+
In a later release, these two fields will not be modified, and will be set to values defined in the container image and the `Task` YAML.
For this release, use the `disable-home-env-overwrite` and `disable-working-directory-overwrite` flags to disable overwriting of the `HOME` and `workingDir` variables.

* The following commands are deprecated and might be removed in the future release: `tkn pipeline create`, `tkn task create`.

* The `-f` flag with the `tkn resource create` command is now deprecated. It might be removed in the future release.

* The `-t` flag and the `--timeout` flag (with seconds format) for the `tkn clustertask create` command are now deprecated. Only duration timeout format is now supported, for example `1h30s`. These deprecated flags might be removed in the future release.

[id="known-issues-1-4-0_{context}"]
== Known issues
* If you are upgrading from an older version of {pipelines-title}, you must delete your existing deployments before upgrading to {pipelines-title} version 1.0. To delete an existing deployment, you must first delete Custom Resources and then uninstall the {pipelines-title} Operator. For more details, see the uninstalling {pipelines-title} section.
* Submitting the same `v1alpha1` tasks more than once results in an error. Use the `oc replace` command instead of `oc apply` when re-submitting a `v1alpha1` task.
* The `buildah` cluster task does not work when a new user is added to a container.
+
When the Operator is installed, the `--storage-driver` flag for the `buildah` cluster task is not specified, therefore the flag is set to its default value. In some cases, this causes the storage driver to be set incorrectly. When a new user is added, the incorrect storage-driver results in the failure of the `buildah` cluster task with the following error:
+
----
useradd: /etc/passwd.8: lock file already used
useradd: cannot lock /etc/passwd; try again later.
----
+
As a workaround, manually set the `--storage-driver` flag value to `overlay` in the `buildah-task.yaml` file:
+
. Login to your cluster as a `cluster-admin`:
+
----
$ oc login -u <login> -p <password> https://openshift.example.com:6443
----
. Use the `oc edit` command to edit `buildah` cluster task:
+
----
$ oc edit clustertask buildah
----
+
The current version of the `buildah` clustertask YAML file opens in the editor set by your `EDITOR` environment variable.
. Under the `Steps` field, locate the following `command` field:
+
----
 command: ['buildah', 'bud', '--format=$(params.FORMAT)', '--tls-verify=$(params.TLSVERIFY)', '--layers', '-f', '$(params.DOCKERFILE)', '-t', '$(resources.outputs.image.url)', '$(params.CONTEXT)']
----

. Replace the `command` field with the following:
+
----
 command: ['buildah', '--storage-driver=overlay', 'bud', '--format=$(params.FORMAT)', '--tls-verify=$(params.TLSVERIFY)', '--no-cache', '-f', '$(params.DOCKERFILE)', '-t', '$(params.IMAGE)', '$(params.CONTEXT)']
----
. Save the file and exit.


+
Alternatively, you can also modify the `buildah` cluster task YAML file directly on the web console by navigating to *Pipelines* -> *Cluster Tasks* -> *buildah*. Select *Edit Cluster Task* from the *Actions* menu and replace the `command` field as shown in the previous procedure.

[id="fixed-issues-1-0_{context}"]
== Fixed issues
* Previously, the `DeploymentConfig` task triggered a new deployment build even when an image build was already in progress. This caused the deployment of the pipeline to fail. With this fix, the `deploy task` command  is now replaced with the `oc rollout status` command which waits for the in-progress deployment to finish.
* Support for `APP_NAME` parameter is now added in pipeline templates.
* Previously, the pipeline template for Java S2I failed to look up the image in the registry. With this fix, the image is looked up using the existing image pipeline resources instead of the user provided `IMAGE_NAME` parameter.
* All the {pipelines-shortname} images are now based on the Red Hat Universal Base Images (UBI).
* Previously, when the pipeline was installed in a namespace other than `tekton-pipelines`, the `tkn version` command displayed the pipeline version as `unknown`. With this fix, the `tkn version` command now displays the correct pipeline version in any namespace.
* The `-c` flag is no longer supported for the `tkn version` command.
* Non-admin users can now list the cluster trigger bindings.
* The event listener `CompareSecret` function is now fixed for the CEL Interceptor.
* The `list`, `describe`, and `start` subcommands for tasks and cluster tasks now correctly display the output in case a task and cluster task have the same name.
* Previously, the {pipelines-shortname} Operator modified the privileged security context constraints (SCCs), which caused an error during cluster upgrade. This error is now fixed.
* In the `tekton-pipelines` namespace, the timeouts of all task runs and pipeline runs are now set to the value of `default-timeout-minutes` field using the config map.
* Previously, the pipelines section in the web console was not displayed for non-admin users. This issue is now resolved.
