// Module included in the following assemblies:
// * builds/basic-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-basic-cancel-all-state_{context}"]
= Canceling all builds in a given state

You can cancel all builds in a given state, such as `new` or `pending`, while ignoring the builds in other states.

.Procedure

* To cancel all in a given state, enter the following command:
+
[source,terminal]
----
$ oc cancel-build bc/<buildconfig_name>
----
