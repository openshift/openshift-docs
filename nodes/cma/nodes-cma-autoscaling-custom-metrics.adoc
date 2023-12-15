:_mod-docs-content-type: ASSEMBLY
:context: nodes-cma-autoscaling-custom-metrics
[id="nodes-cma-autoscaling-custom-metrics"]
= Viewing Operator metrics
include::_attributes/common-attributes.adoc[]

toc::[]


The Custom Metrics Autoscaler Operator exposes ready-to-use metrics that it pulls from the on-cluster monitoring component. You can query the metrics by using the Prometheus Query Language (PromQL) to analyze and diagnose issues. All metrics are reset when the controller pod restarts.

include::modules/nodes-cma-autoscaling-custom-metrics-access.adoc[leveloffset=+1]
include::modules/nodes-cma-autoscaling-custom-metrics-provided.adoc[leveloffset=+2]
