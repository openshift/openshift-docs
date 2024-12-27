// Module included in the following assemblies:
//
// * hardware_enablement/kmm-kernel-module-management.adoc

:_mod-docs-content-type: CONCEPT
[id="kmm-hub-kmm-hub_{context}"]
= KMM-Hub

The KMM project provides KMM-Hub, an edition of KMM dedicated to hub clusters. KMM-Hub monitors all kernel versions running on the spokes and determines the nodes on the cluster that should receive a kernel module.

KMM-Hub runs all compute-intensive tasks such as image builds and kmod signing, and prepares the trimmed-down `Module` to be transferred to the spokes through RHACM.

[NOTE]
====
KMM-Hub cannot be used to load kernel modules on the hub cluster. Install the regular edition of KMM to load kernel modules.
====
