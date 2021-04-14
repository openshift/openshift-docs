// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-configuring-csv-composition_{context}"]
= CSV composition configuration

Operator authors can configure CSV composition by populating several fields in the `deploy/olm-catalog/csv-config.yaml` file:

[cols="2a,8a",options="header"]
|===
|Field |Description

|`operator-path` (string)
|The Operator resource manifest file path. Default: `deploy/operator.yaml`.

|`crd-cr-path-list` (string(, string)*)
|A list of CRD and CR manifest file paths. Default: `[deploy/crds/*_{crd,cr}.yaml]`.

|`rbac-path-list` (string(, string)*)
|A list of RBAC role manifest file paths. Default: `[deploy/role.yaml]`.
|===
