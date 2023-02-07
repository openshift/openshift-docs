// Module included in the following assemblies:
//* builds/build-strategies.adoc

[id="builds-strategy-force-pull-procedure_{context}"]
= Using the force pull flag

By default, if the builder image specified in the build configuration is available locally on the node, that image will be used. However, you can use the `forcepull` flag to override the local image and refresh it from the registry.

.Procedure

To override the local image and refresh it from the registry to which the image stream points, create a `BuildConfig` with the `forcePull` flag set to `true`.
