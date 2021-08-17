// Module included in the following assemblies:
//
// * metering/metering-using-metering.adoc
[id="metering-writing-reports_{context}"]
= Writing Reports

Writing a report is the way to process and analyze data using metering.

To write a report, you must define a `Report` resource in a YAML file, specify the required parameters, and create it in the `openshift-metering` namespace.

.Prerequisites

* Metering is installed.

.Procedure

. Change to the `openshift-metering` project:
+
[source,terminal]
----
$ oc project openshift-metering
----

. Create a `Report` resource as a YAML file:
+
.. Create a YAML file with the following content:
+
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: Report
metadata:
  name: namespace-cpu-request-2020 <2>
  namespace: openshift-metering
spec:
  reportingStart: '2020-01-01T00:00:00Z'
  reportingEnd: '2020-12-30T23:59:59Z'
  query: namespace-cpu-request <1>
  runImmediately: true <3>
----
<1> The `query` specifies the `ReportQuery` resources used to generate the report. Change this based on what you want to report on. For a list of options, run `oc get reportqueries | grep -v raw`.
<2> Use a descriptive name about what the report does for `metadata.name`. A good name describes the query, and the schedule or period you used.
<3> Set `runImmediately`  to `true` for it to run with whatever data is available, or set it to `false` if you want it to wait for `reportingEnd` to pass.

.. Run the following command to create the `Report` resource:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
.Example output
[source,terminal]
----
report.metering.openshift.io/namespace-cpu-request-2020 created
----
+

. You can list reports and their `Running` status with the following command:
+
[source,terminal]
----
$ oc get reports
----
+
.Example output
[source,terminal]
----
NAME                         QUERY                   SCHEDULE   RUNNING    FAILED   LAST REPORT TIME       AGE
namespace-cpu-request-2020   namespace-cpu-request              Finished            2020-12-30T23:59:59Z   26s
----
