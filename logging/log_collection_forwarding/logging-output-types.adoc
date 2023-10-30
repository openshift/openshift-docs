:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="logging-output-types"]
= Log output types
:context: logging-output-types

toc::[]

Log outputs specified in the `ClusterLogForwarder` CR can be any of the following types:

`default`:: The on-cluster, Red{nbsp}Hat managed log store. You are not required to configure the default output.
+
[NOTE]
====
If you configure a `default` output, you receive an error message, because the `default` output name is reserved for referencing the on-cluster, Red{nbsp}Hat managed log store.
====
`loki`:: Loki, a horizontally scalable, highly available, multi-tenant log aggregation system.
`kafka`:: A Kafka broker. The `kafka` output can use a TCP or TLS connection.
`elasticsearch`:: An external Elasticsearch instance. The `elasticsearch` output can use a TLS connection.
`fluentdForward`:: An external log aggregation solution that supports Fluentd. This option uses the Fluentd *forward* protocols. The `fluentForward` output can use a TCP or TLS connection and supports shared-key authentication by providing a *shared_key* field in a secret. Shared-key authentication can be used with or without TLS.
+
[IMPORTANT]
====
The `fluentdForward` output is only supported if you are using the Fluentd collector. It is not supported if you are using the Vector collector. If you are using the Vector collector, you can forward logs to Fluentd by using the `http` output.
====
`syslog`:: An external log aggregation solution that supports the syslog link:https://tools.ietf.org/html/rfc3164[RFC3164] or link:https://tools.ietf.org/html/rfc5424[RFC5424] protocols. The `syslog` output can use a UDP, TCP, or TLS connection.
`cloudwatch`:: Amazon CloudWatch, a monitoring and log storage service hosted by Amazon Web Services (AWS).

// supported outputs by version
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-7.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-6.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-5.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-4.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-3.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-2.adoc[leveloffset=+1]
include::modules/cluster-logging-collector-log-forwarding-supported-plugins-5-1.adoc[leveloffset=+1]
