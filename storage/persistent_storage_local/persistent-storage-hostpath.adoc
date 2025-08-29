:_mod-docs-content-type: ASSEMBLY
[id="persistent-storage-using-hostpath"]
= Persistent storage using hostPath
include::_attributes/common-attributes.adoc[]
:context: persistent-storage-hostpath

toc::[]

A hostPath volume in an {product-title} cluster mounts a file or directory from the host node's filesystem into your pod. Most pods will not need a hostPath volume, but it does offer a quick option for testing should an application require it.

[IMPORTANT]
====
The cluster administrator must configure pods to run as privileged. This grants access to pods in the same node.
====

include::modules/persistent-storage-hostpath-about.adoc[leveloffset=+1]
include::modules/persistent-storage-hostpath-static-provisioning.adoc[leveloffset=+1]
include::modules/persistent-storage-hostpath-pod.adoc[leveloffset=+1]
