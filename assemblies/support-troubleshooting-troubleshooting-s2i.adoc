:_mod-docs-content-type: ASSEMBLY
[id="troubleshooting-s2i"]
= Troubleshooting the Source-to-Image process
include::_attributes/common-attributes.adoc[]
:context: troubleshooting-s2i

toc::[]

// Strategies for Source-to-Image troubleshooting
include::modules/strategies-for-s2i-troubleshooting.adoc[leveloffset=+1]

// Gathering Source-to-Image diagnostic data
include::modules/gathering-s2i-diagnostic-data.adoc[leveloffset=+1]

// Gathering application diagnostic data to investigate application failures
include::modules/gathering-application-diagnostic-data.adoc[leveloffset=+1]

ifndef::openshift-rosa,openshift-dedicated[]
[role="_additional-resources"]
== Additional resources

* See xref:../../cicd/builds/build-strategies.adoc#build-strategy-s2i_build-strategies[Source-to-Image (S2I) build] for more details about the S2I build strategy.
endif::openshift-rosa,openshift-dedicated[]
