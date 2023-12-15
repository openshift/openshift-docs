// Module included in the following assemblies:
//
// * networking/ptp/configuring-ptp.adoc

:_mod-docs-content-type: REFERENCE
[id="nw-columbiaville-ptp-config-refererence_{context}"]
= Intel Columbiaville E800 series NIC as PTP ordinary clock reference

The following table describes the changes that you must make to the reference PTP configuration to use Intel Columbiaville E800 series NICs as ordinary clocks. Make the changes in a `PtpConfig` custom resource (CR) that you apply to the cluster.

.Recommended PTP settings for Intel Columbiaville NIC
[options="header"]
|====
|PTP configuration|Recommended setting
|`phc2sysOpts`|`-a -r -m -n 24 -N 8 -R 16`
|`tx_timestamp_timeout`|`50`
|`boundary_clock_jbod`|`0`
|====

[NOTE]
====
For `phc2sysOpts`, `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics.
====
