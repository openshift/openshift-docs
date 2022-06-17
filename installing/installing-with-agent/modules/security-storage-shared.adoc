// Module included in the following assemblies:
//
// * security/container_security/security-storage.adoc

[id="security-network-storage-shared_{context}"]
= Shared storage

For shared storage providers like NFS, the PV registers its
group ID (GID) as an annotation on the PV resource. Then, when the PV is claimed
by the pod, the annotated GID is added to the supplemental groups of the pod,
giving that pod access to the contents of the shared storage.
