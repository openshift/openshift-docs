// Module included in the following assemblies:
//* builds/build-strategies.adoc

:_mod-docs-content-type: PROCEDURE
[id="builds-strategy-s2i-incremental-builds_{context}"]
= Performing source-to-image incremental builds

Source-to-image (S2I) can perform incremental builds, which means it reuses artifacts from previously-built images.

.Procedure

* To create an incremental build, apply the following modification to the strategy definition:
+
[source,yaml]
----
strategy:
  sourceStrategy:
    from:
      kind: "ImageStreamTag"
      name: "incremental-image:latest" <1>
    incremental: true <2>
----
<1> Specify an image that supports incremental builds. Consult the documentation of the builder image to determine if it supports this behavior.
<2> This flag controls whether an incremental build is attempted. If the builder image does not support incremental builds, the build will still succeed, but you will get a log message stating the incremental build was not successful because of a missing `save-artifacts` script.

[role="_additional-resources"]
.Additional resources

* See S2I Requirements for information on how to create a builder image supporting incremental builds.
