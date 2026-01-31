// Module included in the following assemblies:
//
// * security/oc_compliance_plug_in/co-scans/oc-compliance-plug-in-using.adoc

:_mod-docs-content-type: PROCEDURE
[id="viewing-compliance-remediation-details_{context}"]
= Viewing ComplianceCheckResult object details

When scans are finished running, `ComplianceCheckResult` objects are created for the individual scan rules. The `view-result` subcommand provides a human-readable output of the `ComplianceCheckResult` object details.

.Procedure

* Run:
+
[source,terminal]
----
$ oc compliance view-result ocp4-cis-scheduler-no-bind-address
----
