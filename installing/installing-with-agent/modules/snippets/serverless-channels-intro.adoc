// Text snippet included in the following files
//
// * /serverless/develop/serverless-creating-channels.adoc
// * /serverless/discover/serverless-channels.adoc

Channels are custom resources that define a single event-forwarding and persistence layer. After events have been sent to a channel from an event source or producer, these events can be sent to multiple Knative services or other sinks by using a subscription.

image::serverless-event-channel-workflow.png[Channel workflow overview]

You can create channels by instantiating a supported `Channel` object, and configure re-delivery attempts by modifying the `delivery` spec in a `Subscription` object.
