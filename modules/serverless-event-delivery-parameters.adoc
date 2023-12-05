// Module included in the following assemblies:
//
// serverless/develop/serverless-event-delivery.adoc

:_mod-docs-content-type: REFERENCE
[id="serverless-event-delivery-parameters_{context}"]
= Configurable event delivery parameters

The following parameters can be configured for event delivery:

Dead letter sink:: You can configure the `deadLetterSink` delivery parameter so that if an event fails to be delivered, it is stored in the specified event sink. Undelivered events that are not stored in a dead letter sink are dropped. The dead letter sink be any addressable object that conforms to the Knative Eventing sink contract, such as a Knative service, a Kubernetes service, or a URI.

Retries:: You can set a minimum number of times that the delivery must be retried before the event is sent to the dead letter sink, by configuring the `retry` delivery parameter with an integer value.

Back off delay:: You can set the `backoffDelay` delivery parameter to specify the time delay before an event delivery retry is attempted after a failure. The duration of the `backoffDelay` parameter is specified using the https://en.wikipedia.org/wiki/ISO_8601#Durations[ISO 8601] format. For example, `PT1S` specifies a 1 second delay.

Back off policy:: The `backoffPolicy` delivery parameter can be used to specify the retry back off policy. The policy can be specified as either `linear` or `exponential`. When using the `linear` back off policy, the back off delay is equal to `backoffDelay * <numberOfRetries>`. When using the `exponential` backoff policy, the back off delay is equal to `backoffDelay*2^<numberOfRetries>`.
