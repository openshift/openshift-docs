// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

:_mod-docs-content-type: CONCEPT
[id="op-performance-tuning-using-tektonconfig-cr_{context}"]
= Performance tuning using TektonConfig CR

You can modify the fields under the `.spec.pipeline.performance` parameter in the `TektonConfig` custom resource (CR) to change high availability (HA) support and performance configuration for the {pipelines-shortname} controller.

.Example TektonConfig performance fields
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    performance:
      disable-ha: false
      buckets: 1
      threads-per-controller: 2
      kube-api-qps: 5.0
      kube-api-burst: 10
----

The fields are optional. If you set them, the {pipelines-title} Operator includes most of the fields as arguments in the `openshift-pipelines-controller` deployment under the `openshift-pipelines-controller` container. The {pipelines-shortname} Operator also updates the `buckets` field in the `config-leader-election` configuration map under the `openshift-pipelines` namespace.

If you do not specify the values, the {pipelines-shortname} Operator does not update those fields and applies the default values for the {pipelines-shortname} controller.

[NOTE]
====
If you modify or remove any of the performance fields, the {pipelines-shortname} Operator updates the `openshift-pipelines-controller` deployment and the `config-leader-election` configuration map (if the `buckets` field changed) and re-creates `openshift-pipelines-controller` pods.
====

.Modifiable fields for tuning {pipelines-shortname} performance
[options="header"]
|===

| Name | Description | Default value for the {pipelines-shortname} controller

| `disable-ha` | Enable or disable the high availability (HA) support. By default, the HA support is enabled. | `false`

| `buckets` | The number of buckets used to partition the key space for each reconciler.

Each of the replicas uses these buckets. The instance that owns a bucket reconciles the keys partitioned into that bucket. The maximum value is `10` | `1`

| `threads-per-controller` | The number of threads (workers) to use when the work queue of the {pipelines-shortname} controller is processed. | `2`

| `kube-api-qps` | The maximum queries per second (QPS) to the cluster master from the REST client. | `5.0`

| `kube-api-burst` | The maximum burst for a throttle. | `10`

|===

[NOTE]
====
The {pipelines-shortname} Operator does not control the number of replicas of the {pipelines-shortname} controller. The `replicas` setting of the deployment determines the number of replicas. For example, to change the number of replicas to 3, enter the following command:

[source,terminal]
----
$ oc --namespace openshift-pipelines scale deployment openshift-pipelines-controller --replicas=3
----
====

[IMPORTANT]
====
The `kube-api-qps` and `kube-api-burst` fields are multiplied by 2 in the {pipelines-shortname} controller. For example, if the `kube-api-qps` and `kube-api-burst` values are `10`, the actual QPS and burst values become `20`.
====


