// Module included in the following assemblies:
//
// * metering/metering-installing-metering.adoc
// * metering/metering-using-metering.adoc

[id="metering-overview_{context}"]
= Metering overview

Metering is a general purpose data analysis tool that enables you to write reports to process data from different data sources. As a cluster administrator, you can use metering to analyze what is happening in your cluster. You can either write your own, or use predefined SQL queries to define how you want to process data from the different data sources you have available.

Metering focuses primarily on in-cluster metric data using Prometheus as a default data source, enabling users of metering to do reporting on pods, namespaces, and most other Kubernetes resources.

You can install metering on {product-title} 4.x clusters and above.

[id="metering-resources_{context}"]
== Metering resources

Metering has many resources which can be used to manage the deployment and installation of metering, as well as the reporting functionality metering provides.

Metering is managed using the following custom resource definitions (CRDs):

[cols="1,7"]
|===

|*MeteringConfig* |Configures the metering stack for deployment. Contains customizations and configuration options to control each component that makes up the metering stack.

|*Report* |Controls what query to use, when, and how often the query should be run, and where to store the results.

|*ReportQuery* |Contains the SQL queries used to perform analysis on the data contained within `ReportDataSource` resources.

|*ReportDataSource* |Controls the data available to `ReportQuery` and `Report` resources. Allows configuring access to different databases for use within metering.

|===
