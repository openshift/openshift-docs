:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-webhook-metrics"]
= Webhook metrics
:context: serverless-webhook-metrics

Webhook metrics report useful information about operations. For example, if a large number of operations fail, this might indicate an issue with a user-created resource.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`request_count`
|The number of requests that are routed to the webhook.
|Counter
|`admission_allowed`, `kind_group`, `kind_kind`, `kind_version`, `request_operation`, `resource_group`, `resource_namespace`, `resource_resource`, `resource_version`
|Integer (no units)

|`request_latencies`
|The response time for a webhook request.
|Histogram
|`admission_allowed`, `kind_group`, `kind_kind`, `kind_version`, `request_operation`, `resource_group`, `resource_namespace`, `resource_resource`, `resource_version`
|Milliseconds
|===
