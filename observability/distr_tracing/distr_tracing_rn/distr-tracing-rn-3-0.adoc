:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="distributed-tracing-rn-3-0"]
= Release notes for {DTProductName} 3.0
:context: distributed-tracing-rn-3-0

toc::[]

include::modules/distr-tracing-product-overview.adoc[leveloffset=+1]

[id="component-versions_distributed-tracing-rn-3-0"]
== Component versions in the {DTProductName} 3.0

[options="header"]
|===
|Operator |Component |Version
|{JaegerName}
|Jaeger
|1.51.0

|xref:../../otel/otel-release-notes.adoc[{OTELName}]
|OpenTelemetry
|0.89.0

|{TempoName}
|Tempo
|2.3.0
|===

// Jaeger section
[id="jaeger-release-notes_distributed-tracing-rn-3-0"]
== {JaegerName}

[id="deprecated-functionality_jaeger-release-notes_distributed-tracing-rn-3-0"]
=== Deprecated functionality

In Red Hat OpenShift distributed tracing 3.0, Jaeger and Elasticsearch are deprecated, and both are planned to be removed in a future release. Red Hat will provide critical and above CVE bug fixes and support for these components during the current release lifecycle, but these components will no longer receive feature enhancements.

In Red Hat OpenShift distributed tracing 3.0, Tempo provided by the {TempoOperator} and the OpenTelemetry collector provided by the Red Hat build of OpenTelemetry are the preferred Operators for distributed tracing collection and storage. The OpenTelemetry and Tempo distributed tracing stack is to be adopted by all users because this will be the stack that will be enhanced going forward.

[id="new-features-and-enhancements_jaeger-release-notes_distributed-tracing-rn-3-0"]
=== New features and enhancements

This update introduces the following enhancements for the {JaegerShortName}:

* Support for the ARM architecture.
* Support for cluster-wide proxy environments.

[id="bug-fixes_jaeger-release-notes_distributed-tracing-rn-3-0"]
=== Bug fixes

This update introduces the following bug fixes for the {JaegerShortName}:

* Fixed support for disconnected environments when using the `oc adm catalog mirror` CLI command. (link:https://issues.redhat.com/browse/TRACING-3546[TRACING-3546])

[id="known-issues_jaeger-release-notes_distributed-tracing-rn-3-0"]
=== Known issues

* Currently, Apache Spark is not supported.

ifndef::openshift-rosa[]

* Currently, the streaming deployment via AMQ/Kafka is not supported on the IBM Z and IBM Power Systems architectures.
endif::openshift-rosa[]

// Tempo section
[id="tempo-release-notes_distributed-tracing-rn-3-0"]
== {TempoName}

[id="new-features-and-enhancements_tempo-release-notes_distributed-tracing-rn-3-0"]
=== New features and enhancements

This update introduces the following enhancements for the {TempoShortName}:

* Support for the ARM architecture.
* Support for span request count, duration, and error count (RED) metrics. The metrics can be visualized in the Jaeger console deployed as part of Tempo or in the web console in the *Observe* menu.

[id="bug-fixes_tempo-release-notes_distributed-tracing-rn-3-0"]
=== Bug fixes

This update introduces the following bug fixes for the {TempoShortName}:

* Fixed support for the custom TLS CA option for connecting to object storage. (link:https://issues.redhat.com/browse/TRACING-3462[TRACING-3462])
* Fixed support for disconnected environments when using the `oc adm catalog mirror` CLI command. (link:https://issues.redhat.com/browse/TRACING-3523[TRACING-3523])
* Fixed mTLS when Gateway is not deployed. (link:https://issues.redhat.com/browse/TRACING-3510[TRACING-3510])

[id="known-issues_tempo-release-notes_distributed-tracing-rn-3-0"]
=== Known issues

* Currently, when used with the {TempoOperator}, the Jaeger UI only displays services that have sent traces in the last 15 minutes. For services that did not send traces in the last 15 minutes, traces are still stored but not displayed in the Jaeger UI. (link:https://issues.redhat.com/browse/TRACING-3139[TRACING-3139])
* Currently, the {TempoShortName} fails on the IBM Z (`s390x`) architecture. (link:https://issues.redhat.com/browse/TRACING-3545[TRACING-3545])

include::modules/support.adoc[leveloffset=+1]

include::modules/making-open-source-more-inclusive.adoc[leveloffset=+1]
