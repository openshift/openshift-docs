// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-retrying-deployment_{context}"]
= Retrying a deployment

If the current revision of your `DeploymentConfig` object failed to deploy, you can restart the deployment process.

.Procedure

. To restart a failed deployment process:
+
[source,terminal]
----
$ oc rollout retry dc/<name>
----
+
If the latest revision of it was deployed successfully, the command displays a message and the deployment process is not retried.
+
[NOTE]
====
Retrying a deployment restarts the deployment process and does not create a new deployment revision. The restarted replication controller has the same configuration it had when it failed.
====
