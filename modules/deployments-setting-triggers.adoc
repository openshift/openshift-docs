// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-setting-triggers_{context}"]
= Setting deployment triggers

.Procedure

. You can set deployment triggers for a `DeploymentConfig` object using the `oc set triggers` command. For example, to set a image change trigger, use the following command:
+
[source,terminal]
----
$ oc set triggers dc/<dc_name> \
    --from-image=<project>/<image>:<tag> -c <container_name>
----
