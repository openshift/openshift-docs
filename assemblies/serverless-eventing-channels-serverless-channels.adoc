:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-channels"]
= Channels and subscriptions
:context: serverless-channels

toc::[]

include::snippets/serverless-channels-intro.adoc[]

After you create a `Channel` object, a mutating admission webhook adds a set of `spec.channelTemplate` properties for the `Channel` object based on the default channel implementation. For example, for an `InMemoryChannel` default implementation, the `Channel` object looks as follows:

[source,yaml]
----
apiVersion: messaging.knative.dev/v1
kind: Channel
metadata:
  name: example-channel
  namespace: default
spec:
  channelTemplate:
    apiVersion: messaging.knative.dev/v1
    kind: InMemoryChannel
----

The channel controller then creates the backing channel instance based on the `spec.channelTemplate` configuration.

[NOTE]
====
The `spec.channelTemplate` properties cannot be changed after creation, because they are set by the default channel mechanism rather than by the user.
====

When this mechanism is used with the preceding example, two objects are created: a generic backing channel and an `InMemoryChannel` channel. If you are using a different default channel implementation, the `InMemoryChannel` is replaced with one that is specific to your implementation. For example, with the Knative broker for Apache Kafka, the `KafkaChannel` channel is created.

The backing channel acts as a proxy that copies its subscriptions to the user-created channel object, and sets the user-created channel object status to reflect the status of the backing channel.

[id="serverless-channels-implementations"]
== Channel implementation types

`InMemoryChannel` and `KafkaChannel` channel implementations can be used with {ServerlessProductName} for development use.

The following are limitations of `InMemoryChannel` type channels:

* No event persistence is available. If a pod goes down, events on that pod are lost.
* `InMemoryChannel` channels do not implement event ordering, so two events that are received in the channel at the same time can be delivered to a subscriber in any order.
* If a subscriber rejects an event, there are no re-delivery attempts by default. You can configure re-delivery attempts by modifying the `delivery` spec in the `Subscription` object.
