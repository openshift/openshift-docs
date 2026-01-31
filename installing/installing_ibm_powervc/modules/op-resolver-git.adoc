// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-git-specify_{context}"]
= Specifying a remote pipeline or task using the Git resolver

When creating a pipeline run, you can specify a remote pipeline from a Git repository. When creating a pipeline or a task run, you can specify a remote task from a Git repository.

.Prerequisites

* If you want to use the authenticated SCM API, you must configure the authenticated Git connection for the Git resolver.

.Procedure

. To specify a remote pipeline or task from a Git repository, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: git
  params:
  - name: url
    value: <git_repository_url>
  - name: revision
    value: <branch_name>
  - name: pathInRepo
    value: <path_in_repository>
# ...
----
+
.Supported parameters for the Git resolver
|===
| Parameter | Description | Example value

| `url`
| The URL of the repository, when using anonymous cloning.
| `+https://github.com/tektoncd/catalog.git+`

| `repo`
| The repository name, when using the authenticated SCM API.
| `test-infra`

| `org`
| The organization for the repository, when using the authenticated SCM API.
| `tektoncd`

| `revision`
| The Git revision in the repository. You can specify a branch name, a tag  name, or a commit SHA hash.
| `aeb957601cf41c012be462827053a21a420befca` +
`main` +
`v0.38.2`

| `pathInRepo`
| The path name of the YAML file in the repository.
| `task/golang-build/0.3/golang-build.yaml`
|===
+
[NOTE]
====
To clone and fetch the repository anonymously, use the `url` parameter. To use the authenticated SCM API, use the `repo` parameter. Do not specify the `url` parameter and the `repo` parameter together.
====
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: git-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: git
    params:
    - name: url
      value: https://github.com/tektoncd/catalog.git
    - name: revision
      value: main
    - name: pathInRepo
      value: pipeline/simple/0.1/simple.yaml
    - name: sample-pipeline-parameter
      value: test
  params:
  - name: name
    value: "testPipelineRun"
----

The following example pipeline references a remote task from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-git-task-reference-demo
spec:
  tasks:
  - name: "git-task-reference-demo"
    taskRef:
      resolver: git
      params:
      - name: url
        value: https://github.com/tektoncd/catalog.git
      - name: revision
        value: main
      - name: pathInRepo
        value: task/git-clone/0.6/git-clone.yaml
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: git-task-reference-demo
spec:
  taskRef:
    resolver: git
    params:
    - name: url
      value: https://github.com/tektoncd/catalog.git
    - name: revision
      value: main
    - name: pathInRepo
      value: task/git-clone/0.6/git-clone.yaml
    - name: sample-task-parameter
      value: test
----
