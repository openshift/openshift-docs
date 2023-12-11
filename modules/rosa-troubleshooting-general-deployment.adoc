// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
:_mod-docs-content-type: PROCEDURE
[id="rosa-troubleshooting-general-deployment-failure_{context}"]
= Obtaining information on a failed cluster

If a cluster deployment fails, the cluster is put into an "error" state.

.Procedure
Run the following command to get more information:

[source,terminal]
----
$ rosa describe cluster -c <my_cluster_name> --debug
----
