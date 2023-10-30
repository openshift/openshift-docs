// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-import-import-mode_{context}"]
= Working with manifest lists

You can import a single sub-manifest, or all manifests, of a manifest list when using `oc import-image` or `oc tag` CLI commands by adding the `--import-mode` flag.

Refer to the commands below to create an image stream that includes a single sub-manifest or multi-architecture images.

.Procedure

* Create an image stream that includes multi-architecture images, and sets the import mode to `PreserveOriginal`, by entering the following command:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --reference-policy=local --confirm
----
+
.Example output
+
[source,terminal]
----
---
Arch:           <none>
Manifests:      linux/amd64     sha256:6e325b86566fafd3c4683a05a219c30c421fbccbf8d87ab9d20d4ec1131c3451
                linux/arm64     sha256:d8fad562ffa75b96212c4a6dc81faf327d67714ed85475bf642729703a2b5bf6
                linux/ppc64le   sha256:7b7e25338e40d8bdeb1b28e37fef5e64f0afd412530b257f5b02b30851f416e1
---
----

* Alternatively, enter the following command to import an image with the `Legacy` import mode, which discards manifest lists and imports a single sub-manifest:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='Legacy' --confirm
----
+
[NOTE]
====
The `--import-mode=` default value is `Legacy`. Excluding this value, or failing to specify either `Legacy` or `PreserveOriginal`, imports a single sub-manifest. An invalid import mode returns the following error: `error: valid ImportMode values are Legacy or PreserveOriginal`.
====

[discrete]
[id="images-imagestream-import-import-mode-limitations"]
== Limitations

Working with manifest lists has the following limitations:

* In some cases, users might want to use sub-manifests directly. When `oc adm prune images` is run, or the `CronJob` pruner runs, they cannot detect when a sub-manifest list is used. As a result, an administrator using `oc adm prune images`, or the `CronJob` pruner, might delete entire manifest lists, including sub-manifests.
+
To avoid this limitation, you can use the manifest list by tag or by digest instead.
