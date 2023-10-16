// Module included in the following assemblies:
//
// * operators/understanding/olm-packaging-format.adoc

[id="olm-fb-catalogs-guidelines_{context}"]
= Guidelines

Consider the following guidelines when maintaining file-based catalogs.

[id="olm-fb-catalogs-immutable_{context}"]
== Immutable bundles

The general advice with Operator Lifecycle Manager (OLM) is that bundle images and their metadata should be treated as immutable.

If a broken bundle has been pushed to a catalog, you must assume that at least one of your users has upgraded to that bundle. Based on that assumption, you must release another bundle with an upgrade edge from the broken bundle to ensure users with the broken bundle installed receive an upgrade. OLM will not reinstall an installed bundle if the contents of that bundle are updated in the catalog.

However, there are some cases where a change in the catalog metadata is preferred:

* Channel promotion: If you already released a bundle and later decide that you would like to add it to another channel, you can add an entry for your bundle in another `olm.channel` blob.
* New upgrade edges: If you release a new `1.2.z` bundle version, for example `1.2.4`, but `1.3.0` is already released, you can update the catalog metadata for `1.3.0` to skip `1.2.4`.

[id="olm-fb-catalogs-source-control_{context}"]
== Source control

Catalog metadata should be stored in source control and treated as the source of truth. Updates to catalog images should include the following steps:

. Update the source-controlled catalog directory with a new commit.
. Build and push the catalog image. Use a consistent tagging taxonomy, such as `:latest` or `:<target_cluster_version>`, so that users can receive updates to a catalog as they become available.
