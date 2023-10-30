// Module included in the following assemblies:
//
// * virt/monitoring/virt-exposing-custom-metrics-for-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-accessing-node-exporter-outside-cluster_{context}"]
= Accessing the node exporter service outside the cluster

You can access the node-exporter service outside the cluster and view the exposed metrics.

.Prerequisites
* You have access to the cluster as a user with `cluster-admin` privileges or the `monitoring-edit` role.
* You have enabled monitoring for the user-defined project by configuring the node-exporter service.

.Procedure

. Expose the node-exporter service.
+
[source,terminal]
----
$ oc expose service -n <namespace> <node_exporter_service_name>
----
. Obtain the FQDN (Fully Qualified Domain Name) for the route.
+
[source,terminal]
----
$ oc get route -o=custom-columns=NAME:.metadata.name,DNS:.spec.host
----
+
.Example output
[source,terminal]
----
NAME                    DNS
node-exporter-service   node-exporter-service-dynamation.apps.cluster.example.org
----
. Use the `curl` command to display metrics for the node-exporter service.
+
[source,terminal]
----
$ curl -s http://node-exporter-service-dynamation.apps.cluster.example.org/metrics
----
+
.Example output
[source,terminal]
----
go_gc_duration_seconds{quantile="0"} 1.5382e-05
go_gc_duration_seconds{quantile="0.25"} 3.1163e-05
go_gc_duration_seconds{quantile="0.5"} 3.8546e-05
go_gc_duration_seconds{quantile="0.75"} 4.9139e-05
go_gc_duration_seconds{quantile="1"} 0.000189423
----
