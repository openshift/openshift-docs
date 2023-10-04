// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-core-ref-components.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-cpu-partitioning-performance-tune_{context}"]
= CPU partitioning and performance tuning

New in this release::

Open vSwitch (OVS) is removed from CPU partitioning. OVS manages its cpuset dynamically to automatically adapt to network traffic needs. Users no longer need to reserve additional CPUs for handling high network throughput on the primary container network interface (CNI). There is no impact on the configuration needed to benefit from this change.

Description::

CPU partitioning allows for the separation of sensitive workloads from generic purposes, auxiliary processes, interrupts, and driver work queues to achieve improved performance and latency. The CPUs allocated to those auxiliary processes are referred to as `reserved` in the following sections. In hyperthreaded systems, a CPU is one hyperthread.
+
For more information, see https://docs.openshift.com/container-platform/latest/scalability_and_performance/cnf-low-latency-tuning.html#cnf-cpu-infra-container_cnf-master[Restricting CPUs for infra and application containers].
+
Configure system level performance.
For recommended settings, see link:https://docs.openshift.com/container-platform/latest/scalability_and_performance/ztp_far_edge/ztp-reference-cluster-configuration-for-vdu.html#ztp-du-configuring-host-firmware-requirements_sno-configure-for-vdu[Configuring host firmware for low latency and high performance].

Limits and requirements::
* The operating system needs a certain amount of CPU to perform all the support tasks including kernel networking.
** A system with just user plane networking applications (DPDK) needs at least one Core (2 hyperthreads when enabled) reserved for the operating system and the infrastructure components.
* A system with Hyper-Threading enabled must always put all core sibling threads to the same pool of CPUs.
* The set of reserved and isolated cores must include all CPU cores.
* Core 0 of each NUMA node must be included in the reserved CPU set.
* Isolated cores might be impacted by interrupts. The following annotations must be attached to the pod if guaranteed QoS pods require full use of the CPU:
+
----
cpu-load-balancing.crio.io: "disable"
cpu-quota.crio.io: "disable"
irq-load-balancing.crio.io: "disable"
----
* When per-pod power management is enabled with `PerformanceProfile.workloadHints.perPodPowerManagement` the following annotations must also be attached to the pod if guaranteed QoS pods require full use of the CPU:
+
----
cpu-c-states.crio.io: "disable"
cpu-freq-governor.crio.io: "performance"
----

Engineering considerations::
* The minimum reserved capacity (`systemReserved`) required can be found by following the guidance in  link:https://access.redhat.com/solutions/5843241["Which amount of CPU and memory are recommended to reserve for the system in OCP 4 nodes?"]
* The actual required reserved CPU capacity depends on the cluster configuration and workload attributes.
* This reserved CPU value must be rounded up to a full core (2 hyper-thread) alignment.
* Changes to the CPU partitioning will drain and reboot the nodes in the MCP.
* The reserved CPUs reduce the pod density, as the reserved CPUs are removed from the allocatable capacity of the OpenShift node.
* The real-time workload hint should be enabled if the workload is real-time capable.
* Hardware without Interrupt Request (IRQ) affinity support will impact isolated CPUs. To ensure that pods with guaranteed CPU QoS have full use of allocated CPU, all hardware in the server must support IRQ affinity.
