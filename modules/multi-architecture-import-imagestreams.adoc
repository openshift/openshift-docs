//Module included in the following assemblies
//
//post_installation_configuration/multi-architecture-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="multi-architecture-import-imagestreams_{context}"]

= Importing manifest lists in image streams on your multi-architecture compute machines

On an {product-title} {product-version} cluster with multi-architecture compute machines, the image streams in the cluster do not import manifest lists automatically. You must manually change the default `importMode` option to the `PreserveOriginal` option in order to import the manifest list.

.Prerequisites

* You installed the {product-title} CLI (`oc`).

.Procedure

* The following example command shows how to patch the `ImageStream` cli-artifacts so that the `cli-artifacts:latest` image stream tag is imported as a manifest list.
+
[source,terminal]
----
$ oc patch is/cli-artifacts -n openshift -p '{"spec":{"tags":[{"name":"latest","importPolicy":{"importMode":"PreserveOriginal"}}]}}'
----

.Verification

* You can check that the manifest lists imported properly by inspecting the image stream tag. The following command will list the individual architecture manifests for a particular tag.
+
[source,terminal]
----
$ oc get istag cli-artifacts:latest -n openshift -oyaml
----

+
If the `dockerImageManifests` object is present, then the manifest list import was successful.

+
.Example output of the `dockerImageManifests` object
[source, yaml]
----
dockerImageManifests:
  - architecture: amd64
    digest: sha256:16d4c96c52923a9968fbfa69425ec703aff711f1db822e4e9788bf5d2bee5d77
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: arm64
    digest: sha256:6ec8ad0d897bcdf727531f7d0b716931728999492709d19d8b09f0d90d57f626
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: ppc64le
    digest: sha256:65949e3a80349cdc42acd8c5b34cde6ebc3241eae8daaeea458498fedb359a6a
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
  - architecture: s390x
    digest: sha256:75f4fa21224b5d5d511bea8f92dfa8e1c00231e5c81ab95e83c3013d245d1719
    manifestSize: 1252
    mediaType: application/vnd.docker.distribution.manifest.v2+json
    os: linux
----
