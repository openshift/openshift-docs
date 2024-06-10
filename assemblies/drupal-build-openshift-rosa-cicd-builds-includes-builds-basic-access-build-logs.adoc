// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-access-build-logs_{context}"]
= Accessing build logs

You can access build logs using the web console or the CLI.

.Procedure

* To stream the logs using the build directly, enter the following command:
+
[source,terminal]
----
$ oc describe build <build_name>
----
