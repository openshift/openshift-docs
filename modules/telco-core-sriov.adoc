// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-core-ref-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-sriov_{context}"]
= SR-IOV

New in this release::

Not applicable

Description::

SR-IOV enables physical network interfaces (PFs) to be divided into multiple virtual functions (VFs). VFs can then be assigned to multiple pods to achieve higher throughput performance while keeping the pods isolated. The SR-IOV Network Operator provisions and manages SR-IOV CNI, network device plugin, and other components of the SR-IOV stack.

Limits and requirements::

* The network interface controllers supported are listed in https://docs.openshift.com/container-platform/4.14/networking/hardware_networks/about-sriov.html#nw-sriov-supported-platforms_about-sriov[OCP supported SR-IOV devices]
* SR-IOV and IOMMU enablement in BIOS: The SR-IOV Network Operator automatically enables IOMMU on the kernel command line.
* SR-IOV VFs do not receive link state updates from PF. If link down detection is needed, it must be done at the protocol level.

Engineering considerations::
* SR-IOV interfaces in `vfio` mode are typically used to enable additional secondary networks for applications that require high throughput or low latency.
