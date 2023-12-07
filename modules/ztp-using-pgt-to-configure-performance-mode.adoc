// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.adoc

:_module-type: PROCEDURE
[id="ztp-using-pgt-to-configure-performance-mode_{context}"]
= Configuring performance mode using PolicyGenTemplate CRs

Follow this example to set performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

Performance mode provides low latency at a relatively high power consumption.

.Prerequisites

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

.Procedure

. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates` as follows to set performance mode.
+
[source,yaml]
----
- fileName: PerformanceProfile.yaml
  policyName: "config-policy"
  metadata:
    [...]
  spec:
    [...]
    workloadHints:
         realTime: true
         highPowerConsumption: false
         perPodPowerManagement: false
----

. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.
