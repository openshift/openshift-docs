// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-cancel-multiple_{context}"]
= Canceling multiple builds

You can cancel multiple builds with the following CLI command.

.Procedure

* To manually cancel multiple builds, enter the following command:
+
[source,terminal]
----
$ oc cancel-build <build1_name> <build2_name> <build3_name>
----
