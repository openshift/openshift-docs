:_mod-docs-content-type: SNIPPET
.PerformanceProfile CR options for {sno} clusters
[cols=2*, width="90%", options="header"]
|====
|PerformanceProfile CR field
|Description

|`metadata.name`
a|Ensure that `name` matches the following fields set in related {ztp} custom resources (CRs):

* `include=openshift-node-performance-${PerformanceProfile.metadata.name}` in `TunedPerformancePatch.yaml`
* `name: 50-performance-${PerformanceProfile.metadata.name}` in `validatorCRs/informDuValidator.yaml`

|`spec.additionalKernelArgs`
|`"efi=runtime"` Configures UEFI secure boot for the cluster host.

|`spec.cpu.isolated`
a|Set the isolated CPUs. Ensure all of the Hyper-Threading pairs match.

[IMPORTANT]
====
The reserved and isolated CPU pools must not overlap and together must span all available cores. CPU cores that are not accounted for cause an undefined behaviour in the system.
====

|`spec.cpu.reserved`
|Set the reserved CPUs. When workload partitioning is enabled, system processes, kernel threads, and system container threads are restricted to these CPUs. All CPUs that are not isolated should be reserved.

|`spec.hugepages.pages`
a|* Set the number of huge pages (`count`)
* Set the huge pages size (`size`).
* Set `node` to the NUMA node where the `hugepages` are allocated (`node`)

|`spec.realTimeKernel`
|Set `enabled` to `true` to use the realtime kernel.

|`spec.workloadHints`
|Use `workloadHints` to define the set of top level flags for different type of workloads.
The example configuration configures the cluster for low latency and high performance.
|====
