// Module included in the following assemblies:
//
// * networking/ptp/about-ptp.adoc

:_mod-docs-content-type: CONCEPT
[id="ptp-linuxptp-introduction_{context}"]
= Overview of linuxptp and gpsd in {product-title} nodes

{product-title} uses the PTP Operator with `linuxptp` and `gpsd` packages for high precision network synchronization.
The `linuxptp` package provides tools and daemons for PTP timing in networks.
Cluster hosts with Global Navigation Satellite System (GNSS) capable NICs use `gpsd` to interface with GNSS clock sources.

The `linuxptp` package includes the `ts2phc`, `pmc`, `ptp4l`, and `phc2sys` programs for system clock synchronization.

ts2phc:: `ts2phc` synchronizes the PTP hardware clock (PHC) across PTP devices with a high degree of precision.
`ts2phc` is used in grandmaster clock configurations.
It receives the precision timing signal a high precision clock source such as Global Navigation Satellite System (GNSS).
GNSS provides an accurate and reliable source of synchronized time for use in large distributed networks.
GNSS clocks typically provide time information with a precision of a few nanoseconds.
+
The `ts2phc` system daemon sends timing information from the grandmaster clock to other PTP devices in the network by reading time information from the grandmaster clock and converting it to PHC format.
PHC time is used by other devices in the network to synchronize their clocks with the grandmaster clock.

pmc:: `pmc` implements a PTP management client (`pmc`) according to IEEE standard 1588.1588.
`pmc` provides basic management access for the `ptp4l` system daemon.
`pmc` reads from standard input and sends the output over the selected transport, printing any replies it receives.

ptp4l:: `ptp4l` implements the PTP boundary clock and ordinary clock and runs as a system daemon.
`ptp4l` does the following:
* Synchronizes the PHC to the source clock with hardware time stamping
* Synchronizes the system clock to the source clock with software time stamping

phc2sys:: `phc2sys` synchronizes the system clock to the PHC on the network interface controller (NIC).
The `phc2sys` system daemon continuously monitors the PHC for timing information.
When it detects a timing error, the PHC corrects the system clock.

The `gpsd` package includes the `ubxtool`, `gspipe`, `gpsd`, programs for GNSS clock synchronization with the host clock.

ubxtool:: `ubxtool` CLI allows you to communicate with a u-blox GPS system. The `ubxtool` CLI uses the u-blox binary protocol to communicate with the GPS.

gpspipe:: `gpspipe` connects to `gpsd` output and pipes it to `stdout`.

gpsd:: `gpsd` is a service daemon that monitors one or more GPS or AIS receivers connected to the host.
