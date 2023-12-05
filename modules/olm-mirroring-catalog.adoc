// Module included in the following assemblies:
//
// * installing/disconnected_install/installing-mirroring-installation-images.adoc

:_mod-docs-content-type: CONCEPT
[id="olm-mirror-catalog_{context}"]
= Mirroring Operator catalogs for use with disconnected clusters

You can mirror the Operator contents of a Red Hat-provided catalog, or a custom catalog, into a container image registry using the `oc adm catalog mirror` command. The target registry must support link:https://docs.docker.com/registry/spec/manifest-v2-2/[Docker v2-2]. For a cluster on a restricted network, this registry can be one that the cluster has network access to, such as a mirror registry created during a restricted network cluster installation.

[IMPORTANT]
====
* The {product-registry} cannot be used as the target registry because it does not support pushing without a tag, which is required during the mirroring process.
* Running `oc adm catalog mirror` might result in the following error: `error: unable to retrieve source image`. This error occurs when image indexes include references to images that no longer exist on the image registry. Image indexes might retain older references to allow users running those images an upgrade path to newer points on the upgrade graph. As a temporary workaround, you can use the `--skip-missing` option to bypass the error and continue downloading the image index. For more information, see link:https://access.redhat.com/solutions/6975305[Service Mesh Operator mirroring failed].
====

The `oc adm catalog mirror` command also automatically mirrors the index image that is specified during the mirroring process, whether it be a Red Hat-provided index image or your own custom-built index image, to the target registry. You can then use the mirrored index image to create a catalog source that allows Operator Lifecycle Manager (OLM) to load the mirrored catalog onto your {product-title} cluster.
