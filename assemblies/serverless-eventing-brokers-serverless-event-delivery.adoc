:_mod-docs-content-type: ASSEMBLY
[id="serverless-event-delivery"]
= Event delivery
include::_attributes/common-attributes.adoc[]
:context: serverless-event-delivery

toc::[]

You can configure event delivery parameters that are applied in cases where an event fails to be delivered to an event sink. Configuring event delivery parameters, including a dead letter sink, ensures that any events that fail to be delivered to an event sink are retried. Otherwise, undelivered events are dropped.

// event delivery behavior of different component types, e.g. kafka
include::modules/serverless-event-delivery-component-behaviors.adoc[leveloffset=+1]

// event delivery configurable parameters
include::modules/serverless-event-delivery-parameters.adoc[leveloffset=+1]

// configuring parameters examples
include::modules/serverless-configuring-event-delivery-examples.adoc[leveloffset=+1]

// event delivery ordering
include::modules/trigger-event-delivery-config.adoc[leveloffset=+1]
