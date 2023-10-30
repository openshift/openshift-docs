// Module included in the following assemblies:
//
// cli_reference/developer_cli_odo/using_odo_in_a_restricted_environment/creating-and-deploying-a-component-to-the-disconnected-cluster

:_mod-docs-content-type: PROCEDURE
[id="overwriting-the-mirror-registry_{context}"]
= Overwriting the mirror registry

To download npm packages for Node.js dependencies and Maven packages for Java dependencies from a private mirror registry, you must create and configure a mirror npm or Maven registry on the cluster. You can then overwrite the mirror registry on an existing component or when you create a new component.

.Procedure

* To overwrite the mirror registry on an existing component:
+
[source,terminal]
----
$ odo config set --env NPM_MIRROR=<npm_mirror_registry>
----

* To overwrite the mirror registry when creating a component:
+
[source,terminal]
----
$ odo component create nodejs --env NPM_MIRROR=<npm_mirror_registry>
----
