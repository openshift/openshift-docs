// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-external-image-tags_{context}"]
= Adding tags for an external image

You can add tags for external images.

.Procedure

* Add tags pointing to internal or external images, by using the `oc tag` command for all tag-related operations:
+
[source,terminal]
----
$ oc tag <repository/image> <image-name:tag>
----
+
For example, this command maps the `docker.io/python:3.6.0` image to the `3.6` tag in the `python` image stream.
+
[source,terminal]
----
$ oc tag docker.io/python:3.6.0 python:3.6
----
+
.Example output
[source,terminal]
----
Tag python:3.6 set to docker.io/python:3.6.0.
----
+
If the external image is secured, you must create a secret with credentials for accessing that registry.
