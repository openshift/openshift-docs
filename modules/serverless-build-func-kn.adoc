// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-build-func-kn_{context}"]
= Building functions

Before you can run a function, you must build the function project. If you are using the `kn func run` command, the function is built automatically. However, you can use the `kn func build` command to build a function without running it, which can be useful for advanced users or debugging scenarios.

The `kn func build` command creates an OCI container image that can be run locally on your computer or on an {product-title} cluster. This command uses the function project name and the image registry name to construct a fully qualified image name for your function.

[id="serverless-build-func-kn-image-containers_{context}"]
== Image container types

By default, `kn func build` creates a container image by using Red Hat Source-to-Image (S2I) technology.

.Example build command using Red Hat Source-to-Image (S2I)
[source,terminal]
----
$ kn func build
----

[id="serverless-build-func-kn-image-registries_{context}"]
== Image registry types

The OpenShift Container Registry is used by default as the image registry for storing function images.

.Example build command using OpenShift Container Registry
[source,terminal]
----
$ kn func build
----

.Example output
[source,terminal]
----
Building function image
Function image has been built, image: registry.redhat.io/example/example-function:latest
----

You can override using OpenShift Container Registry as the default image registry by using the `--registry` flag:

.Example build command overriding OpenShift Container Registry to use quay.io
[source,terminal]
----
$ kn func build --registry quay.io/username
----

.Example output
[source,terminal]
----
Building function image
Function image has been built, image: quay.io/username/example-function:latest
----

[id="serverless-build-func-kn-push_{context}"]
== Push flag

You can add the `--push` flag to a `kn func build` command to automatically push the function image after it is successfully built:

.Example build command using OpenShift Container Registry
[source,terminal]
----
$ kn func build --push
----

[id="serverless-build-func-kn-help_{context}"]
== Help command

You can use the help command to learn more about `kn func build` command options:

.Build help command
[source,terminal]
----
$ kn func help build
----
