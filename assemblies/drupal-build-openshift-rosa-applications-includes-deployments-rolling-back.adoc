// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-rolling-back_{context}"]
= Rolling back a deployment

Rollbacks revert an application back to a previous revision and can be performed using the REST API, the CLI, or the web console.

.Procedure

. To rollback to the last successful deployed revision of your configuration:
+
[source,terminal]
----
$ oc rollout undo dc/<name>
----
+
The `DeploymentConfig` object's template is reverted to match the deployment revision specified in the undo command, and a new replication controller is started. If no revision is specified with `--to-revision`, then the last successfully deployed revision is used.

. Image change triggers on the `DeploymentConfig` object are disabled as part of the rollback to prevent accidentally starting a new deployment process soon after the rollback is complete.
+
To re-enable the image change triggers:
+
[source,terminal]
----
$ oc set triggers dc/<name> --auto
----

[NOTE]
====
Deployment configs also support automatically rolling back to the last successful revision of the configuration in case the latest deployment process fails. In that case, the latest template that failed to deploy stays intact by the system and it is up to users to fix their configurations.
====
