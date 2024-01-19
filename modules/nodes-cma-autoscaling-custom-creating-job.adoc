// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-adding.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-creating-job_{context}"]
= Adding a custom metrics autoscaler to a job

You can create a custom metrics autoscaler for any `Job` object.

:FeatureName: Scaling by using a scaled job
include::snippets/technology-preview.adoc[]

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

.Procedure

. Create a YAML file similar to the following:
+
[source,yaml,options="nowrap"]
----
kind: ScaledJob
apiVersion: keda.sh/v1alpha1
metadata:
  name: scaledjob
  namespace: my-namespace
spec:
  failedJobsHistoryLimit: 5
  jobTargetRef:
    activeDeadlineSeconds: 600 <1>
    backoffLimit: 6 <2>
    parallelism: 1 <3>
    completions: 1 <4>
    template:  <5>
      metadata:
        name: pi
      spec:
        containers:
        - name: pi
          image: perl
          command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
  maxReplicaCount: 100 <6>
  pollingInterval: 30 <7>
  successfulJobsHistoryLimit: 5 <8>
  failedJobsHistoryLimit: 5 <9>
  envSourceContainerName: <10>
  rolloutStrategy: gradual <11>
  scalingStrategy: <12>
    strategy: "custom"
    customScalingQueueLengthDeduction: 1
    customScalingRunningJobPercentage: "0.5"
    pendingPodConditions:
      - "Ready"
      - "PodScheduled"
      - "AnyOtherCustomPodCondition"
    multipleScalersCalculation : "max"
  triggers:
  - type: prometheus <13>
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "bearer"
    authenticationRef: <14>
      name: prom-cluster-triggerauthentication
----
<1> Specifies the maximum duration the job can run.
<2> Specifies the number of retries for a job. The default is `6`.
<3> Optional: Specifies how many pod replicas a job should run in parallel; defaults to `1`.
* For non-parallel jobs, leave unset. When unset, the default is `1`.
<4> Optional: Specifies how many successful pod completions are needed to mark a job completed.
* For non-parallel jobs, leave unset. When unset,  the default is `1`.
* For parallel jobs with a fixed completion count, specify the number of completions.
* For parallel jobs with a work queue, leave unset. When unset the default is the value of the `parallelism` parameter.
<5> Specifies the template for the pod the controller creates.
<6> Optional: Specifies the maximum number of replicas when scaling up. The default is `100`.
<7> Optional: Specifies the interval in seconds to check each trigger on. The default is `30`.
<8> Optional: Specifies the number of successful finished jobs should be kept. The default is `100`.
<9> Optional: Specifies how many failed jobs should be kept. The default is `100`.
<10> Optional: Specifies the name of the container in the target resource, from which the custom autoscaler gets environment variables holding secrets and so forth. The default is `.spec.template.spec.containers[0]`.
<11> Optional: Specifies whether existing jobs are terminated whenever a scaled job is being updated:
+
--
* `default`: The autoscaler terminates an existing job if its associated scaled job is updated. The autoscaler recreates the job with the latest specs.
* `gradual`: The autoscaler does not terminate an existing job if its associated scaled job is updated. The autoscaler creates new jobs with the latest specs.
--
+
<12> Optional: Specifies a scaling strategy: `default`, `custom`, or `accurate`. The default is `default`. For more information, see the link in the "Additional resources" section that follows.
<13> Specifies the trigger to use as the basis for scaling, as described in the "Understanding the custom metrics autoscaler triggers" section.
<14> Optional: Specifies a trigger authentication or a cluster trigger authentication. For more information, see _Understanding the custom metrics autoscaler trigger authentication_ in the _Additional resources_ section.
* Enter `TriggerAuthentication` to use a trigger authentication. This is the default.
* Enter `ClusterTriggerAuthentication` to use a cluster trigger authentication.

. Create the custom metrics autoscaler by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

.Verification

* View the command output to verify that the custom metrics autoscaler was created:
+
[source,terminal]
----
$ oc get scaledjob <scaled_job_name>
----
+
.Example output
[source,terminal]
----
NAME        MAX   TRIGGERS     AUTHENTICATION              READY   ACTIVE    AGE
scaledjob   100   prometheus   prom-triggerauthentication  True    True      8s
----
+
Note the following fields in the output:
+
--
* `TRIGGERS`: Indicates the trigger, or scaler, that is being used.
* `AUTHENTICATION`: Indicates the name of any trigger authentication being used.
* `READY`: Indicates whether the scaled object is ready to start scaling:
** If `True`, the scaled object is ready.
** If `False`, the scaled object is not ready because of a problem in one or more of the objects you created.
* `ACTIVE`: Indicates whether scaling is taking place:
** If `True`, scaling is taking place.
** If `False`, scaling is not taking place because there are no metrics or there is a problem in one or more of the objects you created.
--
