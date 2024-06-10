:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-operating-system-issues"]
= Troubleshooting operating system issues
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-operating-system-issues

toc::[]

{product-title} runs on {op-system}. You can follow these procedures to troubleshoot problems related to the operating system.

// Investigating kernel crashes
include::modules/investigating-kernel-crashes.adoc[leveloffset=+1]

include::modules/troubleshooting-enabling-kdump.adoc[leveloffset=+2]

include::modules/troubleshooting-enabling-kdump-day-one.adoc[leveloffset=+2]

[id="testing-kdump-configuration"]
=== Testing the kdump configuration

ifdef::openshift-enterprise[]
See the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line_managing-monitoring-and-updating-the-kernel#testing-the-kdump-configuration_configuring-kdump-on-the-command-line[Testing the kdump configuration] section in the {op-system-base} documentation for kdump.
endif::[]

ifdef::openshift-origin[]
See the link:https://fedoraproject.org/wiki/How_to_use_kdump_to_debug_kernel_crashes#Step_2:_Capturing_the_Dump[Capturing the Dump] section in the {op-system-base} documentation for kdump.
endif::[]

[id="analyzing-core-dumps"]
=== Analyzing a core dump

ifdef::openshift-enterprise[]
See the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/analyzing-a-core-dump_managing-monitoring-and-updating-the-kernel[Analyzing a core dump] section in the {op-system-base} documentation for kdump.
endif::[]

ifdef::openshift-origin[]
See the link:https://fedoraproject.org/wiki/How_to_use_kdump_to_debug_kernel_crashes#Step_3:_Dump_Analysis[Dump Analysis] section in the {op-system-base} documentation for kdump.
endif::[]

[NOTE]
====
It is recommended to perform vmcore analysis on a separate {op-system-base} system.
====

[discrete]
[role="_additional-resources"]
[id="additional-resources_investigating-kernel-crashes"]
=== Additional resources
ifdef::openshift-origin[]
* link:https://docs.fedoraproject.org/en-US/fedora-coreos/debugging-kernel-crashes/[Fedora CoreOS Docs on debugging kernel crashes]
* link:https://fedoraproject.org/wiki/How_to_use_kdump_to_debug_kernel_crashes[Setting up kdump in Fedora]
endif::[]
ifdef::openshift-enterprise[]
* link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line_managing-monitoring-and-updating-the-kernel[Setting up kdump in RHEL]
endif::[]
* link:https://www.kernel.org/doc/html/latest/admin-guide/kdump/kdump.html[Linux kernel documentation for kdump]
* kdump.conf(5) — a manual page for the `/etc/kdump.conf` configuration file containing the full documentation of available options
* kexec(8) — a manual page for the `kexec` package
* link:https://access.redhat.com/site/solutions/6038[Red Hat Knowledgebase article] regarding kexec and kdump

include::modules/troubleshooting-debugging-ignition.adoc[leveloffset=+1]
