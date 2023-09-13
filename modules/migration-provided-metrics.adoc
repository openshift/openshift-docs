// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/troubleshooting-3-4.adoc
// * migration-toolkit-for-containers/troubleshooting-mtc.adoc

[id="migration-provided-metrics_{context}"]
= Provided metrics

The `MigrationController` custom resource (CR) provides metrics for the `MigMigration` CR count and for its API requests.

[id="cam_app_workload_migrations-metric_{context}"]
== cam_app_workload_migrations

This metric is a count of `MigMigration` CRs over time. It is useful for viewing alongside the `mtc_client_request_count` and `mtc_client_request_elapsed` metrics to collate API request information with migration status changes. This metric is included in Telemetry.

.cam_app_workload_migrations metric
[%header,cols="3,3,3"]
|===
|Queryable label name |Sample label values |Label description

|status
|`running`, `idle`, `failed`, `completed`
|Status of the `MigMigration` CR

|type
|stage, final
|Type of the `MigMigration` CR
|===

[id="mtc_client_request_count-metric_{context}"]
== mtc_client_request_count

This metric is a cumulative count of Kubernetes API requests that `MigrationController` issued. It is not included in Telemetry.

.mtc_client_request_count metric
[%header,cols="3,3,3"]
|===
|Queryable label name |Sample label values |Label description

|cluster
|`\https://migcluster-url:443`
|Cluster that the request was issued against

|component
|`MigPlan`, `MigCluster`
|Sub-controller API that issued request

|function
|`(*ReconcileMigPlan).Reconcile`
|Function that the request was issued from

|kind
|`SecretList`, `Deployment`
|Kubernetes kind the request was issued for
|===

[id="mtc_client_request_elapsed-metric_{context}"]
== mtc_client_request_elapsed

This metric is a cumulative latency, in milliseconds, of Kubernetes API requests that `MigrationController` issued. It is not included in Telemetry.

.mtc_client_request_elapsed metric
[%header,cols="3,3,3"]
|===
|Queryable label name |Sample label values |Label description

|cluster
|`\https://cluster-url.com:443`
|Cluster that the request was issued against

|component
|`migplan`, `migcluster`
|Sub-controller API that issued request

|function
|`(*ReconcileMigPlan).Reconcile`
|Function that the request was issued from

|kind
|`SecretList`, `Deployment`
|Kubernetes resource that the request was issued for
|===

[id="useful-queries_{context}"]
== Useful queries

The table lists some helpful queries that can be used for monitoring performance.

.Useful queries

[%header,cols="3,3"]
|===
|Query |Description

|`mtc_client_request_count`
|Number of API requests issued, sorted by request type

|`sum(mtc_client_request_count)`
|Total number of API requests issued

|`mtc_client_request_elapsed`
|API request latency, sorted by request type

|`sum(mtc_client_request_elapsed)`
|Total latency of API requests

|`sum(mtc_client_request_elapsed) / sum(mtc_client_request_count)`
|Average latency of API requests

|`mtc_client_request_elapsed / mtc_client_request_count`
|Average latency of API requests, sorted by request type

|`cam_app_workload_migrations{status="running"} * 100`
|Count of running migrations, multiplied by 100 for easier viewing alongside request counts
|===
