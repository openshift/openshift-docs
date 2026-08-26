// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-start-environment-variable_{context}"]
= Setting environment variables when starting a build

You can specify the `--env` flag to set any desired environment variable for the build.

.Procedure

* To specify a desired environment variable, enter the following command:
+
[source,terminal]
----
$ oc start-build <buildconfig_name> --env=<key>=<value>
----
