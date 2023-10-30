:_mod-docs-content-type: ASSEMBLY
[id="distributed-tracing-rn-2-3"]
= Release notes for {DTProductName} 2.3
include::_attributes/common-attributes.adoc[]
:context: distributed-tracing-rn-2-3

toc::[]

include::modules/distr-tracing-product-overview.adoc[leveloffset=+1]

[id="component-versions-2-3-0_distributed-tracing-rn-2-3"]
== Component versions in the {DTProductName} 2.3.0

[options="header"]
|===
|Operator |Component |Version
|{JaegerName}
|Jaeger
|1.30.1

|{OTELName}
|OpenTelemetry
|0.44.0
|===

[id="component-versions-2-3-1_distributed-tracing-rn-2-3"]
== Component versions in the {DTProductName} 2.3.1

[options="header"]
|===
|Operator |Component |Version
|{JaegerName}
|Jaeger
|1.30.2

|{OTELName}
|OpenTelemetry
|0.44.1-1
|===

[id="new-features-and-enhancements_distributed-tracing-rn-2-3"]
== New features and enhancements

With this release, the {JaegerName} Operator is now installed to the `openshift-distributed-tracing` namespace by default. Before this update, the default installation had been in the `openshift-operators` namespace.

[id="bug-fixes_distributed-tracing-rn-2-3"]
== Bug fixes

This release addresses Common Vulnerabilities and Exposures (CVEs) and bug fixes.

//[id="known-issues_distributed-tracing-rn-2-3"]
//== Known issues

include::modules/support.adoc[leveloffset=+1]

include::modules/making-open-source-more-inclusive.adoc[leveloffset=+1]
