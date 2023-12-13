// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-ssl-import-list_{context}"]
= Configuring SSL/TSL when importing manifest lists

To configure SSL/TSL when importing a manifest list, you can use the `--insecure` flag.

.Procedure

* Set `--insecure=true` so that importing a manifest list skips SSL/TSL verification. For example:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag> --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal' --insecure=true
----