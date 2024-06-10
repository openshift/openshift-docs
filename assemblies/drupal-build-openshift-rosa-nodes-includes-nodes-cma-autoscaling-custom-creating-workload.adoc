// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-adding.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cma-autoscaling-custom-creating-workload_{context}"]
= Adding a custom metrics autoscaler to a workload

You can create a custom metrics autoscaler for a workload that is created by a `Deployment`, `StatefulSet`, or `custom resource` object.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

* If you use a custom metrics autoscaler for scaling based on CPU or memory:

** Your cluster administrator must have properly configured cluster metrics. You can use the `oc describe PodMetrics <pod-name>` command to determine if metrics are configured. If metrics are configured, the output appears similar to the following, with CPU and Memory displayed under Usage.
+
[source,terminal]
----
$ oc describe PodMetrics openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
----
+
.Example output
[source,yaml,options="nowrap"]
----
Name:         openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
Namespace:    openshift-kube-scheduler
Labels:       <none>
Annotations:  <none>
API Version:  metrics.k8s.io/v1beta1
Containers:
  Name:  wait-for-host-port
  Usage:
    Memory:  0
  Name:      scheduler
  Usage:
    Cpu:     8m
    Memory:  45440Ki
Kind:        PodMetrics
Metadata:
  Creation Timestamp:  2019-05-23T18:47:56Z
  Self Link:           /apis/metrics.k8s.io/v1beta1/namespaces/openshift-kube-scheduler/pods/openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
Timestamp:             2019-05-23T18:47:56Z
Window:                1m0s
Events:                <none>
----

** The pods associated with the object you want to scale must include specified memory and CPU limits. For example:
+
.Example pod spec
[source,yaml]
----
apiVersion: v1
kind: Pod
# ...
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
# ...
----

.Procedure

. Create a YAML file similar to the following. Only the name `<2>`, object name `<4>`, and object kind `<5>` are required:
+
.Example scaled object
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "0" <1>
  name: scaledobject <2>
  namespace: my-namespace
spec:
  scaleTargetRef:
    apiVersion: apps/v1 <3>
    name: example-deployment <4>
    kind: Deployment <5>
    envSourceContainerName: .spec.template.spec.containers[0] <6>
  cooldownPeriod:  200 <7>
  maxReplicaCount: 100 <8>
  minReplicaCount: 0 <9>
  metricsServer: <10>
    auditConfig:
      logFormat: "json"
      logOutputVolumeClaim: "persistentVolumeClaimName"
      policy:
        rules:
        - level: Metadata
        omitStages: "RequestReceived"
        omitManagedFields: false
      lifetime:
        maxAge: "2"
        maxBackup: "1"
        maxSize: "50"
  fallback: <11>
    failureThreshold: 3
    replicas: 6
  pollingInterval: 30 <12>
  advanced:
    restoreToOriginalReplicaCount: false <13>
    horizontalPodAutoscalerConfig:
      name: keda-hpa-scale-down <14>
      behavior: <15>
        scaleDown:
          stabilizationWindowSeconds: 300
          policies:
          - type: Percent
            value: 100
            periodSeconds: 15
  triggers:
  - type: prometheus <16>
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: basic
    authenticationRef: <17>
      name: prom-triggerauthentication
      kind: TriggerAuthentication
----
<1> Optional: Specifies that the Custom Metrics Autoscaler Operator is to scale the replicas to the specified value and stop autoscaling, as described in the "Pausing the custom metrics autoscaler for a workload" section.
<2> Specifies a name for this custom metrics autoscaler.
<3> Optional: Specifies the API version of the target resource. The default is `apps/v1`.
<4> Specifies the name of the object that you want to scale.
<5> Specifies the `kind` as `Deployment`, `StatefulSet` or `CustomResource`.
<6> Optional: Specifies the name of the container in the target resource, from which the custom metrics autoscaler gets environment variables holding secrets and so forth. The default is `.spec.template.spec.containers[0]`.
<7> Optional. Specifies the period in seconds to wait after the last trigger is reported before scaling the deployment back to `0` if the `minReplicaCount` is set to `0`. The default is `300`.
<8> Optional: Specifies the maximum number of replicas when scaling up. The default is `100`.
<9> Optional: Specifies the minimum number of replicas when scaling down.
<10> Optional: Specifies the parameters for audit logs. as described in the "Configuring audit logging" section.
<11> Optional: Specifies the number of replicas to fall back to if a scaler fails to get metrics from the source for the number of times defined by the `failureThreshold` parameter. For more information on fallback behavior, see the link:https://keda.sh/docs/2.7/concepts/scaling-deployments/#fallback[KEDA documentation].
<12> Optional: Specifies the interval in seconds to check each trigger on. The default is `30`.
<13> Optional: Specifies whether to scale back the target resource to the original replica count after the scaled object is deleted. The default is `false`, which keeps the replica count as it is when the scaled object is deleted.
<14> Optional: Specifies a name for the horizontal pod autoscaler. The default is `keda-hpa-{scaled-object-name}`.
<15> Optional: Specifies a scaling policy to use to control the rate to scale pods up or down, as described in the "Scaling policies" section.
<16> Specifies the trigger to use as the basis for scaling, as described in the "Understanding the custom metrics autoscaler triggers" section. This example uses {product-title} monitoring.
<17> Optional: Specifies a trigger authentication or a cluster trigger authentication. For more information, see _Understanding the custom metrics autoscaler trigger authentication_ in the _Additional resources_ section.
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
$ oc get scaledobject <scaled_object_name>
----
+
.Example output
[source,terminal]
----
NAME            SCALETARGETKIND      SCALETARGETNAME        MIN   MAX   TRIGGERS     AUTHENTICATION               READY   ACTIVE   FALLBACK   AGE
scaledobject    apps/v1.Deployment   example-deployment     0     50    prometheus   prom-triggerauthentication   True    True     True       17s
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
* `FALLBACK`: Indicates whether the custom metrics autoscaler is able to get metrics from the source
** If `False`, the custom metrics autoscaler is getting metrics.
** If `True`, the custom metrics autoscaler is getting metrics because there are no metrics or there is a problem in one or more of the objects you created.
--

