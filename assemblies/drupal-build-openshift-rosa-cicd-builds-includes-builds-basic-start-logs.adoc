// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-start-logs_{context}"]
= Streaming build logs

You can specify the `--follow` flag to stream the build's logs in `stdout`.

.Procedure

* To manually stream a build's logs in `stdout`, enter the following command:
+
[source,terminal]
----
$ oc start-build <buildconfig_name> --follow
----
