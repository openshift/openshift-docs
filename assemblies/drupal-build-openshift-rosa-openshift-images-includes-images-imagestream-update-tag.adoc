// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-update-tag_{context}"]
= Updating image stream tags

You can update a tag to reflect another tag in an image stream.

.Procedure

* Update a tag:
+
[source,terminal]
----
$ oc tag <image-name:tag> <image-name:latest>
----
+
For example, the following updates the `latest` tag to reflect the `3.6` tag in an image stream:
+
[source,terminal]
----
$ oc tag python:3.6 python:latest
----
+
.Example output
[source,terminal]
----
Tag python:latest set to python@sha256:438208801c4806548460b27bd1fbcb7bb188273d13871ab43f.
----
