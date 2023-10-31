// Module included in the following assemblies:
//
// * /cicd/gitops/monitoring-argo-cd-custom-resource-workloads.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-disabling-monitoring-for-argo-cd-custom-resource-workloads_{context}"]
= Disabling Monitoring for Argo CD custom resource workloads

You can disable workload monitoring for specific Argo CD instances. Disabling workload monitoring deletes the created PrometheusRule.

.Procedure

* Set the `.spec.monitoring.enabled` field value to `false` on a given Argo CD instance:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  ...
  monitoring:
    enabled: false
  ...
----