:_mod-docs-content-type: ASSEMBLY
[id="virt-vm-control-plane-tuning"]
= Virtual machine control plane tuning
include::_attributes/common-attributes.adoc[]
:context: virt-control-plane-tuning

toc::[]

{VirtProductName} offers the following tuning options at the control-plane level:

* The `highBurst` profile, which uses fixed `QPS` and `burst` rates, to create hundreds of virtual machines (VMs) in one batch
* Migration setting adjustment based on workload type

// this module commented out until jsonpatch is supported or this becomes a TP or DP
// include::modules/virt-configuring-rate-limiters.adoc[leveloffset=+1]

include::modules/virt-configuring-highburst-profile.adoc[leveloffset=+1]