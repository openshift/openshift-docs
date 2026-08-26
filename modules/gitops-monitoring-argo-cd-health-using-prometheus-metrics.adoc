// Module included in the following assemblies:
//
// * cicd/gitops/monitoring-argo-cd-instances.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-monitoring-argo-cd-health-using-promethous-metrics_{context}"]
= Monitoring Argo CD health using Prometheus metrics

You can monitor the health status of an Argo CD application by running Prometheus metrics queries against it.

.Procedure

. In the *Developer* perspective of the web console, select the namespace where your Argo CD application is installed, and navigate to *Observe* -> *Metrics*.
. From the *Select query* drop-down list, select *Custom query*.
. To check the health status of your Argo CD application, enter the Prometheus Query Language (PromQL) query similar to the following example in the *Expression* field:
+
.Example
[source,terminal]
----
sum(argocd_app_info{dest_namespace=~"<your_defined_namespace>",health_status!=""}) by (health_status) <1>
----
<1> Replace the `<your_defined_namespace>` variable with the actual name of your defined namespace, for example `openshift-gitops`.


