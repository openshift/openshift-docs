// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-build-environment_{context}"]
= Build environments

As with pod environment variables, build environment variables can be defined in terms of references to other resources or variables using the Downward API. There are some exceptions, which are noted.

You can also manage environment variables defined in the `BuildConfig` with the `oc set env` command.

[NOTE]
====
Referencing container resources using `valueFrom` in build environment variables is not supported as the references are resolved before the container is created.
====
