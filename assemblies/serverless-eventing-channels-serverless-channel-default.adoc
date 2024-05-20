:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-channel-default"]
= Default channel implementation
:context: serverless-channel-default

You can use the `default-ch-webhook` config map to specify the default channel implementation of Knative Eventing. You can specify the default channel implementation for the entire cluster or for one or more namespaces. Currently the `InMemoryChannel` and `KafkaChannel` channel types are supported.

// Knative Eventing
include::modules/serverless-channel-default.adoc[leveloffset=+1]