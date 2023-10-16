// Module included in the following assemblies:
//
// * monitoring/configuring-monitoring-stack.adoc

[id="enabling-persistent-storage_{context}"]
= Enabling persistent storage

By default, persistent storage is disabled for both Prometheus time-series data and for Alertmanager notifications and silences. You can configure the cluster to persistently store any one of them or both.

.Procedure

* To enable persistent storage of Prometheus time-series data, set this variable to `true` in the Ansible inventory file:
+
`openshift_cluster_monitoring_operator_prometheus_storage_enabled`
+
To enable persistent storage of Alertmanager notifications and silences, set this variable to `true` in the Ansible inventory file:
+
`openshift_cluster_monitoring_operator_alertmanager_storage_enabled`

