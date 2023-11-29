:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="log-visualization"]
= About log visualization
:context: log-visualization

toc::[]

You can visualize your log data in the {product-title} web console, or the Kibana web console, depending on your deployed log storage solution. The Kibana console can be used with ElasticSearch log stores, and the {product-title} web console can be used with the ElasticSearch log store or the LokiStack.

include::snippets/logging-kibana-dep-snip.adoc[]

include::modules/configuring-log-visualizer.adoc[leveloffset=+1]

[id="log-visualization-resource-logs"]
== Viewing logs for a resource

Resource logs are a default feature that provides limited log viewing capability. You can view the logs for various resources, such as builds, deployments, and pods by using the {oc-first} and the web console.

[TIP]
====
To enhance your log retrieving and viewing experience, install the {logging}. The {logging} aggregates all the logs from your {product-title} cluster, such as node system audit logs, application container logs, and infrastructure logs, into a dedicated log store. You can then query, discover, and visualize your log data through the Kibana console or the {product-title} web console. Resource logs do not access the {logging} log store.
====

include::modules/viewing-resource-logs-cli-console.adoc[leveloffset=+2]
