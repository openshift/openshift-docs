.Example AlertingRule CR
[source,yaml]
----
  apiVersion: loki.grafana.com/v1
  kind: AlertingRule
  metadata:
    name: loki-operator-alerts
    namespace: openshift-operators-redhat <1>
    labels: <2>
      openshift.io/cluster-monitoring: "true"
  spec:
    tenantID: "infrastructure" <3> <4> <5>
    groups:
      - name: LokiOperatorHighReconciliationError
        rules:
          - alert: HighPercentageError
            expr: | <6>
              sum(rate({kubernetes_namespace_name="openshift-operators-redhat", kubernetes_pod_name=~"loki-operator-controller-manager.*"} |= "error" [1m])) by (job)
                /
              sum(rate({kubernetes_namespace_name="openshift-operators-redhat", kubernetes_pod_name=~"loki-operator-controller-manager.*"}[1m])) by (job)
                > 0.01
            for: 10s
            labels:
              severity: critical <7>
            annotations:
              summary: High Loki Operator Reconciliation Errors <8>
              description: High Loki Operator Reconciliation Errors <9>
----
<1> The `namespace` where this AlertingRule is created must have a label matching the LokiStack `spec.rules.namespaceSelector` definition.
<2> The `labels` block must match the LokiStack `spec.rules.selector` definition.
<3> Must be `application`, `infrastructure`, or `audit`.
<4> AlertingRules for `infrastructure` tenants are only supported in the `openshift-\*`, `kube-\*`, or `default` namespaces.
<5> AlertingRules for `audit` tenants are only supported in the `openshift-logging` namespace.
<6> Value for `kubernetes_namespace_name:` must match the value for `metadata.namespace`.
<7> Mandatory field. Must be `critical`, `warning`, or `info`.
<8> Mandatory field.
<9> Mandatory field.
