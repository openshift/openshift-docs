// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-du-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-sr-iov-operator_{context}"]
= SR-IOV Operator

New in this release::
* No reference design updates in this release

Description::
The SR-IOV Operator provisions and configures the SR-IOV CNI and device plugins.
Both `netdevice` (kernel VFs) and `vfio` (DPDK) devices are supported.

Engineering considerations::
* Customer variation on the configuration and number of `SriovNetwork` and `SriovNetworkNodePolicy` custom resources (CRs) is expected.

* IOMMU kernel command line settings are applied with a `MachineConfig` CR at install time. This ensures that the `SriovOperator` CR does not cause a reboot of the node when adding them.
