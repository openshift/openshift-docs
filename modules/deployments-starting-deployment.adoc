// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-starting-a-deployment_{context}"]
= Starting a deployment

You can start a rollout to begin the deployment process of your application.

.Procedure

. To start a new deployment process from an existing `DeploymentConfig` object, run the following command:
+
[source,terminal]
----
$ oc rollout latest dc/<name>
----
+
[NOTE]
====
If a deployment process is already in progress, the command displays a message and a new replication controller will not be deployed.
====
