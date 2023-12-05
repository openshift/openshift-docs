// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-checking-the-managed-cluster-status_{context}"]
= Monitoring the managed cluster installation status

Ensure that cluster provisioning was successful by checking the cluster status.

.Prerequisites

* All of the custom resources have been configured and provisioned, and the `Agent`
custom resource is created on the hub for the managed cluster.

.Procedure

. Check the status of the managed cluster:
+
[source,terminal]
----
$ oc get managedcluster
----
+
`True` indicates the managed cluster is ready.

. Check the agent status:
+
[source,terminal]
----
$ oc get agent -n <cluster_name>
----

. Use the `describe` command to provide an in-depth description of the agent’s condition. Statuses to be aware of include `BackendError`, `InputError`, `ValidationsFailing`, `InstallationFailed`, and `AgentIsConnected`. These statuses are relevant to the `Agent` and `AgentClusterInstall` custom resources.
+
[source,terminal]
----
$ oc describe agent -n <cluster_name>
----

. Check the cluster provisioning status:
+
[source,terminal]
----
$ oc get agentclusterinstall -n <cluster_name>
----

. Use the `describe` command to provide an in-depth description of the cluster provisioning status:
+
[source,terminal]
----
$ oc describe agentclusterinstall -n <cluster_name>
----

. Check the status of the managed cluster’s add-on services:
+
[source,terminal]
----
$ oc get managedclusteraddon -n <cluster_name>
----

. Retrieve the authentication information of the `kubeconfig` file for the managed cluster:
+
[source,terminal]
----
$ oc get secret -n <cluster_name> <cluster_name>-admin-kubeconfig -o jsonpath={.data.kubeconfig} | base64 -d > <directory>/<cluster_name>-kubeconfig
----
