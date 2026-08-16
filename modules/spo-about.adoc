// Module included in the following assemblies:
//
// * security/security_profiles_operator/spo-understanding.adoc

:_mod-docs-content-type: CONCEPT
[id="spo-about_{context}"]
= About Security Profiles

Security profiles can increase security at the container level in your cluster.

Seccomp security profiles list the syscalls a process can make. Permissions are broader than SELinux, enabling users to restrict operations system-wide, such as `write`.

SELinux security profiles provide a label-based system that restricts the access and usage of processes, applications, or files in a system. All files in an environment have labels that define permissions. SELinux profiles can define access within a given structure, such as directories.