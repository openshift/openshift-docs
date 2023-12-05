// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SSPCommonTemplatesModificationReverted"]
= SSPCommonTemplatesModificationReverted

[discrete]
[id="meaning-sspcommontemplatesmodificationreverted"]
== Meaning

This alert fires when the Scheduling, Scale, and Performance (SSP) Operator
reverts changes to common templates as part of its reconciliation procedure.

The SSP Operator deploys and reconciles the common templates and the Template
Validator. If a user or script changes a common template, the changes are reverted
by the SSP Operator.

[discrete]
[id="impact-sspcommontemplatesmodificationreverted"]
== Impact

Changes to common templates are overwritten.

[discrete]
[id="diagnosis-sspcommontemplatesmodificationreverted"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | grep ssp-operator | \
  awk '{print $1}')"
----

. Check the `ssp-operator` logs for templates with reverted changes:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l control-plane=ssp-operator | \
  grep 'common template' -C 3
----

[discrete]
[id="mitigation-sspcommontemplatesmodificationreverted"]
== Mitigation

Try to identify and resolve the cause of the changes.

Ensure that changes are made only to copies of templates, and not to the templates
themselves.
