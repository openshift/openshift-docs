:_mod-docs-content-type: ASSEMBLY
[id="nw-ovn-kubernetes-enabling-multicast"]
= Enabling multicast for a project
include::_attributes/common-attributes.adoc[]
:context: ovn-kubernetes-enabling-multicast

ifeval::["{product-version}" == "4.3"]
:bz:
endif::[]
ifeval::["{product-version}" == "4.4"]
:bz:
endif::[]
ifeval::["{product-version}" == "4.5"]
:bz:
endif::[]

toc::[]

ifdef::bz[]
[NOTE]
====
In {product-title} {product-version}, a bug prevents pods in the same namespace, but assigned to different nodes, from communicating over multicast. For more information, see link:https://bugzilla.redhat.com/show_bug.cgi?id=1843695[BZ#1843695].
====
endif::bz[]

include::modules/nw-about-multicast.adoc[leveloffset=+1]
include::modules/nw-enabling-multicast.adoc[leveloffset=+1]

ifdef::bz[]
:!bz:
endif::bz[]
