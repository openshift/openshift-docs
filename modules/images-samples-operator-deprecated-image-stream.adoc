// Module included in the following assemblies:
//
// * openshift_images/configuring-samples-operator.adoc
// * openshift_images/configuring-samples-operator.adoc


:_mod-docs-content-type: PROCEDURE
[id="images-samples-operator-deprecated-image-stream_{context}"]
= Removing deprecated image stream tags from the Cluster Samples Operator

The Cluster Samples Operator leaves deprecated image stream tags in an image stream because users can have deployments that use the deprecated image stream tags.

You can remove deprecated image stream tags by editing the image stream with the  `oc tag` command.

[NOTE]
====
Deprecated image stream tags that the samples providers have removed from their image streams are not included on initial installations.
====

.Prerequisites

* You installed the `oc` CLI.

.Procedure

* Remove deprecated image stream tags by editing the image stream with the  `oc tag` command.
+
[source,terminal]
----
$ oc tag -d <image_stream_name:tag>
----
+
.Example output
[source,terminal]
----
Deleted tag default/<image_stream_name:tag>.
----

//Similar procedure in images-imagestreams-remove-tag.adoc
