// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-operatorgroups.adoc

[id="olm-operatorgroups-static_{context}"]
= Static Operator groups

An Operator group is _static_ if its `spec.staticProvidedAPIs` field is set to `true`. As a result, OLM does not modify the `olm.providedAPIs` annotation of an Operator group, which means that it can be set in advance. This is useful when a user wants to use an Operator group to prevent resource contention in a set of namespaces but does not have active member CSVs that provide the APIs for those resources.

Below is an example of an Operator group that protects `Prometheus` resources in all namespaces with the `something.cool.io/cluster-monitoring: "true"` annotation:

[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-monitoring
  namespace: cluster-monitoring
  annotations:
    olm.providedAPIs: Alertmanager.v1.monitoring.coreos.com,Prometheus.v1.monitoring.coreos.com,PrometheusRule.v1.monitoring.coreos.com,ServiceMonitor.v1.monitoring.coreos.com
spec:
  staticProvidedAPIs: true
  selector:
    matchLabels:
      something.cool.io/cluster-monitoring: "true"
----
