// Module included in the following assemblies:
// cluster-logging-release-notes.adoc
:_mod-docs-content-type: REFERENCE
[id="cluster-logging-release-notes-5-7-2_{context}"]
= Logging 5.7.2
This release includes link:https://access.redhat.com/errata/RHSA-2023:3495[OpenShift Logging Bug Fix Release 5.7.2].

[id="openshift-logging-5-7-2-bug-fixes_{context}"]
== Bug fixes
* Before this update, it was not possible to delete the `openshift-logging` namespace directly due to the presence of a pending finalizer. With this update, the finalizer is no longer utilized, enabling direct deletion of the namespace. (link:https://issues.redhat.com/browse/LOG-3316[LOG-3316])

* Before this update, the `run.sh` script would display an incorrect `chunk_limit_size` value if it was changed according to the {product-title} documentation. However, when setting the `chunk_limit_size` via the environment variable `$BUFFER_SIZE_LIMIT`, the script would show the correct value. With this update, the `run.sh` script now consistently displays the correct `chunk_limit_size` value in both scenarios. (link:https://issues.redhat.com/browse/LOG-3330[LOG-3330])

* Before this update, the {product-title} web console's logging view plugin did not allow for custom node placement or tolerations. This update adds the ability to define node placement and tolerations for the logging view plugin. (link:https://issues.redhat.com/browse/LOG-3749[LOG-3749])

* Before this update, the Cluster Logging Operator encountered an Unsupported Media Type exception when trying to send logs to DataDog via the Fluentd HTTP Plugin. With this update, users can seamlessly assign the content type for log forwarding by configuring the HTTP header Content-Type. The value provided is automatically assigned to the `content_type` parameter within the plugin, ensuring successful log transmission. (link:https://issues.redhat.com/browse/LOG-3784[LOG-3784])

* Before this update, when the `detectMultilineErrors` field was set to `true` in the `ClusterLogForwarder` custom resource (CR), PHP multi-line errors were recorded as separate log entries, causing the stack trace to be split across multiple messages. With this update, multi-line error detection for PHP is enabled, ensuring that the entire stack trace is included in a single log message. (link:https://issues.redhat.com/browse/LOG-3878[LOG-3878])

* Before this update, `ClusterLogForwarder` pipelines containing a space in their name caused the Vector collector pods to continuously crash. With this update, all spaces, dashes (-), and dots (.) in pipeline names are replaced with underscores (_). (link:https://issues.redhat.com/browse/LOG-3945[LOG-3945])

* Before this update, the `log_forwarder_output` metric did not include the `http` parameter. This update adds the missing parameter to the metric. (link:https://issues.redhat.com/browse/LOG-3997[LOG-3997])

* Before this update, Fluentd did not identify some multi-line JavaScript client exceptions when they ended with a colon. With this update, the Fluentd buffer name is prefixed with an underscore, resolving the issue. (link:https://issues.redhat.com/browse/LOG-4019[LOG-4019])

* Before this update, when configuring log forwarding to write to a Kafka output topic which matched a key in the payload, logs dropped due to an error.  With this update, Fluentd's buffer name has been prefixed with an underscore, resolving the issue.(link:https://issues.redhat.com/browse/LOG-4027[LOG-4027])

* Before this update, the LokiStack gateway returned label values for namespaces without applying the access rights of a user. With this update, the LokiStack gateway applies permissions to label value requests, resolving the issue. (link:https://issues.redhat.com/browse/LOG-4049[LOG-4049])

* Before this update, the Cluster Logging Operator API required a certificate to be provided by a secret when the `tls.insecureSkipVerify` option was set to `true`. With this update, the Cluster Logging Operator API no longer requires a certificate to be provided by a secret in such cases. The following configuration has been added to the Operator's CR:
+
[source,yaml]
----
tls.verify_certificate = false
tls.verify_hostname = false
----
+
(link:https://issues.redhat.com/browse/LOG-3445[LOG-3445])

* Before this update, the LokiStack route configuration caused queries running longer than 30 seconds to timeout. With this update, the LokiStack global and per-tenant `queryTimeout` settings affect the route timeout settings, resolving the issue. (link:https://issues.redhat.com/browse/LOG-4052[LOG-4052])

* Before this update, a prior fix to remove defaulting of the `collection.type` resulted in the Operator no longer honoring the deprecated specs for resource, node selections, and tolerations.  This update modifies the Operator behavior to always prefer the `collection.logs` spec over those of `collection`.  This varies from previous behavior that allowed using both the preferred fields and deprecated fields but would ignore the deprecated fields when `collection.type` was populated. (link:https://issues.redhat.com/browse/LOG-4185[LOG-4185])

* Before this update, the Vector log collector did not generate TLS configuration for forwarding logs to multiple Kafka brokers if the broker URLs were not specified in the output. With this update, TLS configuration is generated appropriately for multiple brokers. (link:https://issues.redhat.com/browse/LOG-4163[LOG-4163])

* Before this update, the option to enable passphrase for log forwarding to Kafka was unavailable. This limitation presented a security risk as it could potentially expose sensitive information. With this update, users now have a seamless option to enable passphrase for log forwarding to Kafka. (link:https://issues.redhat.com/browse/LOG-3314[LOG-3314])

* Before this update, Vector log collector did not honor the `tlsSecurityProfile` settings for outgoing TLS connections. After this update, Vector handles TLS connection settings appropriately. (link:https://issues.redhat.com/browse/LOG-4011[LOG-4011])

* Before this update, not all available output types were included in the `log_forwarder_output_info` metrics. With this update, metrics contain Splunk and Google Cloud Logging data which was missing previously. (link:https://issues.redhat.com/browse/LOG-4098[LOG-4098])

* Before this update, when `follow_inodes` was set to `true`, the Fluentd collector could crash on file rotation. With this update, the `follow_inodes` setting does not crash the collector. (link:https://issues.redhat.com/browse/LOG-4151[LOG-4151])

* Before this update, the Fluentd collector could incorrectly close files that should be watched because of how those files were tracked. With this update, the tracking parameters have been corrected.  (link:https://issues.redhat.com/browse/LOG-4149[LOG-4149])

* Before this update, forwarding logs with the Vector collector and naming a pipeline in the `ClusterLogForwarder` instance `audit`, `application` or `infrastructure` resulted in collector pods staying in the `CrashLoopBackOff` state with the following error in the collector log:
+
[source,text]
----
ERROR vector::cli: Configuration error. error=redefinition of table transforms.audit for key transforms.audit
----
+
After this update, pipeline names no longer clash with reserved input names, and pipelines can be named `audit`, `application` or `infrastructure`. (link:https://issues.redhat.com/browse/LOG-4218[LOG-4218])

* Before this update, when forwarding logs to a syslog destination with the Vector collector and setting the `addLogSource` flag to `true`, the following extra empty fields were added to the forwarded messages: `namespace_name=`, `container_name=`, and `pod_name=`. With this update, these fields are no longer added to journal logs. (link:https://issues.redhat.com/browse/[LOG-4219])

* Before this update, when a `structuredTypeKey` was not found, and a `structuredTypeName` was not specified, log messages were still parsed into structured object. With this update, parsing of logs is as expected. (link:https://issues.redhat.com/browse/LOG-4220[LOG-4220])


[id="openshift-logging-5-7-2-CVEs_{context}"]
== CVEs

* link:https://access.redhat.com/security/cve/CVE-2021-26341[CVE-2021-26341]
* link:https://access.redhat.com/security/cve/CVE-2021-33655[CVE-2021-33655]
* link:https://access.redhat.com/security/cve/CVE-2021-33656[CVE-2021-33656]
* link:https://access.redhat.com/security/cve/CVE-2022-1462[CVE-2022-1462]
* link:https://access.redhat.com/security/cve/CVE-2022-1679[CVE-2022-1679]
* link:https://access.redhat.com/security/cve/CVE-2022-1789[CVE-2022-1789]
* link:https://access.redhat.com/security/cve/CVE-2022-2196[CVE-2022-2196]
* link:https://access.redhat.com/security/cve/CVE-2022-2663[CVE-2022-2663]
* link:https://access.redhat.com/security/cve/CVE-2022-3028[CVE-2022-3028]
* link:https://access.redhat.com/security/cve/CVE-2022-3239[CVE-2022-3239]
* link:https://access.redhat.com/security/cve/CVE-2022-3522[CVE-2022-3522]
* link:https://access.redhat.com/security/cve/CVE-2022-3524[CVE-2022-3524]
* link:https://access.redhat.com/security/cve/CVE-2022-3564[CVE-2022-3564]
* link:https://access.redhat.com/security/cve/CVE-2022-3566[CVE-2022-3566]
* link:https://access.redhat.com/security/cve/CVE-2022-3567[CVE-2022-3567]
* link:https://access.redhat.com/security/cve/CVE-2022-3619[CVE-2022-3619]
* link:https://access.redhat.com/security/cve/CVE-2022-3623[CVE-2022-3623]
* link:https://access.redhat.com/security/cve/CVE-2022-3625[CVE-2022-3625]
* link:https://access.redhat.com/security/cve/CVE-2022-3627[CVE-2022-3627]
* link:https://access.redhat.com/security/cve/CVE-2022-3628[CVE-2022-3628]
* link:https://access.redhat.com/security/cve/CVE-2022-3707[CVE-2022-3707]
* link:https://access.redhat.com/security/cve/CVE-2022-3970[CVE-2022-3970]
* link:https://access.redhat.com/security/cve/CVE-2022-4129[CVE-2022-4129]
* link:https://access.redhat.com/security/cve/CVE-2022-20141[CVE-2022-20141]
* link:https://access.redhat.com/security/cve/CVE-2022-25147[CVE-2022-25147]
* link:https://access.redhat.com/security/cve/CVE-2022-25265[CVE-2022-25265]
* link:https://access.redhat.com/security/cve/CVE-2022-30594[CVE-2022-30594]
* link:https://access.redhat.com/security/cve/CVE-2022-36227[CVE-2022-36227]
* link:https://access.redhat.com/security/cve/CVE-2022-39188[CVE-2022-39188]
* link:https://access.redhat.com/security/cve/CVE-2022-39189[CVE-2022-39189]
* link:https://access.redhat.com/security/cve/CVE-2022-41218[CVE-2022-41218]
* link:https://access.redhat.com/security/cve/CVE-2022-41674[CVE-2022-41674]
* link:https://access.redhat.com/security/cve/CVE-2022-42703[CVE-2022-42703]
* link:https://access.redhat.com/security/cve/CVE-2022-42720[CVE-2022-42720]
* link:https://access.redhat.com/security/cve/CVE-2022-42721[CVE-2022-42721]
* link:https://access.redhat.com/security/cve/CVE-2022-42722[CVE-2022-42722]
* link:https://access.redhat.com/security/cve/CVE-2022-43750[CVE-2022-43750]
* link:https://access.redhat.com/security/cve/CVE-2022-47929[CVE-2022-47929]
* link:https://access.redhat.com/security/cve/CVE-2023-0394[CVE-2023-0394]
* link:https://access.redhat.com/security/cve/CVE-2023-0461[CVE-2023-0461]
* link:https://access.redhat.com/security/cve/CVE-2023-1195[CVE-2023-1195]
* link:https://access.redhat.com/security/cve/CVE-2023-1582[CVE-2023-1582]
* link:https://access.redhat.com/security/cve/CVE-2023-2491[CVE-2023-2491]
* link:https://access.redhat.com/security/cve/CVE-2023-22490[CVE-2023-22490]
* link:https://access.redhat.com/security/cve/CVE-2023-23454[CVE-2023-23454]
* link:https://access.redhat.com/security/cve/CVE-2023-23946[CVE-2023-23946]
* link:https://access.redhat.com/security/cve/CVE-2023-25652[CVE-2023-25652]
* link:https://access.redhat.com/security/cve/CVE-2023-25815[CVE-2023-25815]
* link:https://access.redhat.com/security/cve/CVE-2023-27535[CVE-2023-27535]
* link:https://access.redhat.com/security/cve/CVE-2023-29007[CVE-2023-29007]
