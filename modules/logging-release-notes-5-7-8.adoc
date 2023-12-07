// Module included in the following assemblies:
// cluster-logging-release-notes.adoc
// logging-5-7-release-notes.adoc

:_mod-docs-content-type: REFERENCE
[id="logging-release-notes-5-7-8_{context}"]
= Logging 5.7.8
This release includes link:https://access.redhat.com/errata/RHBA-2023:6730[OpenShift Logging Bug Fix Release 5.7.8].

[id="logging-release-notes-5-7-8-bug-fixes"]
== Bug fixes
* Before this update, there was a potential conflict when the same name was used for the `outputRefs` and `inputRefs` parameters in the `ClusterLogForwarder` custom resource (CR). As a result, the collector pods entered in a `CrashLoopBackOff` status. With this update, the output labels contain the `OUTPUT_` prefix to ensure a distinction between output labels and pipeline names. (link:https://issues.redhat.com/browse/LOG-4383[LOG-4383])

* Before this update, while configuring the JSON log parser, if you did not set the `structuredTypeKey` or `structuredTypeName` parameters for the Cluster Logging Operator, no alert would display about an invalid configuration. With this update, the Cluster Logging Operator informs you about the configuration issue. (link:https://issues.redhat.com/browse/LOG-4441[LOG-4441])

* Before this update, if the `hecToken` key was missing or incorrect in the secret specified for a Splunk output, the validation failed because the Vector forwarded logs to Splunk without a token. With this update, if the `hecToken` key is missing or incorrect, the validation fails with the `A non-empty hecToken entry is required` error message. (link:https://issues.redhat.com/browse/LOG-4580[LOG-4580])

* Before this update, selecting a date from the `Custom time range` for logs caused an error in the web console. With this update, you can select a date from the time range model in the web console successfully. (link:https://issues.redhat.com/browse/LOG-4684[LOG-4684])

[id="logging-release-notes-5-7-8-CVEs"]
== CVEs
* link:https://access.redhat.com/security/cve/CVE-2023-40217[CVE-2023-40217]
* link:https://access.redhat.com/security/cve/CVE-2023-44487[CVE-2023-44487]