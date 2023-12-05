// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-hub-specify_{context}"]
= Specifying a remote pipeline or task using the hub resolver

When creating a pipeline run, you can specify a remote pipeline from {artifact-hub} or {tekton-hub}. When creating a pipeline or a task run, you can specify a remote task from {artifact-hub} or {tekton-hub}.

.Procedure

* To specify a remote pipeline or task from {artifact-hub} or {tekton-hub}, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: hub
  params:
  - name: catalog
    value: <catalog>
  - name: type
    value: <catalog_type>
  - name: kind
    value: [pipeline|task]
  - name: name
    value: <resource_name>
  - name: version
    value: <resource_version>
# ...
----
+
.Supported parameters for the hub resolver
|===
| Parameter | Description | Example value

| `catalog`
| The catalog for pulling the resource.
| Default:  `tekton-catalog-tasks` (for the `task` kind);  `tekton-catalog-pipelines` (for the `pipeline` kind).

| `type`
| The type of the catalog for pulling the resource. Either `artifact` for {artifact-hub} or `tekton` for {tekton-hub}.
| Default:  `artifact`

| `kind`
| Either `task` or `pipeline`.
| Default: `task`

| `name`
| The name of the task or pipeline to fetch from the hub.
| `golang-build`

| `version`
| The version of the task or pipeline to fetch from the hub. You must use quotes (`"`) around the number.
| `"0.5.0"`
|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: hub-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: hub
    params:
    - name: catalog
      value: tekton-catalog-pipelines
    - name: type
      value: artifact
    - name: kind
      value: pipeline
    - name: name
      value: example-pipeline
    - name: version
      value: "0.1"
    - name: sample-pipeline-parameter
      value: test
----

The following example pipeline that references a remote task from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-cluster-task-reference-demo
spec:
  tasks:
  - name: "cluster-task-reference-demo"
    taskRef:
      resolver: hub
      params:
      - name: catalog
        value: tekton-catalog-tasks
      - name: type
        value: artifact
      - name: kind
        value: task
      - name: name
        value: example-task
      - name: version
        value: "0.6"
      - name: sample-task-parameter
        value: test
----

The following example task run that references a remote task from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: cluster-task-reference-demo
spec:
  taskRef:
    resolver: hub
    params:
    - name: catalog
      value: tekton-catalog-tasks
    - name: type
      value: artifact
    - name: kind
      value: task
    - name: name
      value: example-task
    - name: version
      value: "0.6"
    - name: sample-task-parameter
      value: test
----
