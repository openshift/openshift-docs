// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-generating-a-csv_{context}"]
= Generating a CSV

.Prerequisites

- An Operator project generated using the Operator SDK

.Procedure

. In your Operator project, configure your CSV composition by modifying the `deploy/olm-catalog/csv-config.yaml` file, if desired.

. Generate the CSV:
+
[source,terminal]
----
$ operator-sdk generate csv --csv-version <version>
----

. In the new CSV generated in the `deploy/olm-catalog/` directory, ensure all required, manually-defined fields are set appropriately.
