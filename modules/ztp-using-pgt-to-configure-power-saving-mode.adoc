// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-advanced-policy-config.adoc

:_module-type: PROCEDURE
[id="ztp-using-pgt-to-configure-power-saving-mode_{context}"]
= Configuring power saving mode using PolicyGenTemplate CRs

Follow this example to set power saving mode by updating the `workloadHints` fields in the generated `PerformanceProfile` CR for the reference configuration, based on the `PolicyGenTemplate` CR in the `group-du-sno-ranGen.yaml`.

The power saving mode balances reduced power consumption with increased latency.

.Prerequisites

* You enabled C-states and OS-controlled P-states in the BIOS.

.Procedure

. Update the `PolicyGenTemplate` entry for `PerformanceProfile` in the `group-du-sno-ranGen.yaml` reference file in `out/argocd/example/policygentemplates` as follows to configure power saving mode. It is recommended to configure the CPU governor for the power saving mode through the additional kernel arguments object.
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
         perPodPowerManagement: true
    [...]
    additionalKernelArgs:
       - [...]
       - "cpufreq.default_governor=schedutil" <1>
----
<1> The `schedutil` governor is recommended, however, other governors that can be used include `ondemand` and `powersave`.

. Commit the `PolicyGenTemplate` change in Git, and then push to the Git repository being monitored by the {ztp} Argo CD application.

.Verification

.  Select a worker node in your deployed cluster from the list of nodes identified by using the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Log in to the node by using the following command:
+
[source,terminal]
----
$ oc debug node/<node-name>
----
+
Replace `<node-name>` with the name of the node you want to verify the power state on.

. Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths as shown in the following example:
+
[source,terminal]
----
# chroot /host
----

. Run the following command to verify the applied power state:
+
[source,terminal]
----
# cat /proc/cmdline
----

.Expected output

* For power saving mode the `intel_pstate=passive`.
