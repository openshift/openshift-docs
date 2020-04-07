// Module included in the following assemblies:
//
// * monitoring/configuring-monitoring-stack.adoc

[id="setting-persistent-storage-size_{context}"]
= Setting persistent storage size

You can specify the size of the persistent volume claim for Prometheus and Alertmanager.

.Procedure

* Change these Ansible variables:
+
--
* `openshift_cluster_monitoring_operator_prometheus_storage_capacity` (default: 50Gi)
* `openshift_cluster_monitoring_operator_alertmanager_storage_capacity` (default: 2Gi)
--
+
Each of these variables applies only if its corresponding `storage_enabled` variable is set to `true`.

