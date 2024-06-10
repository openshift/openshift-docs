// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SSPDown"]
= SSPDown

[discrete]
[id="meaning-sspdown"]
== Meaning

This alert fires when all the Scheduling, Scale and Performance (SSP) Operator
pods are down.

The SSP Operator is responsible for deploying and reconciling the common
templates and the Template Validator.

[discrete]
[id="impact-sspdown"]
== Impact

Dependent components might not be deployed. Changes in the components might
not be reconciled. As a result, the common templates and/or the Template
Validator might not be updated or reset if they fail.

[discrete]
[id="diagnosis-sspdown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | grep ssp-operator | \
  awk '{print $1}')"
----

. Check the status of the `ssp-operator` pods.
+
[source,terminal]
----
$ oc -n $NAMESPACE get pods -l control-plane=ssp-operator
----

. Obtain the details of the `ssp-operator` pods:
+
[source,terminal]
----
$ oc -n $NAMESPACE describe pods -l control-plane=ssp-operator
----

. Check the `ssp-operator` logs for error messages:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l control-plane=ssp-operator
----

[discrete]
[id="mitigation-sspdown"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
