// Module included in the following assemblies:
// * openshift_images/tagging-images

:_mod-docs-content-type: PROCEDURE
[id="images-referencing-images-imagestreams_{context}"]
= Referencing images in imagestreams

You can use tags to reference images in image streams using the following reference types.

.Imagestream reference types
[width="50%",options="header"]
|===
|Reference type |Description

|`ImageStreamTag`
|An `ImageStreamTag` is used to reference or retrieve an image for a given image stream and tag.

|`ImageStreamImage`
|An `ImageStreamImage` is used to reference or retrieve an image for a given image stream and image `sha` ID.

|`DockerImage`
|A `DockerImage` is used to reference or retrieve an image for a given external registry. It uses standard Docker `pull specification` for its name.
|===

When viewing example image stream definitions you may notice they contain definitions of `ImageStreamTag` and references to `DockerImage`, but nothing related to `ImageStreamImage`.

This is because the `ImageStreamImage` objects are automatically created in {product-title} when you import or tag an image into the image stream. You should never have to explicitly define an `ImageStreamImage` object in any image stream definition that you use to create image streams.

.Procedure

* To reference an image for a given image stream and tag, use `ImageStreamTag`:
+
----
<image_stream_name>:<tag>
----

* To reference an image for a given image stream and image `sha` ID, use `ImageStreamImage`:
+
----
<image_stream_name>@<id>
----
+
The `<id>` is an immutable identifier for a specific image, also called a
digest.

* To reference or retrieve an image for a given external registry, use `DockerImage`:
+
----
openshift/ruby-20-centos7:2.0
----
+
[NOTE]
====
When no tag is specified, it is assumed the `latest` tag is used.
====
+
You can also reference a third-party registry:
+
----
registry.redhat.io/rhel7:latest
----
+
Or an image with a digest:
+
----
centos/ruby-22-centos7@sha256:3a335d7d8a452970c5b4054ad7118ff134b3a6b50a2bb6d0c07c746e8986b28e
----
