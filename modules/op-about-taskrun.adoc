// Ths module is included in the following assembly:
//
// *openshift_pipelines/op-creating-applications-with-cicd-pipelines.adoc

[id="about-taskrun_{context}"]
= TaskRun

A `TaskRun` instantiates a task for execution with specific inputs, outputs, and execution parameters on a cluster. It can be invoked on its own or as part of a pipeline run for each task in a pipeline.

A task consists of one or more steps that execute container images, and each container image performs a specific piece of build work. A task run executes the steps in a task in the specified order, until all steps execute successfully or a failure occurs. A `TaskRun` is automatically created by a `PipelineRun` for each task in a pipeline.

The following example shows a task run that runs the `apply-manifests` task with the relevant input parameters:
[source,yaml]
----
apiVersion: tekton.dev/v1beta1 <1>
kind: TaskRun <2>
metadata:
  name: apply-manifests-taskrun <3>
spec: <4>
  serviceAccountName: pipeline
  taskRef: <5>
    kind: Task
    name: apply-manifests
  workspaces: <6>
  - name: source
    persistentVolumeClaim:
      claimName: source-pvc
----
<1> The task run API version `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `TaskRun`.
<3> Unique name to identify this task run.
<4> Definition of the task run. For this task run, the task and the required workspace are specified.
<5> Name of the task reference used for this task run. This task run executes the `apply-manifests` task.
<6> Workspace used by the task run.
