// Module included in the following assemblies:
// * assembly/openshift_images/managing-image-streams.adoc

:_mod-docs-content-type: CONCEPT
[id="images-imagestream-specify-architecture_{context}"]
= Specifying architecture for --import-mode

You can swap your imported image stream between multi-architecture and single architecture by excluding or including the `--import-mode=` flag

.Procedure

* Run the following command to update your image stream from multi-architecture to single architecture by excluding the `--import-mode=` flag:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag> --from=<registry>/<project_name>/<image-name>
----

* Run the following command to update your image stream from single-architecture to multi-architecture:
+
[source,terminal]
----
$ oc import-image <multiarch-image-stream-tag>  --from=<registry>/<project_name>/<image-name> \
--import-mode='PreserveOriginal'
----