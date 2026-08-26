// Module included in the following assemblies:
//
// * /cicd/gitops/monitoring-argo-cd-custom-resource-workloads.adoc

:_mod-docs-content-type: PROCEDURE
[id="gitops-enabling-monitoring-for-argo-cd-custom-resource-workloads_{context}"]
= Enabling Monitoring for Argo CD custom resource workloads

By default, the monitoring configuration for Argo CD custom resource workloads is set to `false`.

With {gitops-title}, you can enable workload monitoring for specific Argo CD instances. As a result, the Operator creates a `PrometheusRule` object that contains alert rules for all the workloads managed by the specific Argo CD instances. These alert rules trigger the firing of an alert when the replica count of the corresponding component has drifted from the desired state for a certain amount of time. The Operator will not overwrite the changes made to the `PrometheusRule` object by the users.

.Procedure

. Set the `.spec.monitoring.enabled` field value to `true` on a given Argo CD instance:
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
    enabled: true
  ...
----

. Verify whether an alert rule is included in the PrometheusRule created by the Operator:
+
.Example alert rule

[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: argocd-component-status-alert
  namespace: openshift-gitops
spec:
  groups:
    - name: ArgoCDComponentStatus
      rules:
        ...
        - alert: ApplicationSetControllerNotReady <1>
          annotations:
            message: >-
              applicationSet controller deployment for Argo CD instance in
              namespace "default" is not running
          expr: >-
            kube_statefulset_status_replicas{statefulset="openshift-gitops-application-controller statefulset",
            namespace="openshift-gitops"} !=
            kube_statefulset_status_replicas_ready{statefulset="openshift-gitops-application-controller statefulset",
            namespace="openshift-gitops"}
          for: 1m
          labels:
            severity: critical
----
<1> Alert rule in the PrometheusRule that checks whether the workloads created by the Argo CD instances are running as expected.
