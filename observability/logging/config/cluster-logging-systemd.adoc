:_mod-docs-content-type: ASSEMBLY
:context: cluster-logging-systemd
[id="cluster-logging-systemd"]
= Configuring systemd-journald and Fluentd
include::_attributes/common-attributes.adoc[]

toc::[]

Because Fluentd reads from the journal, and the journal default settings are very low, journal entries can be lost because the journal cannot keep up with the logging rate from system services.

We recommend setting `RateLimitIntervalSec=30s` and `RateLimitBurst=10000` (or even higher if necessary) to prevent the journal from losing entries.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.


include::modules/cluster-logging-systemd-scaling.adoc[leveloffset=+1]
