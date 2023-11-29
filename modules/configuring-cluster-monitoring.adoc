// Module included in the following assemblies:
//
// * scalability_and_performance/recommended-performance-scale-practices/recommended-infrastructure-practices.adoc

:_mod-docs-content-type: PROCEDURE
[id="configuring-cluster-monitoring_{context}"]
= Configuring cluster monitoring

[role="_abstract"]
You can increase the storage capacity for the Prometheus component in the cluster monitoring stack.

.Procedure

To increase the storage capacity for Prometheus:

. Create a YAML configuration file, `cluster-monitoring-config.yaml`. For example:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
data:
  config.yaml: |
    prometheusK8s:
      retention: {{PROMETHEUS_RETENTION_PERIOD}} <1>
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      volumeClaimTemplate:
        spec:
          storageClassName: {{STORAGE_CLASS}} <2>
          resources:
            requests:
              storage: {{PROMETHEUS_STORAGE_SIZE}} <3>
    alertmanagerMain:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      volumeClaimTemplate:
        spec:
          storageClassName: {{STORAGE_CLASS}} <2>
          resources:
            requests:
              storage: {{ALERTMANAGER_STORAGE_SIZE}} <4>
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
----
<1> The default value of Prometheus retention is `PROMETHEUS_RETENTION_PERIOD=15d`. Units are measured in time using one of these suffixes: s, m, h, d.
<2> The storage class for your cluster.
<3> A typical value is `PROMETHEUS_STORAGE_SIZE=2000Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.
<4> A typical value is `ALERTMANAGER_STORAGE_SIZE=20Gi`. Storage values can be a plain integer or a fixed-point integer using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki.

. Add values for the retention period, storage class, and storage sizes.

. Save the file.

. Apply the changes by running:
+
[source,terminal]
----
$ oc create -f cluster-monitoring-config.yaml
----
