// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="monitoring-pipeline-run-status-using-pipelines-as-code_{context}"]
= Monitoring pipeline run status using {pac}

[role="_abstract"]
Depending on the context and supported tools, you can monitor the status of a pipeline run in different ways.

[discrete]
.Status on GitHub Apps
When a pipeline run finishes, the status is added in the *Check* tabs with limited information on how long each task of your pipeline took, and the output of the `tkn pipelinerun describe` command.

[discrete]
.Log error snippet
When {pac} detects an error in one of the tasks of a pipeline, a small snippet consisting of the last 3 lines in the task breakdown of the first failed task is displayed.

[NOTE]
====
{pac} avoids leaking secrets by looking into the pipeline run and replacing secret values with hidden characters. However, {pac} cannot hide secrets coming from workspaces and envFrom source.
====

[discrete]
.Annotations for log error snippets

In the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec, you can set the `error-detection-from-container-logs` parameter to `true`. In this case, {pac} detects the errors from the container logs and adds them as annotations on the pull request where the error occurred.

:FeatureName: Adding annotations for log error snippets
include::snippets/technology-preview.adoc[]

Currently, {pac} supports only the simple cases where the error looks like `makefile` or `grep` output of the following format:
[source,yaml]
----
<filename>:<line>:<column>: <error message>
----

You can customize the regular expression used to detect the errors with the `error-detection-simple-regexp` parameter. The regular expression uses named groups to give flexibility on how to specify the matching. The groups needed to match are `filename`, `line`, and `error`. You can view the {pac} config map for the default regular expression.

[NOTE]
====
By default, {pac} scans only the last 50 lines of the container logs. You can increase this value in the `error-detection-max-number-of-lines` field or set `-1` for an unlimited number of lines. However, such configurations may increase the memory usage of the watcher.
====

[discrete]
.Status for webhook
For webhook, when the event is a pull request, the status is added as a comment on the pull or merge request.

[discrete]
.Failures
If a namespace is matched to a `Repository` custom resource definition (CRD), {pac} emits its failure log messages in the Kubernetes events inside the namespace.

[discrete]
.Status associated with Repository CRD
The last 5 status messages for a pipeline run is stored inside the `Repository` custom resource.

[source,terminal]
----
$ oc get repo -n <pipelines-as-code-ci>
----

[source,terminal]
----
NAME                  URL                                                        NAMESPACE             SUCCEEDED   REASON      STARTTIME   COMPLETIONTIME
pipelines-as-code-ci   https://github.com/openshift-pipelines/pipelines-as-code   pipelines-as-code-ci   True        Succeeded   59m         56m
----

Using the `tkn pac describe` command, you can extract the status of the runs associated with your repository and its metadata.

[discrete]
.Notifications
{pac} does not manage notifications. If you need to have notifications, use the `finally` feature of pipelines.
