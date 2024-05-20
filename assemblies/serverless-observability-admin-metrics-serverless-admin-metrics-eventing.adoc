:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-admin-metrics-eventing"]
= Knative Eventing metrics
:context: serverless-admin-metrics-eventing

toc::[]

Cluster administrators can view the following metrics for Knative Eventing components.

By aggregating the metrics from HTTP code, events can be separated into two categories; successful events (2xx) and failed events (5xx).

include::modules/serverless-broker-ingress-metrics.adoc[leveloffset=+1]
include::modules/serverless-broker-filter-metrics.adoc[leveloffset=+1]
include::modules/serverless-inmemory-dispatch-metrics.adoc[leveloffset=+1]
include::modules/serverless-event-source-metrics.adoc[leveloffset=+1]