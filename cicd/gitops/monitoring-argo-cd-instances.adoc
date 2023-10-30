:_mod-docs-content-type: ASSEMBLY
[id="monitoring-argo-cd-instances"]
= Monitoring Argo CD instances
include::_attributes/common-attributes.adoc[]
:context: monitoring-argo-cd-instances

toc::[]

By default, the {gitops-title} Operator automatically detects an installed Argo CD instance in your defined namespace, for example, `openshift-gitops`, and connects it to the monitoring stack of the cluster to provide alerts for out-of-sync applications.

.Prerequisites
* You have access to the cluster with `cluster-admin` privileges.
* You have access to the {product-title} web console.
* You have installed the {gitops-title} Operator in your cluster.
* You have installed an Argo CD application in your defined namespace, for example, `openshift-gitops`.

include::modules/gitops-monitoring-argo-cd-health-using-prometheus-metrics.adoc[leveloffset=+1]
