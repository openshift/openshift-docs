// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="running-pipeline-run-using-pipelines-as-code_{context}"]
= Running a pipeline run using {pac}

[role="_abstract"]
With default configuration, {pac} runs any pipeline run in the `.tekton/` directory of the default branch of repository, when specified events such as pull request or push occurs on the repository. For example, if a pipeline run on the default branch has the annotation `pipelinesascode.tekton.dev/on-event: "[pull_request]"`, it will run whenever a pull request event occurs.

In the event of a pull request or a merge request, {pac} also runs pipelines from branches other than the default branch, if the following conditions are met by the author of the pull request:

* The author is the owner of the repository.
* The author is a collaborator on the repository.
* The author is a public member on the organization of the repository.
* The pull request author is listed in an `OWNER` file located in the repository root of the `main` branch as defined in the GitHub configuration for the repository. Also, the  pull request author is added to either `approvers` or `reviewers` section. For example, if an author is listed in the `approvers` section, then a pull request raised by that author starts the pipeline run.

[source,yaml]
----
...
  approvers:
    - approved
...
----

If the pull request author does not meet the requirements, another user who meets the requirements can comment `/ok-to-test` on the pull request, and start the pipeline run.

[discrete]
.Pipeline run execution
A pipeline run always runs in the namespace of the `Repository` custom resource definition (CRD) associated with the repository that generated the event.

You can observe the execution of your pipeline runs using the `tkn pac` CLI tool.

* To follow the execution of the last pipeline run, use the following example:
+
[source,terminal]
----
$ tkn pac logs -n <my-pipeline-ci> -L <1>
----
<1> `my-pipeline-ci` is the namespace for the `Repository` CRD.

* To follow the execution of any pipeline run interactively, use the following example:
+
[source,terminal]
----
$ tkn pac logs -n <my-pipeline-ci> <1>
----
<1> `my-pipeline-ci` is the namespace for the `Repository` CRD.
If you need to view a pipeline run other than the last one, you can use the `tkn pac logs` command to select a `PipelineRun` attached to the repository:

If you have configured {pac} with a GitHub App, {pac} posts a URL in the *Checks* tab of the GitHub App. You can click the URL and follow the pipeline execution.

[discrete]
.Restarting a pipeline run

You can restart a pipeline run with no events, such as sending a new commit to your branch or raising a pull request. On a GitHub App, go to the *Checks* tab and click *Re-run*.

If you target a pull or merge request, use the following comments inside your pull request to restart all or specific pipeline runs:

* The `/retest` comment restarts all pipeline runs.

* The `/retest <pipelinerun-name>` comment restarts a specific pipeline run.

* The `/cancel` comment cancels all pipeline runs.

* The `/cancel <pipelinerun-name>` comment cancels a specific pipeline run.

The results of the comments are visible under the *Checks* tab of a GitHub App.
