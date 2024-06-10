// Module included in the following assemblies:
// * assembly/openshift_images/managing-image-streams.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-imagestream-import-images-private-registry_{context}"]
= Importing images and image streams from private registries

An image stream can be configured to import tag and image metadata from private image registries requiring authentication. This procedures applies if you change the registry that the Cluster Samples Operator uses to pull content from to something other than link:https://registry.redhat.io[registry.redhat.io].

[NOTE]
====
When importing from insecure or secure registries, the registry URL defined in the secret must include the `:80` port suffix or the secret is not used when attempting to import from the registry.
====

.Procedure

. You must create a `secret` object that is used to store your credentials by entering the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> --from-file=.dockerconfigjson=<file_absolute_path> --type=kubernetes.io/dockerconfigjson
----
+
. After the secret is configured, create the new image stream or enter the `oc import-image` command:
+
[source,terminal]
----
$ oc import-image <imagestreamtag> --from=<image> --confirm
----
+
During the import process, {product-title} picks up the secrets and provides them to the remote party.
