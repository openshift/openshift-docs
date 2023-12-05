// Module included in the following assemblies:
//
// * nodes/containers/nodes-containers-sysctls.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-sysctls-about_{context}"]
= About sysctls

In Linux, the sysctl interface allows an administrator to modify kernel parameters at runtime. Parameters are available from the `_/proc/sys/_` virtual process file system. The parameters cover various subsystems, such as:

- kernel (common prefix: `_kernel._`)
- networking (common prefix: `_net._`)
- virtual memory (common prefix: `_vm._`)
- MDADM (common prefix: `_dev._`)

More subsystems are described in link:https://www.kernel.org/doc/Documentation/sysctl/README[Kernel documentation].
To get a list of all parameters, run:

[source,terminal]
----
$ sudo sysctl -a
----