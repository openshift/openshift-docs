// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-access-buildconfig-logs_{context}"]
= Accessing BuildConfig logs

You can access `BuildConfig` logs using the web console or the CLI.

.Procedure

* To stream the logs of the latest build for a `BuildConfig`, enter the following command:
+
[source,terminal]
----
$ oc logs -f bc/<buildconfig_name>
----
