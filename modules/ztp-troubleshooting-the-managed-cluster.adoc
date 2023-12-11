// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-manual-install.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-troubleshooting-the-managed-cluster_{context}"]
= Troubleshooting the managed cluster

Use this procedure to diagnose any installation issues that might occur with the managed cluster.

.Procedure

. Check the status of the managed cluster:
+
[source,terminal]
----
$ oc get managedcluster
----
+
.Example output
[source,terminal]
----
NAME            HUB ACCEPTED   MANAGED CLUSTER URLS   JOINED   AVAILABLE   AGE
SNO-cluster     true                                   True     True      2d19h
----
+
If the status in the `AVAILABLE` column is `True`, the managed cluster is being managed by the hub.
+
If the status in the `AVAILABLE` column is `Unknown`, the managed cluster is not being managed by the hub.
Use the following steps to continue checking to get more information.

. Check the `AgentClusterInstall` install status:
+
[source,terminal]
----
$ oc get clusterdeployment -n <cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        PLATFORM            REGION   CLUSTERTYPE   INSTALLED    INFRAID    VERSION  POWERSTATE AGE
Sno0026    agent-baremetal                               false                          Initialized
2d14h
----
+
If the status in the `INSTALLED` column is `false`, the installation was unsuccessful.

. If the installation failed, enter the following command to review the status of the `AgentClusterInstall` resource:
+
[source,terminal]
----
$ oc describe agentclusterinstall -n <cluster_name> <cluster_name>
----

. Resolve the errors and reset the cluster:

.. Remove the cluster’s managed cluster resource:
+
[source,terminal]
----
$ oc delete managedcluster <cluster_name>
----
.. Remove the cluster’s namespace:
+
[source,terminal]
----
$ oc delete namespace <cluster_name>
----
+
This deletes all of the namespace-scoped custom resources created for this cluster. You must wait for the `ManagedCluster` CR deletion to complete before proceeding.

.. Recreate the custom resources for the managed cluster.
