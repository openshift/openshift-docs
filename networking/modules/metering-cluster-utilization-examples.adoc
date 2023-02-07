// Module included in the following assemblies:
//
// * metering/metering-usage-examples.adoc

[id="metering-cluster-utilization-examples_{context}"]
= Measure cluster utilization using cron expressions

You can also use cron expressions when configuring the period of your reports. The following report measures cluster utilization by looking at CPU utilization from 9am-5pm every weekday.

.Weekday CPU utilization by cluster example

[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: cluster-cpu-utilization-weekdays <1>
spec:
  query: "cluster-cpu-utilization" <2>
  schedule:
   period: "cron"
   expression: 0 0 * * 1-5 <3>
----
<1> To say organized, remember to change the `name` of your report if you change any of the other values.
<2> Adjust your query here. You can also measure cluster utilization with the `cluster-memory-utilization` query.
<3> For cron periods, normal cron expressions are valid.
