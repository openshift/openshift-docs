// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-design-spec.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-ref-eng-usecase-model_{context}"]
= Engineering Considerations common use model

The following engineering considerations are relevant for the common use model.

Worker nodes::

* Worker nodes run on Intel 3rd Generation Xeon (IceLake) processors or newer. Alternatively, if using Skylake or earlier processors, the mitigations for silicon security vulnerabilities such as Spectre must be disabled; failure to do so may result in a significant 40 percent decrease in transaction performance.

* IRQ Balancing is enabled on worker nodes. The `PerformanceProfile` sets `globallyDisableIrqLoadBalancing: false`. Guaranteed QoS Pods are annotated to ensure isolation as described in "CPU partitioning and performance tuning" subsection in "Reference core design components" section.

All nodes::

* Hyper-Threading is enabled on all nodes
* CPU architecture is `x86_64` only
* Nodes are running the stock (non-RT) kernel
* Nodes are not configured for workload partitioning

The balance of node configuration between power management and maximum performance varies between `MachineConfigPools` in the cluster. This configuration is consistent for all nodes within a `MachineConfigPool`.

CPU partitioning::

CPU partitioning is configured using the PerformanceProfile and applied on a per `MachineConfigPool` basis. See the "CPU partitioning and performance tuning" subsection in "Reference core design components".