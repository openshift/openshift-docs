// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

:_mod-docs-content-type: PROCEDURE
[id="resolver-cluster-specify_{context}"]
= Specifying a remote pipeline or task using the cluster resolver

When creating a pipeline run, you can specify a remote pipeline from the same cluster. When creating a pipeline or a task run, you can specify a remote task from the same cluster.

.Procedure

* To specify a remote pipeline or task from the same cluster, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: cluster
  params:
  - name: name
    value: <name>
  - name: namespace
    value: <namespace>
  - name: kind
    value: [pipeline|task]
# ...
----
+
.Supported parameters for the cluster resolver
|===
| Parameter | Description | Example value

| `name`
| The name of the resource to fetch.
| `some-pipeline`

| `namespace`
| The namespace in the cluster containing the resource.
| `other-namespace`

| `kind`
| The kind of the resource to fetch.
| `pipeline`

|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from the same cluster:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: cluster-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: cluster
    params:
    - name: name
      value: some-pipeline
    - name: namespace
      value: test-namespace
    - name: kind
      value: pipeline
    - name: sample-pipeline-parameter
      value: test
----

The following example pipeline references a remote task from the same cluster:

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
      resolver: cluster
      params:
      - name: name
        value: some-task
      - name: namespace
        value: test-namespace
      - name: kind
        value: task
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from the same cluster:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: cluster-task-reference-demo
spec:
  taskRef:
    resolver: cluster
    params:
    - name: name
      value: some-task
    - name: namespace
      value: test-namespace
    - name: kind
      value: task
    - name: sample-task-parameter
      value: test
----
