// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.adoc

:_module-type: PROCEDURE
[id="ztp-using-pgt-to-maximize-power-savings-mode_{context}"]
= Maximizing power savings

Limiting the maximum CPU frequency is recommended to achieve maximum power savings.
Enabling C-states on the non-critical workload CPUs without restricting the maximum CPU frequency negates much of the power savings by boosting the frequency of the critical CPUs.

Maximize power savings by updating the `sysfs` plugin fields, setting an appropriate value for `max_perf_pct` in the `TunedPerformancePatch` CR for the reference configuration. This example based on the `group-du-sno-ranGen.yaml` describes the procedure to follow to restrict the maximum CPU frequency.

.Prerequisites

* You have configured power savings mode as described in "Using PolicyGenTemplate CRs to configure power savings mode".

.Procedure

. Update the `PolicyGenTemplate` entry for `TunedPerformancePatch` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates`. To maximize power savings, add `max_perf_pct` as shown in the following example:
+
[source,yaml]
----
- fileName: TunedPerformancePatch.yaml
      policyName: "config-policy"
      spec:
        profile:
          - name: performance-patch
            data: |
              [...]
              [sysfs]
              /sys/devices/system/cpu/intel_pstate/max_perf_pct=<x> <1>
----
+
<1> 	The `max_perf_pct` controls the maximum frequency the `cpufreq` driver is allowed to set as a percentage of the maximum supported CPU frequency. This value applies to all CPUs. You can check the maximum supported frequency in `/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq`. As a starting point, you can use a percentage that caps all CPUs at the `All Cores Turbo` frequency. The `All Cores Turbo` frequency is the frequency that all cores will run at when the cores are all fully occupied.
+
[NOTE]
====
To maximize power savings, set a lower value. Setting a lower value for `max_perf_pct` limits the maximum CPU frequency, thereby reducing power consumption, but also potentially impacting performance. Experiment with different values and monitor the system's performance and power consumption to find the optimal setting for your use-case.
====

. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.
