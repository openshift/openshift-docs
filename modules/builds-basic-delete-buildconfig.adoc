// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-delete-buildconfig_{context}"]
= Deleting a BuildConfig

You can delete a `BuildConfig` using the following command.

.Procedure

* To delete a `BuildConfig`, enter the following command:
+
[source,terminal]
----
$ oc delete bc <BuildConfigName>
----
+
This also deletes all builds that were instantiated from this `BuildConfig`.

* To delete a `BuildConfig` and keep the builds instatiated from the `BuildConfig`, specify the `--cascade=false` flag when you enter the following command:
+
[source,terminal]
----
$ oc delete --cascade=false bc <BuildConfigName>
----
