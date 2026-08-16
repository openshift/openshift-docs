// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-bundles-specify_{context}"]
= Specifying a remote pipeline or task using the bundles resolver

When creating a pipeline run, you can specify a remote pipeline from a Tekton bundle. When creating a pipeline or a task run, you can specify a remote task from a Tekton bundle.

.Procedure

* To specify a remote pipeline or task from a Tekton bundle, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: bundles
  params:
  - name: bundle
    value: <fully_qualified_image_name>
  - name: name
    value: <resource_name>
  - name: kind
    value: [pipeline|task]
# ...
----
+
.Supported parameters for the bundles resolver
|===
| Parameter | Description | Example value

| `serviceAccount`
| The name of the service account to use when constructing registry credentials.
| `default`

| `bundle`
| The bundle URL pointing at the image to fetch.
| `gcr.io/tekton-releases/catalog/upstream/golang-build:0.1`

| `name`
| The name of the resource to pull out of the bundle.
| `golang-build`

| `kind`
| The kind of the resource to pull out of the bundle.
| `task`
|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: bundle-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: bundles
    params:
    - name: bundle
      value: registry.example.com:5000/simple/pipeline:latest
    - name: name
      value: hello-pipeline
    - name: kind
      value: pipeline
    - name: sample-pipeline-parameter
      value: test
  params:
  - name: username
    value: "pipelines"
----

The following example pipeline references a remote task from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-bundle-task-reference-demo
spec:
  tasks:
  - name: "bundle-task-demo"
    taskRef:
      resolver: bundles
      params:
      - name: bundle
        value: registry.example.com:5000/advanced/task:latest
      - name: name
        value: hello-world
      - name: kind
        value: task
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: bundle-task-reference-demo
spec:
  taskRef:
    resolver: bundles
    params:
    - name: bundle
      value: registry.example.com:5000/simple/new_task:latest
    - name: name
      value: hello-world
    - name: kind
      value: task
    - name: sample-task-parameter
      value: test
----
