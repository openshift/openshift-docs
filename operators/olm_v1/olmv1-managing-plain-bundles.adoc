:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="olmv1-managing-plain-bundles"]
= Managing plain bundles in {olmv1} (Technology Preview)

:context: olmv1-managing-catalogs

toc::[]

In {olmv1-first}, a _plain bundle_ is a static collection of arbitrary Kubernetes manifests in YAML format. The experimental `olm.bundle.mediatype` property of the `olm.bundle` schema object differentiates a plain bundle (`plain+v0`) from a regular (`registry+v1`) bundle.

:FeatureName: {olmv1}
include::snippets/technology-preview.adoc[]

// For more information, see the [Plain Bundle Specification](https://github.com/operator-framework/rukpak/blob/main/docs/bundles/plain.md) in the RukPak repository.

As a cluster administrator, you can build and publish a file-based catalog that includes a plain bundle image by completing the following procedures:

. Build a plain bundle image.
. Create a file-based catalog.
. Add the plain bundle image to your file-based catalog.
. Build your catalog as an image.
. Publish your catalog image.

[role="_additional-resources"]
.Additional resources

* xref:../../operators/olm_v1/arch/olmv1-rukpak.adoc#olmv1-rukpak[RukPak component and packaging format]

[id="prerequisites_olmv1-plain-bundles"]
== Prerequisites

* Access to an {product-title} cluster using an account with `cluster-admin` permissions
+
--
include::snippets/olmv1-cli-only.adoc[]
--
* The `TechPreviewNoUpgrades` feature set enabled on the cluster
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters.
====
* The OpenShift CLI (`oc`) installed on your workstation
* The `opm` CLI installed on your workstation
* Docker or Podman installed on your workstation
* Push access to a container registry, such as link:https://quay.io[Quay]
* Kubernetes manifests for your bundle in a flat directory at the root of your project similar to the following structure:
+
.Example directory structure
[source,terminal]
----
manifests
├── namespace.yaml
├── service_account.yaml
├── cluster_role.yaml
├── cluster_role_binding.yaml
└── deployment.yaml
----


[role="_additional-resources"]
.Additional resources

* xref:../../nodes/clusters/nodes-cluster-enabling-features.adoc#nodes-cluster-enabling[Enabling features using feature gates]

// - Only the `redhat-operators` catalog source enabled on the cluster. This is a restriction during the Technology Preview release.

include::modules/olmv1-building-plain-image.adoc[leveloffset=+1]
include::modules/olmv1-creating-fbc.adoc[leveloffset=+1]
include::modules/olmv1-adding-plain-to-fbc.adoc[leveloffset=+1]
include::modules/olmv1-publishing-fbc.adoc[leveloffset=+1]