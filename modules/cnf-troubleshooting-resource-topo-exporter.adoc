// Module included in the following assemblies:
//
// *scalability_and_performance/cnf-numa-aware-scheduling.adoc

:_module-type: PROCEDURE
[id="cnf-troubleshooting-resource-topo-exporter_{context}"]
= Troubleshooting the resource topology exporter

Troubleshoot `noderesourcetopologies` objects where unexpected results are occurring by inspecting the corresponding `resource-topology-exporter` logs.

[NOTE]
====
It is recommended that NUMA resource topology exporter instances in the cluster are named for nodes they refer to. For example, a worker node with the name `worker` should have a corresponding `noderesourcetopologies` object called `worker`.
====

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Get the daemonsets managed by the NUMA Resources Operator. Each daemonset has a corresponding `nodeGroup` in the `NUMAResourcesOperator` CR. Run the following command:
+
[source,terminal]
----
$ oc get numaresourcesoperators.nodetopology.openshift.io numaresourcesoperator -o jsonpath="{.status.daemonsets[0]}"
----
+
.Example output
[source,json]
----
{"name":"numaresourcesoperator-worker","namespace":"openshift-numaresources"}
----

. Get the label for the daemonset of interest using the value for `name` from the previous step:
+
[source,terminal]
----
$ oc get ds -n openshift-numaresources numaresourcesoperator-worker -o jsonpath="{.spec.selector.matchLabels}"
----
+
.Example output
[source,json]
----
{"name":"resource-topology"}
----

. Get the pods using the `resource-topology` label by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-numaresources -l name=resource-topology -o wide
----
+
.Example output
[source,terminal]
----
NAME                                 READY   STATUS    RESTARTS   AGE    IP            NODE
numaresourcesoperator-worker-5wm2k   2/2     Running   0          2d1h   10.135.0.64   compute-0.example.com
numaresourcesoperator-worker-pb75c   2/2     Running   0          2d1h   10.132.2.33   compute-1.example.com
----

. Examine the logs of the `resource-topology-exporter` container running on the worker pod that corresponds to the node you are troubleshooting. Run the following command:
+
[source,terminal]
----
$ oc logs -n openshift-numaresources -c resource-topology-exporter numaresourcesoperator-worker-pb75c
----
+
.Example output
[source,terminal]
----
I0221 13:38:18.334140       1 main.go:206] using sysinfo:
reservedCpus: 0,1
reservedMemory:
  "0": 1178599424
I0221 13:38:18.334370       1 main.go:67] === System information ===
I0221 13:38:18.334381       1 sysinfo.go:231] cpus: reserved "0-1"
I0221 13:38:18.334493       1 sysinfo.go:237] cpus: online "0-103"
I0221 13:38:18.546750       1 main.go:72]
cpus: allocatable "2-103"
hugepages-1Gi:
  numa cell 0 -> 6
  numa cell 1 -> 1
hugepages-2Mi:
  numa cell 0 -> 64
  numa cell 1 -> 128
memory:
  numa cell 0 -> 45758Mi
  numa cell 1 -> 48372Mi
----
