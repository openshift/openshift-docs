// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc

:_mod-docs-content-type: CONCEPT
[id="about_{context}"]
= About dynamic provisioning

The `StorageClass` resource object describes and classifies storage that can
be requested, as well as provides a means for passing parameters for
dynamically provisioned storage on demand. `StorageClass` objects can also
serve as a management mechanism for controlling different levels of
storage and access to the storage. Cluster Administrators (`cluster-admin`)
 or Storage Administrators (`storage-admin`) define and create the
`StorageClass` objects that users can request without needing any detailed
knowledge about the underlying storage volume sources.

The {product-title} persistent volume framework enables this functionality
and allows administrators to provision a cluster with persistent storage.
The framework also gives users a way to request those resources without
having any knowledge of the underlying infrastructure.

Many storage types are available for use as persistent volumes in
{product-title}. While all of them can be statically provisioned by an
administrator, some types of storage are created dynamically using the
built-in provider and plugin APIs.
