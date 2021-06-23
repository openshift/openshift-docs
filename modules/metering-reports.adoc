// Module included in the following assemblies:
//
// * metering/metering-about-reports.adoc
[id="metering-reports_{context}"]
= Reports

The `Report` custom resource is used to manage the execution and status of reports. Metering produces reports derived from usage data sources, which can be used in further analysis and filtering. A single `Report` resource represents a job that manages a database table and updates it with new information according to a schedule. The report exposes the data in that table via the Reporting Operator HTTP API.

Reports with a `spec.schedule` field set are always running and track what time periods it has collected data for. This ensures that if metering is shutdown or unavailable for an extended period of time, it backfills the data starting where it left off. If the schedule is unset, then the report runs once for the time specified by the `reportingStart` and `reportingEnd`. By default, reports wait for `ReportDataSource` resources to have fully imported any data covered in the reporting period. If the report has a schedule, it waits to run until the data in the period currently being processed has finished importing.

[id="metering-example-report-with-schedule_{context}"]
== Example report with a schedule

The following example `Report` object contains information on every pod's CPU requests, and runs every hour, adding the last hours worth of data each time it runs.

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: pod-cpu-request-hourly
spec:
  query: "pod-cpu-request"
  reportingStart: "2021-07-01T00:00:00Z"
  schedule:
    period: "hourly"
    hourly:
      minute: 0
      second: 0
----

[id="metering-example-report-without-schedule_{context}"]
== Example report without a schedule (run-once)

The following example `Report` object contains information on every pod's CPU requests for all of July. After completion, it does not run again.

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: pod-cpu-request-hourly
spec:
  query: "pod-cpu-request"
  reportingStart: "2021-07-01T00:00:00Z"
  reportingEnd: "2021-07-31T00:00:00Z"
----

[id="metering-query_{context}"]
== query

The `query` field names the `ReportQuery` resource used to generate the report. The report query controls the schema of the report as well as how the results are processed.

*`query` is a required field.*

Use the following command to list available `ReportQuery` resources:

[source,terminal]
----
$ oc -n openshift-metering get reportqueries
----

.Example output
[source,terminal]
----
NAME                                         AGE
cluster-cpu-capacity                         23m
cluster-cpu-capacity-raw                     23m
cluster-cpu-usage                            23m
cluster-cpu-usage-raw                        23m
cluster-cpu-utilization                      23m
cluster-memory-capacity                      23m
cluster-memory-capacity-raw                  23m
cluster-memory-usage                         23m
cluster-memory-usage-raw                     23m
cluster-memory-utilization                   23m
cluster-persistentvolumeclaim-request        23m
namespace-cpu-request                        23m
namespace-cpu-usage                          23m
namespace-cpu-utilization                    23m
namespace-memory-request                     23m
namespace-memory-usage                       23m
namespace-memory-utilization                 23m
namespace-persistentvolumeclaim-request      23m
namespace-persistentvolumeclaim-usage        23m
node-cpu-allocatable                         23m
node-cpu-allocatable-raw                     23m
node-cpu-capacity                            23m
node-cpu-capacity-raw                        23m
node-cpu-utilization                         23m
node-memory-allocatable                      23m
node-memory-allocatable-raw                  23m
node-memory-capacity                         23m
node-memory-capacity-raw                     23m
node-memory-utilization                      23m
persistentvolumeclaim-capacity               23m
persistentvolumeclaim-capacity-raw           23m
persistentvolumeclaim-phase-raw              23m
persistentvolumeclaim-request                23m
persistentvolumeclaim-request-raw            23m
persistentvolumeclaim-usage                  23m
persistentvolumeclaim-usage-raw              23m
persistentvolumeclaim-usage-with-phase-raw   23m
pod-cpu-request                              23m
pod-cpu-request-raw                          23m
pod-cpu-usage                                23m
pod-cpu-usage-raw                            23m
pod-memory-request                           23m
pod-memory-request-raw                       23m
pod-memory-usage                             23m
pod-memory-usage-raw                         23m
----

Report queries with the `-raw` suffix are used by other `ReportQuery` resources to build more complex queries, and should not be used directly for reports.

`namespace-` prefixed queries aggregate pod CPU and memory requests by namespace, providing a list of namespaces and their overall usage based on resource requests.

`pod-` prefixed queries are similar to `namespace-` prefixed queries but aggregate information by pod rather than namespace. These queries include the pod's namespace and node.

`node-` prefixed queries return information about each node's total available resources.

`aws-` prefixed queries are specific to AWS. Queries suffixed with `-aws` return the same data as queries of the same name without the suffix, and correlate usage with the EC2 billing data.

The `aws-ec2-billing-data` report is used by other queries, and should not be used as a standalone report. The `aws-ec2-cluster-cost` report provides a total cost based on the nodes included in the cluster, and the sum of their costs for the time period being reported on.

Use the following command to get the `ReportQuery` resource as YAML, and check the `spec.columns` field. For example, run:

[source,terminal]
----
$ oc -n openshift-metering get reportqueries namespace-memory-request -o yaml
----

.Example output
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: ReportQuery
metadata:
  name: namespace-memory-request
  labels:
    operator-metering: "true"
spec:
  columns:
  - name: period_start
    type: timestamp
    unit: date
  - name: period_end
    type: timestamp
    unit: date
  - name: namespace
    type: varchar
    unit: kubernetes_namespace
  - name: pod_request_memory_byte_seconds
    type: double
    unit: byte_seconds
----

[id="metering-schedule_{context}"]
== schedule

The `spec.schedule` configuration block defines when the report runs. The main fields in the `schedule` section are `period`, and then depending on the value of `period`, the fields `hourly`, `daily`, `weekly`, and `monthly` allow you to fine-tune when the report runs.

For example, if `period` is set to `weekly`, you can add a `weekly` field to the `spec.schedule` block. The following example will run once a week on Wednesday, at 1 PM (hour 13 in the day).

[source,yaml]
----
...
  schedule:
    period: "weekly"
    weekly:
      dayOfWeek: "wednesday"
      hour: 13
...
----

[id="metering-period_{context}"]
=== period

Valid values of `schedule.period` are listed below, and the options available to set for a given period are also listed.

* `hourly`
** `minute`
** `second`
* `daily`
** `hour`
** `minute`
** `second`
* `weekly`
** `dayOfWeek`
** `hour`
** `minute`
** `second`
* `monthly`
** `dayOfMonth`
** `hour`
** `minute`
** `second`
* `cron`
** `expression`

Generally, the `hour`, `minute`, `second` fields control when in the day the report runs, and `dayOfWeek`/`dayOfMonth` control what day of the week, or day of month the report runs on, if it is a weekly or monthly report period.

For each of these fields, there is a range of valid values:

* `hour` is an integer value between 0-23.
* `minute` is an integer value between 0-59.
* `second` is an integer value between 0-59.
* `dayOfWeek` is a string value that expects the day of the week (spelled out).
* `dayOfMonth` is an integer value between 1-31.

For cron periods, normal cron expressions are valid:

* `expression: "*/5 * * * *"`

[id="metering-reportingStart_{context}"]
== reportingStart

To support running a report against existing data, you can set the `spec.reportingStart` field to a link:https://tools.ietf.org/html/rfc3339#section-5.8[RFC3339 timestamp] to tell the report to run according to its `schedule` starting from `reportingStart` rather than the current time.

[NOTE]
====
Setting the `spec.reportingStart` field to a specific time will result in the Reporting Operator running many queries in succession for each interval in the schedule that is between the `reportingStart` time and the current time. This could be thousands of queries if the period is less than daily and the `reportingStart` is more than a few months back. If `reportingStart` is left unset, the report will run at the next full `reportingPeriod` after the time the report is created.
====

As an example of how to use this field, if you had data already collected dating back to January 1st, 2019 that you want to include in your `Report` object, you can create a report with the following values:

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: pod-cpu-request-hourly
spec:
  query: "pod-cpu-request"
  schedule:
    period: "hourly"
  reportingStart: "2021-01-01T00:00:00Z"
----

[id="metering-reportingEnd_{context}"]
== reportingEnd

To configure a report to only run until a specified time, you can set the `spec.reportingEnd` field to an link:https://tools.ietf.org/html/rfc3339#section-5.8[RFC3339 timestamp]. The value of this field will cause the report to stop running on its schedule after it has finished generating reporting data for the period covered from its start time until `reportingEnd`.

Because a schedule will most likely not align with the `reportingEnd`, the last period in the schedule will be shortened to end at the specified `reportingEnd` time. If left unset, then the report will run forever, or until a `reportingEnd` is set on the report.

For example, if you want to create a report that runs once a week for the month of July:

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: pod-cpu-request-hourly
spec:
  query: "pod-cpu-request"
  schedule:
    period: "weekly"
  reportingStart: "2021-07-01T00:00:00Z"
  reportingEnd: "2021-07-31T00:00:00Z"
----

[id="metering-expiration_{context}"]
== expiration

Add the `expiration` field to set a retention period on a scheduled metering report. You can avoid manually removing the report by setting the `expiration` duration value. The retention period is equal to the `Report` object `creationDate` plus the `expiration` duration. The report is removed from the cluster at the end of the retention period if no other reports or report queries depend on the expiring report. Deleting the report from the cluster can take several minutes.

[NOTE]
====
Setting the `expiration` field is not recommended for roll-up or aggregated reports. If a report is depended upon by other reports or report queries, then the report is not removed at the end of the retention period. You can view the `report-operator` logs at debug level for the timing output around a report retention decision.
====

For example, the following scheduled report is deleted 30 minutes after the `creationDate` of the report:

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: pod-cpu-request-hourly
spec:
  query: "pod-cpu-request"
  schedule:
    period: "weekly"
  reportingStart: "2021-07-01T00:00:00Z"
  expiration: "30m" <1>
----
<1> Valid time units for the `expiration` duration are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.

[NOTE]
====
The `expiration` retention period for a `Report` object is not precise and works on the order of several minutes, not nanoseconds.
====

[id="metering-runImmediately_{context}"]
== runImmediately

When `runImmediately` is set to `true`, the report runs immediately. This behavior ensures that the report is immediately processed and queued without requiring additional scheduling parameters.

[NOTE]
====
When `runImmediately` is set to `true`, you must set a `reportingEnd` and `reportingStart` value.
====

[id="metering-inputs_{context}"]
== inputs

The `spec.inputs` field of a `Report` object can be used to override or set values defined in a `ReportQuery` resource's `spec.inputs` field.

`spec.inputs` is a list of name-value pairs:

[source,yaml]
----
spec:
  inputs:
  - name: "NamespaceCPUUsageReportName" <1>
    value: "namespace-cpu-usage-hourly" <2>
----

<1> The `name` of an input must exist in the ReportQuery's `inputs` list.
<2> The `value` of the input must be the correct type for the input's `type`.

// TODO(chance): include modules/metering-reportquery-inputs.adoc module

[id="metering-roll-up-reports_{context}"]
== Roll-up reports

Report data is stored in the database much like metrics themselves, and therefore, can be used in aggregated or roll-up reports. A simple use case for a roll-up report is to spread the time required to produce a report over a longer period of time. This is instead of requiring a monthly report to query and add all data over an entire month. For example, the task can be split into daily reports that each run over 1/30 of the data.

A custom roll-up report requires a custom report query. The `ReportQuery` resource template processor provides a `reportTableName` function that can get the necessary table name from a `Report` object's `metadata.name`.

Below is a snippet taken from a built-in query:

.pod-cpu.yaml
[source,yaml]
----
spec:
...
  inputs:
  - name: ReportingStart
    type: time
  - name: ReportingEnd
    type: time
  - name: NamespaceCPUUsageReportName
    type: Report
  - name: PodCpuUsageRawDataSourceName
    type: ReportDataSource
    default: pod-cpu-usage-raw
...

  query: |
...
    {|- if .Report.Inputs.NamespaceCPUUsageReportName |}
      namespace,
      sum(pod_usage_cpu_core_seconds) as pod_usage_cpu_core_seconds
    FROM {| .Report.Inputs.NamespaceCPUUsageReportName | reportTableName |}
...
----

.Example `aggregated-report.yaml` roll-up report
[source,yaml]
----
spec:
  query: "namespace-cpu-usage"
  inputs:
  - name: "NamespaceCPUUsageReportName"
    value: "namespace-cpu-usage-hourly"
----

// TODO(chance): replace the comment below with an include on the modules/metering-rollup-report.adoc
// For more information on setting up a roll-up report, see the [roll-up report guide](rollup-reports.md).

[id="metering-report-status_{context}"]
=== Report status

The execution of a scheduled report can be tracked using its status field. Any errors occurring during the preparation of a report will be recorded here.

The `status` field of a `Report` object currently has two fields:

* `conditions`: Conditions is a list of conditions, each of which have a `type`, `status`, `reason`, and `message` field. Possible values of a condition's `type` field are `Running` and `Failure`, indicating the current state of the scheduled report. The `reason` indicates why its `condition` is in its current state with the `status` being either `true`, `false` or, `unknown`. The `message` provides a human readable indicating why the condition is in the current state. For detailed information on the `reason` values, see link:https://github.com/operator-framework/operator-metering/blob/master/pkg/apis/metering/v1/util/report_util.go#L10[`pkg/apis/metering/v1/util/report_util.go`].
* `lastReportTime`: Indicates the time metering has collected data up to.
