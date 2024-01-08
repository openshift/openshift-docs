// Module included in the following assemblies:
// * openshift_images/tagging-images

:_mod-docs-content-type: PROCEDURE
[id="images-remove-tag-imagestream_{context}"]
= Removing tags from image streams

You can remove tags from an image stream.

.Procedure

* To remove a tag completely from an image stream run:
+
[source,terminal]
----
$ oc delete istag/ruby:latest
----
+
or:
+
[source,terminal]
----
$ oc tag -d ruby:latest
----
