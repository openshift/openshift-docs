:_mod-docs-content-type: ASSEMBLY
[id="metering-about-reports"]
= About Reports
include::_attributes/common-attributes.adoc[]
:context: metering-about-reports

toc::[]

:FeatureName: Metering
include::modules/deprecated-feature.adoc[leveloffset=+1]

A `Report` custom resource provides a method to manage periodic Extract Transform and Load (ETL) jobs using SQL queries. Reports are composed from other metering resources, such as `ReportQuery` resources that provide the actual SQL query to run, and `ReportDataSource` resources that define the data available to the `ReportQuery` and `Report` resources.

Many use cases are addressed by the predefined `ReportQuery` and `ReportDataSource` resources that come installed with metering. Therefore, you do not need to define your own unless you have a use case that is not covered by these predefined resources.

include::modules/metering-reports.adoc[leveloffset=+1]
