// Module is included in the following assemblies:
//
// cli_reference/developer_cli_odo/using-devfiles-in-odo.adoc

:_mod-docs-content-type: PROCEDURE
[id="converting-an-s2i-component-into-a-devfile-component_{context}"]
= Converting an S2I component into a devfile component

With `{odo-title}`, you can create both Source-to-Image (S2I) and devfile components. If you have an existing S2I component, you can convert it into a devfile component using the `odo utils` command.

.Procedure

Run all the commands from the S2I component directory.

. Run the `odo utils convert-to-devfile` command, which creates `devfile.yaml` and `env.yaml` based on your component:
+
[source,terminal]
----
$ odo utils convert-to-devfile
----

. Push the component to your cluster:
+
[source,terminal]
----
$ odo push
----
+
[NOTE]
====
If the devfile component deployment failed, delete it by running: `odo delete -a`
====
+

. Verify that the devfile component deployed successfully:
+
[source,terminal]
----
$ odo list
----

. Delete the S2I component:
+
[source,terminal]
----
$ odo delete --s2i
----
