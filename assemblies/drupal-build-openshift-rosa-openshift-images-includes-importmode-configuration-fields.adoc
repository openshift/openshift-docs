// Module included in the following assemblies:
// * assembly/openshift_images/managing-image-streams.adoc

:_mod-docs-content-type: CONCEPT
[id="importmode-configuration-fields_{context}"]
= Configuration fields for --import-mode

The following table describes the options available for the `--import-mode=` flag:

[cols="3a,8a",options="header"]
|===
|Parameter |Description

| *Legacy* | The default option for `--import-mode`. When specified, the manifest list is discarded, and a single sub-manifest is imported. The platform is chosen in the following order of priority:

. Tag annotations
. Control plane architecture
. Linux/AMD64
. The first manifest in the list

| *PreserveOriginal* | When specified, the original manifest is preserved. For manifest lists, the manifest list and all of its sub-manifests are imported.

|===