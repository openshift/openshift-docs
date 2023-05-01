// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.adoc

:_module-type: PROCEDURE
[id="ztp-using-pgt-to-configure-high-performance-mode_{context}"]
= Configuring high-performance mode using PolicyGenTemplate CRs

Follow this example to set high performance mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

High performance mode provides ultra low latency at the highest power consumption.

.Prerequisites

* You have configured the BIOS with performance related settings by following the guidance in "Configuring host firmware for low latency and high performance".

.Procedure

. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates` as follows to set high-performance mode.
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
         highPowerConsumption: true
         perPodPowerManagement: false
----

. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.
