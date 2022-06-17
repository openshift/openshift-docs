// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-binary-source_{context}"]
= Binary (local) source

Streaming content from a local file system to the builder is called a `Binary` type build. The corresponding value of `BuildConfig.spec.source.type` is `Binary` for these builds.

This source type is unique in that it is leveraged solely based on your use of the `oc start-build`.

[NOTE]
====
Binary type builds require content to be streamed from the local file system, so automatically triggering a binary type build, like an image change trigger, is not possible. This is because the binary files cannot be provided. Similarly, you cannot launch binary type builds from the web console.
====

To utilize binary builds, invoke `oc start-build` with one of these options:

* `--from-file`: The contents of the file you specify are sent as a binary stream to the builder. You can also specify a URL to a file. Then, the builder stores the data in a file with the same name at the top of the build context.

* `--from-dir` and `--from-repo`: The contents are archived and sent as a binary stream to the builder. Then, the builder extracts the contents of the archive within the build context directory. With `--from-dir`, you can also specify a URL to an archive, which is extracted.

* `--from-archive`: The archive you specify is sent to the builder, where it is extracted within the build context directory. This option behaves the same as `--from-dir`; an archive is created on your host first, whenever the argument to these options is a directory.

In each of the previously listed cases:

* If your `BuildConfig` already has a `Binary` source type defined, it is effectively ignored and replaced by what the client sends.

* If your `BuildConfig` has a `Git` source type defined, it is dynamically disabled, since `Binary` and `Git` are mutually exclusive, and the data in the binary stream provided to the builder takes precedence.

Instead of a file name, you can pass a URL with HTTP or HTTPS schema to `--from-file` and `--from-archive`. When using `--from-file` with a URL, the name of the file in the builder image is determined by the `Content-Disposition` header sent by the web server, or the last component of the URL path if the header is not present. No form of authentication is supported and it is not possible to use custom TLS certificate or disable certificate validation.

When using `oc new-build --binary=true`, the command ensures that the restrictions associated with binary builds are enforced. The resulting `BuildConfig` has a source type of `Binary`, meaning that the only valid way to run a build for this `BuildConfig` is to use `oc start-build` with one of the `--from` options to provide the requisite binary data.

ifndef::openshift-online[]
The Dockerfile and `contextDir` source options have special meaning with binary builds.

Dockerfile can be used with any binary build source. If Dockerfile is used and the binary stream is an archive, its contents serve as a replacement Dockerfile to any Dockerfile in the archive. If Dockerfile is used with the `--from-file` argument, and the file argument is named Dockerfile, the value from Dockerfile replaces the value from the binary stream.
endif::[]

In the case of the binary stream encapsulating extracted archive content, the value of the `contextDir` field is interpreted as a subdirectory within the archive, and, if valid, the builder changes into that subdirectory before executing the build.
