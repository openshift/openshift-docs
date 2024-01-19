// Module included in the following assemblies:
// * virt/nodes/virt-managing-node-labeling-obsolete-cpu-models.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-node-labeling-cpu-features_{context}"]
= About node labeling for CPU features

Through the process of iteration, the base CPU features in the minimum CPU model are eliminated from the list of labels generated for the node.

For example:

* An environment might have two supported CPU models: `Penryn` and `Haswell`.

* If `Penryn` is specified as the CPU model for `minCPU`, each base CPU feature for `Penryn` is compared to the list of CPU features supported by `Haswell`.
+
.CPU features supported by `Penryn`
[%collapsible]
====
----
apic
clflush
cmov
cx16
cx8
de
fpu
fxsr
lahf_lm
lm
mca
mce
mmx
msr
mtrr
nx
pae
pat
pge
pni
pse
pse36
sep
sse
sse2
sse4.1
ssse3
syscall
tsc
----
====
+
.CPU features supported by `Haswell`
[%collapsible]
====
----
aes
apic
avx
avx2
bmi1
bmi2
clflush
cmov
cx16
cx8
de
erms
fma
fpu
fsgsbase
fxsr
hle
invpcid
lahf_lm
lm
mca
mce
mmx
movbe
msr
mtrr
nx
pae
pat
pcid
pclmuldq
pge
pni
popcnt
pse
pse36
rdtscp
rtm
sep
smep
sse
sse2
sse4.1
sse4.2
ssse3
syscall
tsc
tsc-deadline
x2apic
xsave
----
====

* If both `Penryn` and `Haswell` support a specific CPU feature, a label is not created for that feature. Labels are generated for CPU features that are supported only by `Haswell` and not by `Penryn`.
+
.Node labels created for CPU features after iteration
[%collapsible]
====
----
aes
avx
avx2
bmi1
bmi2
erms
fma
fsgsbase
hle
invpcid
movbe
pcid
pclmuldq
popcnt
rdtscp
rtm
sse4.2
tsc-deadline
x2apic
xsave
----
====
