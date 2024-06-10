// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SSPFailingToReconcile"]
= SSPFailingToReconcile

[discrete]
[id="meaning-sspfailingtoreconcile"]
== Meaning

This alert fires when the reconcile cycle of the Scheduling, Scale and
Performance (SSP) Operator fails repeatedly, although the SSP Operator
is running.

The SSP Operator is responsible for deploying and reconciling the common
templates and the Template Validator.

[discrete]
[id="impact-sspfailingtoreconcile"]
== Impact

Dependent components might not be deployed. Changes in the components might
not be reconciled. As a result, the common templates or the Template
Validator might not be updated or reset if they fail.

[discrete]
[id="diagnosis-sspfailingtoreconcile"]
== Diagnosis

. Export the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | grep ssp-operator | \
  awk '{print $1}')"
----

. Obtain the details of the `ssp-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pods -l control-plane=ssp-operator
----

. Check the `ssp-operator` logs for errors:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l control-plane=ssp-operator
----

. Obtain the status of the `virt-template-validator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l name=virt-template-validator
----

. Obtain the details of the `virt-template-validator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pods -l name=virt-template-validator
----

. Check the `virt-template-validator` logs for errors:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l name=virt-template-validator
----

[discrete]
[id="mitigation-sspfailingtoreconcile"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
