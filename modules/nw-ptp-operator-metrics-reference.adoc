// Module included in the following assemblies:
//
// * networking/ptp/using-ptp-events.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-ptp-operator-metrics-reference_{context}"]
= PTP fast event metrics reference

The following table describes the PTP fast events metrics that are available from cluster nodes where the `linuxptp-daemon` service is running.

[NOTE]
====
Some of the following metrics are applicable for PTP grandmaster clocks (T-GM) only.
====

.PTP fast event metrics
[cols="1,4,3", options="header"]
|====
|Metric
|Description
|Example

|`openshift_ptp_clock_class`
|Returns the PTP clock class for the interface.
Possible values for PTP clock class are `6` (`LOCKED`), `7` (`HOLDOVER` within specification), `140` (`HOLDOVER` outside specification), and `248` (`FREERUN`).
Applicable to T-GM clocks only.
|`openshift_ptp_clock_class {node="compute-1.example.com", process="ptp4l"} 6`

|`openshift_ptp_clock_state`
|Returns the current PTP clock state for the interface.
Possible values for PTP clock state are `FREERUN`, `LOCKED`, or `HOLDOVER`.
|`openshift_ptp_clock_state {iface="CLOCK_REALTIME", node="compute-1.example.com", process="phc2sys"} 1`

|`openshift_ptp_delay_ns`
|Returns the delay in nanoseconds between the primary clock sending the timing packet and the secondary clock receiving the timing packet.
|`openshift_ptp_delay_ns {from="master", iface="ens2fx", node="compute-1.example.com", process="ts2phc"} 0`

|`openshift_ptp_frequency_adjustment_ns`
|Returns the frequency adjustment in nanoseconds between 2 PTP clocks.
For example, between the upstream clock and the NIC, between the system clock and the NIC, or between the PTP hardware clock (`phc`) and the NIC.
Applicable to T-GM clocks only.
|`openshift_ptp_frequency_adjustment_ns {from="phc", iface="CLOCK_REALTIME", node="compute-1.example.com", process="phc2sys"} -6768`

|`openshift_ptp_interface_role`
|Describes the configured PTP clock role for the interface.
Possible values are 0 (`PASSIVE`), 1 (`SLAVE`), 2 (`MASTER`), 3 (`FAULTY`), 4 (`UNKNOWN`), or 5 (`LISTENING`).

|`openshift_ptp_interface_role {iface="ens2f0", node="compute-1.example.com", process="ptp4l"} 2`

|`openshift_ptp_max_offset_ns`
|Returns the maximum offset in nanoseconds between 2 clocks or interfaces.
For example, between the upstream GNSS clock and the NIC (`ts2phc`), or between the PTP hardware clock (`phc`) and the system clock (`phc2sys`).
Applicable to T-GM clocks only.
|`openshift_ptp_max_offset_ns {from="master", iface="ens2fx", node="compute-1.example.com", process="ts2phc"} 1.038099569e+09`

|`openshift_ptp_offset_ns`
|Returns the offset in nanoseconds between the DPLL clock or the GNSS clock source and the NIC hardware clock.
Applicable to T-GM clocks only.
|`openshift_ptp_offset_ns {from="phc", iface="CLOCK_REALTIME", node="compute-1.example.com", process="phc2sys"} -9`

|`openshift_ptp_process_restart_count`
|Returns a count of the number of times the `ptp4l` process was restarted.
|`openshift_ptp_process_restart_count {config="ptp4l.0.config", node="compute-1.example.com",process="phc2sys"} 1`

|`openshift_ptp_process_status`
|Returns a status code that shows whether the PTP process is running or not.
|`openshift_ptp_process_status {config="ptp4l.0.config", node="compute-1.example.com",process="phc2sys"} 1`

|`openshift_ptp_threshold`
a|Returns values for `HoldOverTimeout`, `MaxOffsetThreshold`, and `MinOffsetThreshold`.

* `holdOverTimeout` is the time value in seconds before the PTP clock event state changes to `FREERUN` when the PTP master clock is disconnected.
* `maxOffsetThreshold` and `minOffsetThreshold` are offset values in nanoseconds that compare against the values for `CLOCK_REALTIME` (`phc2sys`) or master offset (`ptp4l`) values that you configure in the `PtpConfig` CR for the NIC.
|`openshift_ptp_threshold {node="compute-1.example.com", profile="grandmaster", threshold="HoldOverTimeout"} 5`
|====
