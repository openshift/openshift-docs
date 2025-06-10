// Module included in the following assemblies:
// * virt/nodes/virt-managing-node-labeling-obsolete-cpu-models.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-node-labeling-obsolete-cpu-models_{context}"]
= About node labeling for obsolete CPU models

The {VirtProductName} Operator uses a predefined list of obsolete CPU models to ensure that a node supports only valid CPU models for scheduled VMs.

By default, the following CPU models are eliminated from the list of labels generated for the node:

.Obsolete CPU models
[%collapsible]
====
----
"486"
Conroe
athlon
core2duo
coreduo
kvm32
kvm64
n270
pentium
pentium2
pentium3
pentiumpro
phenom
qemu32
qemu64
----
====

This predefined list is not visible in the `HyperConverged` CR. You cannot _remove_ CPU models from this list, but you can add to the list by editing the `spec.obsoleteCPUs.cpuModels` field of the `HyperConverged` CR.