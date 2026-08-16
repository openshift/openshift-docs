:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="serverless-controller-metrics"]
= {ServerlessProductShortName} controller metrics
:context: serverless-controller-metrics

The following metrics are emitted by any component that implements a controller logic. These metrics show details about reconciliation operations and the work queue behavior upon which reconciliation requests are added to the work queue.

[cols=5*,options="header"]
|===
|Metric name
|Description
|Type
|Tags
|Unit

|`work_queue_depth`
|The depth of the work queue.
|Gauge
|`reconciler`
|Integer (no units)

|`reconcile_count`
|The number of reconcile operations.
|Counter
|`reconciler`, `success`
|Integer (no units)

|`reconcile_latency`
|The latency of reconcile operations.
|Histogram
|`reconciler`, `success`
|Milliseconds

|`workqueue_adds_total`
|The total number of add actions handled by the work queue.
|Counter
|`name`
|Integer (no units)

|`workqueue_queue_latency_seconds`
|The length of time an item stays in the work queue before being requested.
|Histogram
|`name`
|Seconds

|`workqueue_retries_total`
|The total number of retries that have been handled by the work queue.
|Counter
|`name`
|Integer (no units)

|`workqueue_work_duration_seconds`
|The length of time it takes to process and item from the work queue.
|Histogram
|`name`
|Seconds

|`workqueue_unfinished_work_seconds`
|The length of time that outstanding work queue items have been in progress.
|Histogram
|`name`
|Seconds

|`workqueue_longest_running_processor_seconds`
|The length of time that the longest outstanding work queue items has been in progress.
|Histogram
|`name`
|Seconds
|===
