:_mod-docs-content-type: ASSEMBLY
[id="cluster-logging-exported-fields"]
= Log Record Fields
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: cluster-logging-exported-fields

toc::[]

The following fields can be present in log records exported by the {logging}. Although log records are typically formatted as JSON objects, the same data model can be applied to other encodings.

To search these fields from Elasticsearch and Kibana, use the full dotted field name when searching. For example, with an Elasticsearch */_search URL*, to look for a Kubernetes pod name, use `/_search/q=kubernetes.pod_name:name-of-my-pod`.

// The logging system can parse JSON-formatted log entries to external systems. These log entries are formatted as a fluentd message with extra fields such as `kubernetes`. The fields exported by the logging system and available for searching from Elasticsearch and Kibana are documented at the end of this document.

include::modules/cluster-logging-exported-fields-top-level-fields.adoc[leveloffset=0]

include::modules/cluster-logging-exported-fields-kubernetes.adoc[leveloffset=0]

// add modules/cluster-logging-exported-fields-openshift when available
