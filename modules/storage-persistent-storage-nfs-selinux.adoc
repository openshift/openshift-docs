// Module included in the following assemblies:
//
// * storage/persistent_storage/persistent-storage-nfs.adoc

:_mod-docs-content-type: PROCEDURE
[id="nfs-selinux_{context}"]
= SELinux

{op-system-base-full} and {op-system-first} systems are configured to use SELinux on remote NFS servers by default.

For non-{op-system-base} and non-{op-system} systems, SELinux does not allow writing from a pod to a remote NFS server. The NFS volume mounts correctly but it is read-only. You will need to enable the correct SELinux permissions by using the following procedure.

.Prerequisites

* The `container-selinux` package must be installed. This package provides the `virt_use_nfs` SELinux boolean.

.Procedure

* Enable the `virt_use_nfs` boolean using the following command. The `-P` option makes this boolean persistent across reboots.
+
[source,terminal]
----
# setsebool -P virt_use_nfs 1
----
