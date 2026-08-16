// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-access-buildconfig-version-logs_{context}"]
= Accessing BuildConfig logs for a given version build

You can access logs for a given version build for a `BuildConfig` using the web console or the CLI.

.Procedure

* To stream the logs for a given version build for a `BuildConfig`, enter the following command:
+
[source,terminal]
----
$ oc logs --version=<number> bc/<buildconfig_name>
----
