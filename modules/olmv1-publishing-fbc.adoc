// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-plain-bundles.adoc

:_mod-docs-content-type: PROCEDURE

[id="olmv1-publishing-fbc_{context}"]
= Building and publishing a file-based catalog

.Procedure

. Build your file-based catalog as an image by running the following command:
+
[source,terminal]
----
$ podman build -f <catalog_dir>.Dockerfile -t \
    quay.io/<organization_name>/<repository_name>:<image_tag> .
----

. Push your catalog image by running the following command:
+
[source,terminal]
----
$ podman push quay.io/<organization_name>/<repository_name>:<image_tag>
----