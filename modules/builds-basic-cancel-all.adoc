// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-cancel-all_{context}"]
= Canceling all builds

You can cancel all builds from the build configuration with the following CLI command.

.Procedure

* To cancel all builds, enter the following command:
+
[source,terminal]
----
$ oc cancel-build bc/<buildconfig_name>
----
