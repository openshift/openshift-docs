// Module included in the following assemblies:
//
// */openshift_pipelines/uninstalling-pipelines.adoc

:_mod-docs-content-type: CONCEPT
[id='op-understanding-pipelines-resource-consumption_{context}']
= Understanding resource consumption in pipelines

Each task consists of a number of required steps to be executed in a particular order defined in the `steps` field of the `Task` resource. Every task runs as a pod, and each step runs as a container within that pod.

Steps are executed one at a time. The pod that executes the task only requests enough resources to run a single container image (step) in the task at a time, and thus does not store resources for all the steps in the task.

The `Resources` field in the `steps` spec specifies the limits for resource consumption.
By default, the resource requests for the CPU, memory, and ephemeral storage are set to `BestEffort` (zero) values or to the minimums set through limit ranges in that project.

.Example configuration of resource requests and limits for a step
[source,yaml]
----
spec:
  steps:
  - name: <step_name>
    resources:
      requests:
        memory: 2Gi
        cpu: 600m
      limits:
        memory: 4Gi
        cpu: 900m
----

When the `LimitRange` parameter and the minimum values for container resource requests are specified in the project in which the pipeline and task runs are executed, {pipelines-title} looks at all the `LimitRange` values in the project and uses the minimum values instead of zero.

.Example configuration of limit range parameters at a project level
[source,yaml]
----
apiVersion: v1
kind: LimitRange
metadata:
  name: <limit_container_resource>
spec:
  limits:
  - max:
      cpu: "600m"
      memory: "2Gi"
    min:
      cpu: "200m"
      memory: "100Mi"
    default:
      cpu: "500m"
      memory: "800Mi"
    defaultRequest:
      cpu: "100m"
      memory: "100Mi"
    type: Container
...
----
