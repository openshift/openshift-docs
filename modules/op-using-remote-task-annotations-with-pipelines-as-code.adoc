// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-remote-task-annotations-with-pipelines-as-code_{context}"]
= Using remote task annotations with {pac}

[role="_abstract"]
{pac} supports fetching remote tasks or pipelines by using annotations in a pipeline run. If you reference a remote task in a pipeline run, or a pipeline in a `PipelineRun` or a `PipelineSpec` object, the {pac} resolver automatically includes it. If there is any error while fetching the remote tasks or parsing them, {pac} stops processing the tasks.

To include remote tasks, refer to the following examples of annotation:

[discrete]
.Reference remote tasks in {tekton-hub}

* Reference a single remote task in {tekton-hub}.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "git-clone" <1>
...
----
<1> {pac} includes the latest version of the task from the {tekton-hub}.


* Reference multiple remote tasks from {tekton-hub}

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "[git-clone, golang-test, tkn]"
...
----

* Reference multiple remote tasks from {tekton-hub} using the `-<NUMBER>` suffix.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "git-clone"
  pipelinesascode.tekton.dev/task-1: "golang-test"
  pipelinesascode.tekton.dev/task-2: "tkn" <1>
...
----
<1> By default, {pac} interprets the string as the latest task to fetch from {tekton-hub}.


* Reference a specific version of a remote task from {tekton-hub}.

+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "[git-clone:0.1]" <1>
...
----
<1> Refers to the `0.1` version of the `git-clone` remote task from {tekton-hub}.


[discrete]
.Remote tasks using URLs

[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "<https://remote.url/task.yaml>" <1>
...
----
<1> The public URL to the remote task.
+
[NOTE]
====
* If you use GitHub and the remote task URL uses the same host as the `Repository` custom resource definition (CRD), {pac} uses the GitHub token and fetches the URL using the GitHub API.
+
For example, if you have a repository URL similar to `https://github.com/<organization>/<repository>` and the remote HTTP URL references a GitHub blob similar to `https://github.com/<organization>/<repository>/blob/<mainbranch>/<path>/<file>`, {pac} fetches the task definition files from that private repository with the GitHub App token.
+
When you work on a public GitHub repository, {pac} acts similarly for a GitHub raw URL such as `https://raw.githubusercontent.com/<organization>/<repository>/<mainbranch>/<path>/<file>`.


* GitHub App tokens are scoped to the owner or organization where the repository is located. When you use the GitHub webhook method, you can fetch any private or public repository on any organization where the personal token is allowed.
====

[discrete]
.Reference a task from a YAML file inside your repository

[source,yaml]
----
...
pipelinesascode.tekton.dev/task: "<share/tasks/git-clone.yaml>" <1>
...
----
<1> Relative path to the local file containing the task definition.
