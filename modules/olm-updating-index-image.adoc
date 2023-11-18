// Module included in the following assemblies:
//
// * operators/admin/olm-managing-custom-catalogs.adoc

ifdef::openshift-origin[]
:index-image: catalog
endif::[]
ifndef::openshift-origin[]
:index-image: redhat-operator-index
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="olm-updating-index-image_{context}"]
= Updating a SQLite-based index image

After configuring OperatorHub to use a catalog source that references a custom index image,
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
administrators with the `dedicated-admin` role
endif::openshift-dedicated,openshift-rosa[]
can keep the available Operators on their cluster up-to-date by adding bundle images to the index image.

You can update an existing index image using the `opm index add` command.

.Prerequisites

* You have installed the `opm` CLI.
* You have `podman` version 1.9.3+.
* An index image is built and pushed to a registry.
* You have an existing catalog source referencing the index image.

.Procedure

. Update the existing index by adding bundle images:
+
[source,terminal]
----
$ opm index add \
    --bundles <registry>/<namespace>/<new_bundle_image>@sha256:<digest> \//<1>
    --from-index <registry>/<namespace>/<existing_index_image>:<existing_tag> \//<2>
    --tag <registry>/<namespace>/<existing_index_image>:<updated_tag> \//<3>
    --pull-tool podman //<4>
----
<1> The `--bundles` flag specifies a comma-separated list of additional bundle images to add to the index.
<2> The `--from-index` flag specifies the previously pushed index.
<3> The `--tag` flag specifies the image tag to apply to the updated index image.
<4> The `--pull-tool` flag specifies the tool used to pull container images.
+
where:
+
--
`<registry>`:: Specifies the hostname of the registry, such as `quay.io` or `mirror.example.com`.
`<namespace>`:: Specifies the namespace of the registry, such as `ocs-dev` or `abc`.
`<new_bundle_image>`:: Specifies the new bundle image to add to the registry, such as `ocs-operator`.
`<digest>`:: Specifies the SHA image ID, or digest, of the bundle image, such as `c7f11097a628f092d8bad148406aa0e0951094a03445fd4bc0775431ef683a41`.
`<existing_index_image>`:: Specifies the previously pushed image, such as `abc-redhat-operator-index`.
`<existing_tag>`:: Specifies a previously pushed image tag, such as `pass:a[{product-version}]`.
`<updated_tag>`:: Specifies the image tag to apply to the updated index image, such as `pass:a[{product-version}].1`.
--
+
.Example command
[source,terminal,subs="attributes+"]
----
$ opm index add \
    --bundles quay.io/ocs-dev/ocs-operator@sha256:c7f11097a628f092d8bad148406aa0e0951094a03445fd4bc0775431ef683a41 \
    --from-index mirror.example.com/abc/abc-redhat-operator-index:{product-version} \
    --tag mirror.example.com/abc/abc-redhat-operator-index:{product-version}.1 \
    --pull-tool podman
----

. Push the updated index image:
+
[source,terminal]
----
$ podman push <registry>/<namespace>/<existing_index_image>:<updated_tag>
----

. After Operator Lifecycle Manager (OLM) automatically polls the index image referenced in the catalog source at its regular interval, verify that the new packages are successfully added:
+
[source,terminal]
----
$ oc get packagemanifests -n openshift-marketplace
----

:!index-image:
