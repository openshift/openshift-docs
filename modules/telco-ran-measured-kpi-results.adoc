// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-du-overview.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-ran-measured-kpi-results_{context}"]
= KPI test results overview

All results are taken from 12-hour test runs.

Realtime kernel KPI test::
Workload nodes running the realtime kernel are validated to these performance KPIs:

* No `oslat` samples greater than 20µs.

* 99.9999% of `cyclictest` samples are less than 10µs. No samples above 20µs.

Non-realtime kernel KPI test::
The non-realtime kernel can be run with a reduced predictable latency target.
The following performance KPIs are validated:

* No `oslat` samples above 20µs.

[NOTE]
====
`cyclictest` tests are not applicable for non-realtime systems.
====

RFC2544 KPI test::
* Zero packet loss at 99.9% line rate (25 Gbps) for 512 byte frames.

* Packet latency is less than 30µs at 80% line rate for 512 byte frames over 12 hour test.

[NOTE]
====
The test application is the DPDK `testpmd` utility.
====

PTP network synchronization::
* The time offset for boundary and ordinary clock configurations, as measured at the follower port on the Intel E810-XXVDA4 (Salem Channel) NIC is less than 100 ns as indicated by the `openshift_ptp_offset_ns` metric.
