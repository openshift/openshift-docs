// Module included in the following assemblies:
// * openshift_images/images-understand.adoc
// * openshift_images/tagging-images.adoc

[id="images-tag_{context}"]
= Image tags

An image tag is a label applied to a container image in a repository that distinguishes a specific image from other images in an image stream. Typically, the tag represents a version number of some sort. For example, here `:v3.11.59-2` is the tag:

[source,text]
----
registry.access.redhat.com/openshift3/jenkins-2-rhel7:v3.11.59-2
----

You can add additional tags to an image. For example, an image might be assigned the tags `:v3.11.59-2` and `:latest`.

{product-title} provides the `oc tag` command, which is similar to the `docker tag` command, but operates on image streams instead of directly on images.
