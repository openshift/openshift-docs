// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-start-re-run_{context}"]
= Re-running a build

You can manually re-run a build using the `--from-build` flag.

.Procedure

* To manually re-run a build, enter the following command:
+
[source,terminal]
----
$ oc start-build --from-build=<build_name>
----
