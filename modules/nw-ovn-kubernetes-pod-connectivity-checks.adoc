// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ovn-kubernetes-pod-connectivity-checks_{context}"]
= Checking the OVN-Kubernetes pod network connectivity

The connectivity check controller, in {product-title} 4.10 and later, orchestrates connection verification checks in your cluster. These include Kubernetes API, OpenShift API and individual nodes. The results for the connection tests are stored in `PodNetworkConnectivity` objects in the `openshift-network-diagnostics` namespace. Connection tests are performed every minute in parallel.

.Prerequisites

* Access to the OpenShift CLI (`oc`).
* Access to the cluster as a user with the `cluster-admin` role.
* You have installed `jq`.

.Procedure

. To list the current `PodNetworkConnectivityCheck` objects, enter the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics
----

. View the most recent success for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.successes[0]'
----

. View the most recent failures for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.failures[0]'
----

. View the most recent outages for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.outages[0]'
----
+
The connectivity check controller also logs metrics from these checks into Prometheus.

. View all the metrics by running the following command:
+
[source,terminal]
----
$ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
promtool query instant  http://localhost:9090 \
'{component="openshift-network-diagnostics"}'
----

. View the latency between the source pod and the openshift api service for the last 5 minutes:
+
[source,terminal]
----
$ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
promtool query instant  http://localhost:9090 \
'{component="openshift-network-diagnostics"}'
----




