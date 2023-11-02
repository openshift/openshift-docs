:_mod-docs-content-type: ASSEMBLY
[id="virt-using-huge-pages-with-vms"]
= Using huge pages with virtual machines
include::_attributes/common-attributes.adoc[]
:context: virt-using-huge-pages-with-vms

toc::[]

You can use huge pages as backing memory for virtual machines in your cluster.

== Prerequisites

* Nodes must have xref:../../../scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc#configuring-huge-pages_huge-pages[pre-allocated huge pages configured].


include::modules/what-huge-pages-do.adoc[leveloffset=+1]

include::modules/virt-configuring-huge-pages-for-vms.adoc[leveloffset=+1]
