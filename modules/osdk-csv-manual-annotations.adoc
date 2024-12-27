// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-csv-manual-annotations_{context}"]
= Operator metadata annotations

Operator developers can set certain annotations in the metadata of a cluster service version (CSV) to enable features or highlight capabilities in user interfaces (UIs), such as OperatorHub or the link:https://catalog.redhat.com/software/search?deployed_as=Operator[Red Hat Ecosystem Catalog]. Operator metadata annotations are manually defined by setting the `metadata.annotations` field in the CSV YAML file.