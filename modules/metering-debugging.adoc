// Module included in the following assemblies:
//
// * metering/metering-troubleshooting-debugging.adoc

[id="metering-debugging_{context}"]
= Debugging metering

Debugging metering is much easier when you interact directly with the various components. The sections below detail how you can connect and query Presto and Hive as well as view the dashboards of the Presto and HDFS components.

[NOTE]
====
All of the commands in this section assume you have installed metering through OperatorHub in the `openshift-metering` namespace.
====

[id="metering-get-reporting-operator-logs_{context}"]
== Get reporting operator logs
Use the command below to follow the logs of the `reporting-operator`:

[source,terminal]
----
$ oc -n openshift-metering logs -f "$(oc -n openshift-metering get pods -l app=reporting-operator -o name | cut -c 5-)" -c reporting-operator
----

[id="metering-query-presto-using-presto-cli_{context}"]
== Query Presto using presto-cli
The following command opens an interactive presto-cli session where you can query Presto. This session runs in the same container as Presto and launches an additional Java instance, which can create memory limits for the pod. If this occurs, you should increase the memory request and limits of the Presto pod.

By default, Presto is configured to communicate using TLS. You must use the following command to run Presto queries:

[source,terminal]
----
$ oc -n openshift-metering exec -it "$(oc -n openshift-metering get pods -l app=presto,presto=coordinator -o name | cut -d/ -f2)"  \
  -- /usr/local/bin/presto-cli --server https://presto:8080 --catalog hive --schema default --user root --keystore-path /opt/presto/tls/keystore.pem
----

Once you run this command, a prompt appears where you can run queries. Use the `show tables from metering;` query to view the list of tables:

[source,terminal]
----
$ presto:default> show tables from metering;
----

.Example output
[source,terminal]
----
                                 Table

 datasource_your_namespace_cluster_cpu_capacity_raw
 datasource_your_namespace_cluster_cpu_usage_raw
 datasource_your_namespace_cluster_memory_capacity_raw
 datasource_your_namespace_cluster_memory_usage_raw
 datasource_your_namespace_node_allocatable_cpu_cores
 datasource_your_namespace_node_allocatable_memory_bytes
 datasource_your_namespace_node_capacity_cpu_cores
 datasource_your_namespace_node_capacity_memory_bytes
 datasource_your_namespace_node_cpu_allocatable_raw
 datasource_your_namespace_node_cpu_capacity_raw
 datasource_your_namespace_node_memory_allocatable_raw
 datasource_your_namespace_node_memory_capacity_raw
 datasource_your_namespace_persistentvolumeclaim_capacity_bytes
 datasource_your_namespace_persistentvolumeclaim_capacity_raw
 datasource_your_namespace_persistentvolumeclaim_phase
 datasource_your_namespace_persistentvolumeclaim_phase_raw
 datasource_your_namespace_persistentvolumeclaim_request_bytes
 datasource_your_namespace_persistentvolumeclaim_request_raw
 datasource_your_namespace_persistentvolumeclaim_usage_bytes
 datasource_your_namespace_persistentvolumeclaim_usage_raw
 datasource_your_namespace_persistentvolumeclaim_usage_with_phase_raw
 datasource_your_namespace_pod_cpu_request_raw
 datasource_your_namespace_pod_cpu_usage_raw
 datasource_your_namespace_pod_limit_cpu_cores
 datasource_your_namespace_pod_limit_memory_bytes
 datasource_your_namespace_pod_memory_request_raw
 datasource_your_namespace_pod_memory_usage_raw
 datasource_your_namespace_pod_persistentvolumeclaim_request_info
 datasource_your_namespace_pod_request_cpu_cores
 datasource_your_namespace_pod_request_memory_bytes
 datasource_your_namespace_pod_usage_cpu_cores
 datasource_your_namespace_pod_usage_memory_bytes
(32 rows)

Query 20210503_175727_00107_3venm, FINISHED, 1 node
Splits: 19 total, 19 done (100.00%)
0:02 [32 rows, 2.23KB] [19 rows/s, 1.37KB/s]

presto:default>
----

[id="metering-query-hive-using-beeline_{context}"]
== Query Hive using beeline
The following opens an interactive beeline session where you can query Hive. This session runs in the same container as Hive and launches an additional Java instance, which can create memory limits for the pod. If this occurs, you should increase the memory request and limits of the Hive pod.

[source,terminal]
----
$ oc -n openshift-metering exec -it $(oc -n openshift-metering get pods -l app=hive,hive=server -o name | cut -d/ -f2) \
  -c hiveserver2 -- beeline -u 'jdbc:hive2://127.0.0.1:10000/default;auth=noSasl'
----

Once you run this command, a prompt appears where you can run queries. Use the `show tables;` query to view the list of tables:

[source,terminal]
----
$ 0: jdbc:hive2://127.0.0.1:10000/default> show tables from metering;
----

.Example output
[source,terminal]
----
+----------------------------------------------------+
|                      tab_name                      |
+----------------------------------------------------+
| datasource_your_namespace_cluster_cpu_capacity_raw |
| datasource_your_namespace_cluster_cpu_usage_raw  |
| datasource_your_namespace_cluster_memory_capacity_raw |
| datasource_your_namespace_cluster_memory_usage_raw |
| datasource_your_namespace_node_allocatable_cpu_cores |
| datasource_your_namespace_node_allocatable_memory_bytes |
| datasource_your_namespace_node_capacity_cpu_cores |
| datasource_your_namespace_node_capacity_memory_bytes |
| datasource_your_namespace_node_cpu_allocatable_raw |
| datasource_your_namespace_node_cpu_capacity_raw  |
| datasource_your_namespace_node_memory_allocatable_raw |
| datasource_your_namespace_node_memory_capacity_raw |
| datasource_your_namespace_persistentvolumeclaim_capacity_bytes |
| datasource_your_namespace_persistentvolumeclaim_capacity_raw |
| datasource_your_namespace_persistentvolumeclaim_phase |
| datasource_your_namespace_persistentvolumeclaim_phase_raw |
| datasource_your_namespace_persistentvolumeclaim_request_bytes |
| datasource_your_namespace_persistentvolumeclaim_request_raw |
| datasource_your_namespace_persistentvolumeclaim_usage_bytes |
| datasource_your_namespace_persistentvolumeclaim_usage_raw |
| datasource_your_namespace_persistentvolumeclaim_usage_with_phase_raw |
| datasource_your_namespace_pod_cpu_request_raw    |
| datasource_your_namespace_pod_cpu_usage_raw      |
| datasource_your_namespace_pod_limit_cpu_cores    |
| datasource_your_namespace_pod_limit_memory_bytes |
| datasource_your_namespace_pod_memory_request_raw |
| datasource_your_namespace_pod_memory_usage_raw   |
| datasource_your_namespace_pod_persistentvolumeclaim_request_info |
| datasource_your_namespace_pod_request_cpu_cores  |
| datasource_your_namespace_pod_request_memory_bytes |
| datasource_your_namespace_pod_usage_cpu_cores    |
| datasource_your_namespace_pod_usage_memory_bytes |
+----------------------------------------------------+
32 rows selected (13.101 seconds)
0: jdbc:hive2://127.0.0.1:10000/default>
----

[id="metering-port-forward-hive-web-ui_{context}"]
== Port-forward to the Hive web UI
Run the following command to port-forward to the Hive web UI:

[source,terminal]
----
$ oc -n openshift-metering port-forward hive-server-0 10002
----

You can now open http://127.0.0.1:10002 in your browser window to view the Hive web interface.

[id="metering-port-forward-hdfs_{context}"]
== Port-forward to HDFS
Run the following command to port-forward to the HDFS namenode:

[source,terminal]
----
$ oc -n openshift-metering port-forward hdfs-namenode-0 9870
----

You can now open http://127.0.0.1:9870 in your browser window to view the HDFS web interface.

Run the following command to port-forward to the first HDFS datanode:

[source,terminal]
----
$ oc -n openshift-metering port-forward hdfs-datanode-0 9864 <1>
----
<1> To check other datanodes, replace `hdfs-datanode-0` with the pod you want to view information on.

[id="metering-ansible-operator_{context}"]
== Metering Ansible Operator
Metering uses the Ansible Operator to watch and reconcile resources in a cluster environment. When debugging a failed metering installation, it can be helpful to view the Ansible logs or status of your `MeteringConfig` custom resource.

[id="metering-accessing-ansible-logs_{context}"]
=== Accessing Ansible logs
In the default installation, the Metering Operator is deployed as a pod. In this case, you can check the logs of the Ansible container within this pod:

[source,terminal]
----
$ oc -n openshift-metering logs $(oc -n openshift-metering get pods -l app=metering-operator -o name | cut -d/ -f2) -c ansible
----

Alternatively, you can view the logs of the Operator container (replace `-c ansible` with `-c operator`) for condensed output.

[id="metering-checking-meteringconfig-status_{context}"]
=== Checking the MeteringConfig Status
It can be helpful to view the `.status` field of your `MeteringConfig` custom resource to debug any recent failures. The following command shows status messages with type `Invalid`:

[source,terminal]
----
$ oc -n openshift-metering get meteringconfig operator-metering -o=jsonpath='{.status.conditions[?(@.type=="Invalid")].message}'
----
// $ oc -n openshift-metering get meteringconfig operator-metering -o json | jq '.status'

[id="metering-checking-meteringconfig-events_{context}"]
=== Checking MeteringConfig Events
Check events that the Metering Operator is generating. This can be helpful during installation or upgrade to debug any resource failures. Sort events by the last timestamp:

[source,terminal]
----
$ oc -n openshift-metering get events --field-selector involvedObject.kind=MeteringConfig --sort-by='.lastTimestamp'
----

.Example output with latest changes in the MeteringConfig resources
[source,terminal]
----
LAST SEEN   TYPE     REASON        OBJECT                             MESSAGE
4m40s       Normal   Validating    meteringconfig/operator-metering   Validating the user-provided configuration
4m30s       Normal   Started       meteringconfig/operator-metering   Configuring storage for the metering-ansible-operator
4m26s       Normal   Started       meteringconfig/operator-metering   Configuring TLS for the metering-ansible-operator
3m58s       Normal   Started       meteringconfig/operator-metering   Configuring reporting for the metering-ansible-operator
3m53s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling metering resources
3m47s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling monitoring resources
3m41s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling HDFS resources
3m23s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling Hive resources
2m59s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling Presto resources
2m35s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling reporting-operator resources
2m14s       Normal   Reconciling   meteringconfig/operator-metering   Reconciling reporting resources
----
