// Module included in the following assemblies:
//
// *

:_mod-docs-content-type: REFERENCE
[id="networking-crs_{context}"]
= Networking reference CRs

.Networking CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Optional,New in this release
Baseline,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-network-yaml[Network.yaml],No,No
Baseline,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-networkattachmentdefinition-yaml[networkAttachmentDefinition.yaml],Yes,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovsubscriptionns-yaml[SriovSubscriptionNS.yaml],No,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovsubscriptionopergroup-yaml[SriovSubscriptionOperGroup.yaml],No,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovsubscription-yaml[SriovSubscription.yaml],No,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovoperatorconfig-yaml[SriovOperatorConfig.yaml],No,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovnetworknodepolicy-yaml[sriovNetworkNodePolicy.yaml],No,No
SR-IOV Network Operator,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-sriovnetwork-yaml[sriovNetwork.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-metallbns-yaml[metallbNS.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-metallbopergroup-yaml[metallbOperGroup.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-metallbsubscription-yaml[metallbSubscription.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-metallb-yaml[metallb.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-bgp-peer-yaml[bgp-peer.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-bfd-profile-yaml[bfd-profile.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-addr-pool-yaml[addr-pool.yaml],No,No
Load balancer,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-bgp-advr-yaml[bgp-advr.yaml],No,No
Multus - Tap CNI for rootless DPDK pod,xref:../../telco_ref_design_specs/ran/telco-ran-ref-du-crs.adoc#ztp-mc_rootless_pods_selinux-yaml[mc_rootless_pods_selinux.yaml],Yes,No
|====
