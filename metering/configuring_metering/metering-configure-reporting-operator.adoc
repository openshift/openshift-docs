:_mod-docs-content-type: ASSEMBLY
[id="metering-configure-reporting-operator"]
= Configuring the Reporting Operator
include::_attributes/common-attributes.adoc[]
:context: metering-configure-reporting-operator

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

The Reporting Operator is responsible for collecting data from Prometheus, storing the metrics in Presto, running report queries against Presto, and exposing their results via an HTTP API. Configuring the Reporting Operator is primarily done in your `MeteringConfig` custom resource.

include::modules/metering-prometheus-connection.adoc[leveloffset=+1]

include::modules/metering-exposing-the-reporting-api.adoc[leveloffset=+1]
