// Module included in the following assemblies:
//
// * builds/advanced-build-operations.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-setting-maximum-duration_{context}"]
= Setting maximum duration

When defining a `BuildConfig` object, you can define its maximum duration by setting the `completionDeadlineSeconds` field. It is specified in seconds and is not set by default. When not set, there is no maximum duration enforced.

The maximum duration is counted from the time when a build pod gets scheduled in the system, and defines how long it can be active, including the time needed to pull the builder image. After reaching the specified timeout, the build is terminated by {product-title}.

.Procedure

* To set maximum duration, specify `completionDeadlineSeconds` in your `BuildConfig`. The following example shows the part of a `BuildConfig` specifying `completionDeadlineSeconds` field for 30 minutes:
+
[source,yaml]
----
spec:
  completionDeadlineSeconds: 1800
----

[NOTE]
====
This setting is not supported with the Pipeline Strategy option.
====
