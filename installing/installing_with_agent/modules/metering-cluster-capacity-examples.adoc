// Module included in the following assemblies:
//
// * metering/metering-usage-examples.adoc

[id="metering-cluster-capacity-examples_{context}"]
= Measure cluster capacity hourly and daily

The following report demonstrates how to measure cluster capacity both hourly and daily. The daily report works by aggregating the hourly report's results.

The following report measures cluster CPU capacity every hour.

.Hourly CPU capacity by cluster example

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: cluster-cpu-capacity-hourly
spec:
  query: "cluster-cpu-capacity"
  schedule:
    period: "hourly" <1>
----
<1> You could change this period to `daily` to get a daily report, but with larger data sets it is more efficient to use an hourly report, then aggregate your hourly data into a daily report.

The following report aggregates the hourly data into a daily report.

.Daily CPU capacity by cluster example

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: cluster-cpu-capacity-daily <1>
spec:
  query: "cluster-cpu-capacity" <2>
  inputs: <3>
  - name: ClusterCpuCapacityReportName
    value: cluster-cpu-capacity-hourly
  schedule:
    period: "daily"
----

<1> To stay organized, remember to change the `name` of your report if you change any of the other values.
<2> You can also measure `cluster-memory-capacity`. Remember to update the query in the associated hourly report as well.
<3> The `inputs` section configures this report to aggregate the hourly report. Specifically, `value: cluster-cpu-capacity-hourly` is the name of the hourly report that gets aggregated.
