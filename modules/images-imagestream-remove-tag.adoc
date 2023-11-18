// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-remove-tag_{context}"]
= Removing image stream tags

You can remove old tags from an image stream.

.Procedure

* Remove old tags from an image stream:
+
[source,terminal]
----
$ oc tag -d <image-name:tag>
----
+
For example:
+
[source,terminal]
----
$ oc tag -d python:3.6
----
+
.Example output
[source,terminal]
----
Deleted tag default/python:3.6
----
