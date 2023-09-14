:_mod-docs-content-type: ASSEMBLY
[id="otel-configuring"]
= Configuring and deploying the {OTELShortName}
include::_attributes/common-attributes.adoc[]
:context: otel-configuring

toc::[]

The {OTELName} Operator uses a custom resource definition (CRD) file that defines the architecture and configuration settings to be used when creating and deploying the {OTELShortName} resources. You can install the default configuration or modify the file.

include::modules/otel-config-collector.adoc[leveloffset=+1]
include::modules/otel-config-multicluster.adoc[leveloffset=+1]
include::modules/otel-config-send-metrics-monitoring-stack.adoc[leveloffset=+1]

[id="setting-up-monitoring-for-otel"]
== Setting up monitoring for the {OTELShortName}

The {OTELOperator} supports monitoring and alerting of each OpenTelemtry Collector instance and exposes upgrade and operational metrics about the Operator itself.

include::modules/otel-configuring-otelcol-metrics.adoc[leveloffset=+2]

// modules/otel-configuring-oteloperator-metrics.adoc[leveloffset=+2]

[role="_additional-resources"]
[id="additional-resources_deploy-otel"]
== Additional resources
* xref:../monitoring/enabling-monitoring-for-user-defined-projects.adoc#enabling-monitoring-for-user-defined-projects[Enabling monitoring for user-defined projects]
