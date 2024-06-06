// Module included in the following assemblies:
//
// * nodes/nodes-containers-volumes.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-volumes-about_{context}"]
= Understanding volumes

Volumes are mounted file systems available to pods and their
containers which may be backed by a number of host-local or network attached
storage endpoints. Containers are not persistent by default; on restart, their contents are
cleared.

To ensure that the file system on the volume contains no errors and, if errors
are present, to repair them when possible, {product-title} invokes the `fsck`
utility prior to the `mount` utility. This occurs when either adding a volume or
updating an existing volume.

The simplest volume type is `emptyDir`, which is a temporary directory on a
single machine. Administrators may also allow you to request a persistent volume that is automatically attached
to your pods.

[NOTE]
====
`emptyDir` volume storage may be restricted by a quota based on the pod's
FSGroup, if the FSGroup parameter is enabled by your cluster administrator.
====

