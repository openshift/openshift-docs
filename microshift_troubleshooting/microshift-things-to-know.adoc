:_mod-docs-content-type: ASSEMBLY
[id="microshift-things-to-know"]
= Responsive restarts and security certificates
include::_attributes/attributes-microshift.adoc[]
:context: microshift-configuring

toc::[]

{product-title} responds to system configuration changes and restarts after alterations are detected, including IP address changes, clock adjustments, and security certificate age.

[id="microshift-ip-address-clock-changes_{context}"]
== IP address changes or clock adjustments

{microshift-short} depends on device IP addresses and system-wide clock settings to remain consistent during its runtime. However, these settings may occasionally change on edge devices, such as DHCP or Network Time Protocol (NTP) updates.

When such changes occur, some {microshift-short} components may stop functioning properly. To mitigate this situation, {microshift-short} monitors the IP address and system time and restarts if either setting change is detected.

The threshold for clock changes is a time adjustment of greater than 10 seconds in either direction. Smaller drifts on regular time adjustments performed by the Network Time Protocol (NTP) service do not cause a restart.

include::modules/microshift-certificate-lifetime.adoc[leveloffset=+1]