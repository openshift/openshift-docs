// Module included in the following assemblies:
// * openshift_images/tagging-images

:_mod-docs-content-type: PROCEDURE
[id="images-add-tags-to-imagestreams_{context}"]
= Adding tags to image streams

An image stream in {product-title} comprises zero or more container images identified by tags.

There are different types of tags available. The default behavior uses a `permanent` tag, which points to a specific image in time. If the `permanent` tag is in use and the source changes, the tag does not change for the destination.

A `tracking` tag means the destination tag's metadata is updated during the import of the source tag.

.Procedure

* You can add tags to an image stream using the `oc tag` command:
+
[source,terminal]
----
$ oc tag <source> <destination>
----
+
For example, to configure the `ruby` image stream `static-2.0` tag to always refer to the current image for the `ruby` image stream `2.0` tag:
+
[source,terminal]
----
$ oc tag ruby:2.0 ruby:static-2.0
----
+
This creates a new image stream tag named `static-2.0` in the `ruby` image stream. The new tag directly references the image id that the `ruby:2.0` image stream tag pointed to at the time `oc tag` was run, and the image it points to never changes.

* To ensure the destination tag is updated when the source tag changes, use the `--alias=true` flag:
+
[source,terminal]
----
$ oc tag --alias=true <source> <destination>
----

[NOTE]
====
Use a tracking tag for creating permanent aliases, for example, `latest` or `stable`. The tag only works correctly within a single image stream. Trying to create a cross-image stream alias produces an error.
====

* You can also add the `--scheduled=true` flag to have the destination tag be
refreshed, or re-imported, periodically. The period is configured globally at
the system level.

* The `--reference` flag creates an image stream tag that is not imported. The tag points to the source location, permanently.
+
If you want to instruct {product-title} to always fetch the tagged image from the integrated registry, use `--reference-policy=local`. The registry uses the pull-through feature to serve the image to the client. By default, the image blobs are mirrored locally by the registry. As a result, they can be pulled more quickly the next time they are needed. The flag also allows for pulling from insecure registries without a need to supply `--insecure-registry` to the container runtime as long as the image stream has an insecure annotation or the tag has an insecure import policy.
