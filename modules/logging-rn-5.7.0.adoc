//module included in logging-5-7-release-notes.adoc
:content-type: REFERENCE
[id="logging-release-notes-5-7-0{context}"]
= Logging 5.7.0
This release includes link:https://access.redhat.com/errata/RHBA-2023:2133[OpenShift Logging Bug Fix Release 5.7.0].

[id="logging-5-7-enhancements"]
== Enhancements
With this update, you can enable logging to detect multi-line exceptions and reassemble them into a single log entry.

To enable logging to detect multi-line exceptions and reassemble them into a single log entry, ensure that the `ClusterLogForwarder` Custom Resource (CR) contains a `detectMultilineErrors` field, with a value of `true`.

[id="logging-5-7-known-issues"]
== Known Issues
None.

[id="logging-5-7-0-bug-fixes"]
== Bug fixes
* Before this update, the `nodeSelector` attribute for the Gateway component of the LokiStack did not impact node scheduling. With this update, the `nodeSelector` attribute works as expected. (link:https://issues.redhat.com/browse/LOG-3713[LOG-3713])

[id="logging-5-7-0-CVEs"]
== CVEs
* link:https://access.redhat.com/security/cve/CVE-2023-1999[CVE-2023-1999]
* link:https://access.redhat.com/security/cve/CVE-2023-28617[CVE-2023-28617]
