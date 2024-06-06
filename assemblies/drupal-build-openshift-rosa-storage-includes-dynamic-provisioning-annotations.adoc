// Module included in the following assemblies
//
// * storage/dynamic-provisioning.adoc
// * post_installation_configuration/storage-configuration.adoc
// * microshift_storage/dynamic-provisioning-microshift.adoc


[id="storage-class-annotations_{context}"]
= Storage class annotations

To set a storage class as the cluster-wide default, add
the following annotation to your storage class metadata:

[source,yaml]
----
storageclass.kubernetes.io/is-default-class: "true"
----

For example:

[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
...
----

This enables any persistent volume claim (PVC) that does not specify a
specific storage class to automatically be provisioned through the
default storage class. However, your cluster can have more than one storage class, but only one of them can be the default storage class.

[NOTE]
====
The beta annotation `storageclass.beta.kubernetes.io/is-default-class` is
still working; however, it will be removed in a future release.
====

To set a storage class description, add the following annotation
to your storage class metadata:

[source,yaml]
----
kubernetes.io/description: My Storage Class Description
----

For example:

[source,yaml]
----
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    kubernetes.io/description: My Storage Class Description
...
----
