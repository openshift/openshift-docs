// Module included in the following assemblies:
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc


[id="defining-storage-classes_{context}"]
= Defining a storage class

`StorageClass` objects are currently a globally scoped object and must be
created by `cluster-admin` or `storage-admin` users.

ifndef::microshift,openshift-rosa[]
[IMPORTANT]
====
The Cluster Storage Operator might install a default storage class depending
on the platform in use. This storage class is owned and controlled by the
Operator. It cannot be deleted or modified beyond defining annotations
and labels. If different behavior is desired, you must define a custom
storage class.
====
endif::microshift,openshift-rosa[]
ifdef::openshift-rosa[]
[IMPORTANT]
====
The Cluster Storage Operator installs a default storage class. This storage class is owned and controlled by the Operator. It cannot be deleted or modified beyond defining annotations and labels. If different behavior is desired, you must define a custom storage class.
====
endif::openshift-rosa[]

The following sections describe the basic definition for a
`StorageClass` object and specific examples for each of the supported plugin types.
