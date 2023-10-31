:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-event-sinks"]
= Event sinks
:context: serverless-event-sinks

toc::[]

include::snippets/serverless-about-event-sinks.adoc[]

Addressable objects receive and acknowledge an event delivered over HTTP to an address defined in their `status.address.url` field. As a special case, the core Kubernetes `Service` object also fulfills the addressable interface.

Callable objects are able to receive an event delivered over HTTP and transform the event, returning `0` or `1` new events in the HTTP response. These returned events may be further processed in the same way that events from an external event source are processed.

// Using --sink flag with kn (generic)
include::modules/specifying-sink-flag-kn.adoc[leveloffset=+1]

[TIP]
====
You can configure which CRs can be used with the `--sink` flag for Knative (`kn`) CLI commands by xref:../../../serverless/cli_tools/advanced-kn-config.adoc#advanced-kn-config[Customizing `kn`].
====
