// Module included in the following assemblies:
//
// * builds/triggering-builds-build-hooks.adoc

[id="builds-configuration-change-triggers_{context}"]
= Configuration change triggers

A configuration change trigger allows a build to be automatically invoked as soon as a new `BuildConfig` is created.

The following is an example trigger definition YAML within the `BuildConfig`:

[source,yaml]
----
  type: "ConfigChange"
----

[NOTE]
====
Configuration change triggers currently only work when creating a new `BuildConfig`. In a future release, configuration change triggers will also be able to launch a build whenever a `BuildConfig` is updated.
====
