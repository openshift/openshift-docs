// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SSPHighRateRejectedVms"]
= SSPHighRateRejectedVms

[discrete]
[id="meaning-ssphighraterejectedvms"]
== Meaning

This alert fires when a user or script attempts to create or modify a large
number of virtual machines (VMs), using an invalid configuration.

[discrete]
[id="impact-ssphighraterejectedvms"]
== Impact

The VMs are not created or modified. As a result, the environment might not
behave as expected.

[discrete]
[id="diagnosis-ssphighraterejectedvms"]
== Diagnosis

. Export the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | grep ssp-operator | \
  awk '{print $1}')"
----

. Check the `virt-template-validator` logs for errors that might indicate the
cause:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l name=virt-template-validator
----
+
.Example output
+
[source,text]
----
{"component":"kubevirt-template-validator","level":"info","msg":"evalution
summary for ubuntu-3166wmdbbfkroku0:\nminimal-required-memory applied: FAIL,
value 1073741824 is lower than minimum [2147483648]\n\nsucceeded=false",
"pos":"admission.go:25","timestamp":"2021-09-28T17:59:10.934470Z"}
----

[discrete]
[id="mitigation-ssphighraterejectedvms"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
