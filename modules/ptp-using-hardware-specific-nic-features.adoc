// Module included in the following assemblies:
//
// * networking/ptp/configuring-ptp.adoc

:_mod-docs-content-type: CONCEPT
[id="ptp-using-hardware-specific-nic-features_{context}"]
= Using hardware-specific NIC features with the PTP Operator

NIC hardware with built-in PTP capabilities sometimes require device-specific configuration.
You can use hardware-specific NIC features for supported hardware with the PTP Operator by configuring a plugin in the `PtpConfig` custom resource (CR).
The `linuxptp-daemon` service uses the named parameters in the `plugin` stanza to start `linuxptp` processes (`ptp4l` and `phc2sys`) based on the specific hardware configuration.

[IMPORTANT]
====
In {product-title} {product-version}, the Intel E810 NIC is supported with a `PtpConfig` plugin.
====
