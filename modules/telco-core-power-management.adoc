// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-core-ref-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-power-management_{context}"]
= Power Management

New in this release::
* You can specify a maximum latency that is C-state for a low latency pod when using per-pod power management. Previously, C-states could only be disabled completely on a per pod basis.

Description::

The https://docs.openshift.com/container-platform/4.14/rest_api/node_apis/performanceprofile-performance-openshift-io-v2.html#spec-workloadhints[Performance Profile] can be used to configure a cluster in a high power, low power or mixed (https://docs.openshift.com/container-platform/4.14/scalability_and_performance/cnf-low-latency-tuning.html#node-tuning-operator-pod-power-saving-config_cnf-master[per-pod power management]) mode. The choice of power mode depends on the characteristics of the workloads running on the cluster particularly how sensitive they are to latency.

Limits and requirements::
* Power configuration relies on appropriate BIOS configuration, for example, enabling C-states and P-states. Configuration varies between hardware vendors.


Engineering considerations::
* Latency: To ensure that latency-sensitive workloads meet their requirements, you will need either a high-power configuration or a per-pod power management configuration. Per-pod power management is only available for `Guaranteed` QoS Pods with dedicated pinned CPUs.
