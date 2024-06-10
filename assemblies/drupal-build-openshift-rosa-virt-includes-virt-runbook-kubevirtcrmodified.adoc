// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubeVirtCRModified"]
= KubeVirtCRModified

[discrete]
[id="meaning-kubevirtcrmodified"]
== Meaning

This alert fires when an operand of the HyperConverged Cluster Operator (HCO)
is changed by someone or something other than HCO.

HCO configures {VirtProductName} and its supporting operators in an
opinionated way and overwrites its operands when there is an unexpected change
to them. Users must not modify the operands directly. The `HyperConverged`
custom resource is the source of truth for the configuration.

[discrete]
[id="impact-kubevirtcrmodified"]
== Impact

Changing the operands manually causes the cluster configuration to fluctuate
and might lead to instability.

[discrete]
[id="diagnosis-kubevirtcrmodified"]
== Diagnosis

* Check the `component_name` value in the alert details to determine the operand
kind (`kubevirt`) and the operand name (`kubevirt-kubevirt-hyperconverged`)
that are being changed:
+
[source,text]
----
Labels
  alertname=KubevirtHyperconvergedClusterOperatorCRModification
  component_name=kubevirt/kubevirt-kubevirt-hyperconverged
  severity=warning
----

[discrete]
[id="mitigation-kubevirtcrmodified"]
== Mitigation

Do not change the HCO operands directly. Use `HyperConverged` objects to configure
the cluster.

The alert resolves itself after 10 minutes if the operands are not changed manually.
