// Do not edit this module. It is generated with a script.
// Do not reuse this module. The anchor IDs do not contain a context statement.
// Module included in the following assemblies:
//
// * virt/monitoring/virt-runbooks.adoc

:_mod-docs-content-type: REFERENCE
[id="virt-runbook-KubeVirtDeprecatedAPIRequested"]
= KubeVirtDeprecatedAPIRequested

[discrete]
[id="meaning-kubevirtdeprecatedapirequested"]
== Meaning

This alert fires when a deprecated `KubeVirt` API is used.

[discrete]
[id="impact-kubevirtdeprecatedapirequested"]
== Impact

Using a deprecated API is not recommended because the request will
fail when the API is removed in a future release.

[discrete]
[id="diagnosis-kubevirtdeprecatedapirequested"]
== Diagnosis

* Check the *Description* and *Summary* sections of the alert to identify the
deprecated API as in the following example:
+
*Description*
+
`Detected requests to the deprecated virtualmachines.kubevirt.io/v1alpha3 API.`
+
*Summary*
+
`2 requests were detected in the last 10 minutes.`

[discrete]
[id="mitigation-kubevirtdeprecatedapirequested"]
== Mitigation

Use fully supported APIs. The alert resolves itself after 10 minutes if the deprecated
API is not used.
