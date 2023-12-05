// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-SSPTemplateValidatorDown"]
= SSPTemplateValidatorDown

[discrete]
[id="meaning-ssptemplatevalidatordown"]
== Meaning

This alert fires when all the Template Validator pods are down.

The Template Validator checks virtual machines (VMs) to ensure that they
do not violate their templates.

[discrete]
[id="impact-ssptemplatevalidatordown"]
== Impact

VMs are not validated against their templates. As a result, VMs might be
created with specifications that do not match their respective workloads.

[discrete]
[id="diagnosis-ssptemplatevalidatordown"]
== Diagnosis

. Set the `NAMESPACE` environment variable:
+
[source,terminal]
----
$ export NAMESPACE="$(oc get deployment -A | grep ssp-operator | \
  awk '{print $1}')"
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

. Check the  `virt-template-validator` logs for error messages:
+
[source,terminal]
----
$ oc -n $NAMESPACE logs --tail=-1 -l name=virt-template-validator
----

[discrete]
[id="mitigation-ssptemplatevalidatordown"]
== Mitigation

Try to identify the root cause and resolve the issue.

If you cannot resolve the issue, log in to the
link:https://access.redhat.com[Customer Portal] and open a support case,
attaching the artifacts gathered during the diagnosis procedure.
