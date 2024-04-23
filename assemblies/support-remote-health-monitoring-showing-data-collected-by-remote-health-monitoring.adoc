:_mod-docs-content-type: ASSEMBLY
[id="showing-data-collected-by-remote-health-monitoring"]
= Showing data collected by remote health monitoring
include::_attributes/common-attributes.adoc[]
ifdef::openshift-dedicated[]
include::_attributes/attributes-openshift-dedicated.adoc[]
endif::[]
:context: showing-data-collected-by-remote-health-monitoring

toc::[]

As an administrator, you can review the metrics collected by Telemetry and the Insights Operator.

include::modules/telemetry-showing-data-collected-from-the-cluster.adoc[leveloffset=+1]

// cannot create resource "pods/exec" in API group "" in the namespace "openshift-insights"
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/insights-operator-showing-data-collected-from-the-cluster.adoc[leveloffset=+1]
endif::openshift-rosa,openshift-dedicated[]
