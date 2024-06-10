:_mod-docs-content-type: ASSEMBLY
[id="creating-machineset-osp"]
= Creating a compute machine set on OpenStack
include::_attributes/common-attributes.adoc[]
:context: creating-machineset-osp

toc::[]

You can create a different compute machine set to serve a specific purpose in your {product-title} cluster on {rh-openstack-first}. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

include::modules/machineset-yaml-osp.adoc[leveloffset=+1]

include::modules/machineset-yaml-osp-sr-iov.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../../installing/installing_openstack/installing-openstack-nfv-preparing.adoc#installing-openstack-nfv-preparing[Preparing to install a cluster that uses SR-IOV or OVS-DPDK on OpenStack]

include::modules/machineset-yaml-osp-sr-iov-port-security.adoc[leveloffset=+1]

include::modules/machineset-creating.adoc[leveloffset=+1]

// Mothballed - re-add when available
// include::modules/machineset-osp-adding-bare-metal.adoc[leveloffset=+1]
