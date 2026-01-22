// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-viewing-logs_{context}"]
= Viewing deployment logs

.Procedure

. To stream the logs of the latest revision for a given `DeploymentConfig` object:
+
[source,terminal]
----
$ oc logs -f dc/<name>
----
+
If the latest revision is running or failed, the command returns the logs of the process that is responsible for deploying your pods. If it is successful, it returns the logs from a pod of your application.

. You can also view logs from older failed deployment processes, if and only if these processes (old replication controllers and their deployer pods) exist and have not been pruned or deleted manually:
+
[source,terminal]
----
$ oc logs --version=1 dc/<name>
----
