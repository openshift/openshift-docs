// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-periodic-import-list_{context}"]
= Configuring periodic importing of manifest lists

To periodically re-import a manifest list, you can use the `--scheduled` flag.

.Procedure

* Set the image stream to periodically update the manifest list by entering the following command:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --scheduled=true
----