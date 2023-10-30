// Module included in the following assemblies:
//
// * applications/deployments/managing-deployment-processes.adoc

:_mod-docs-content-type: PROCEDURE
[id="deployments-viewing-a-deployment_{context}"]
= Viewing a deployment

You can view a deployment to get basic information about all the available revisions of your application.

.Procedure

. To show details about all recently created replication controllers for the provided `DeploymentConfig` object, including any currently running deployment process, run the following command:
+
[source,terminal]
----
$ oc rollout history dc/<name>
----

. To view details specific to a revision, add the `--revision` flag:
+
[source,terminal]
----
$ oc rollout history dc/<name> --revision=1
----

. For more detailed information about a `DeploymentConfig` object and its latest revision, use the `oc describe` command:
+
[source,terminal]
----
$ oc describe dc <name>
----
