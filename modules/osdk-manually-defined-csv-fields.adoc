// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-manually-defined-csv-fields_{context}"]
= Manually-defined CSV fields

Many CSV fields cannot be populated using generated, generic manifests that are not specific to Operator SDK. These fields are mostly human-written metadata about the Operator and various custom resource definitions (CRDs).

Operator authors must directly modify their cluster service version (CSV) YAML file, adding personalized data to the following required fields. The Operator SDK gives a warning during CSV generation when a lack of data in any of the required fields is detected.

The following tables detail which manually-defined CSV fields are required and which are optional.

.Required CSV fields
[cols="2a,8a",options="header"]
|===
|Field |Description

|`metadata.name`
|A unique name for this CSV. Operator version should be included in the name to ensure uniqueness, for example `app-operator.v0.1.1`.

|`metadata.capabilities`
|The capability level according to the Operator maturity model. Options include `Basic Install`, `Seamless Upgrades`, `Full Lifecycle`, `Deep Insights`, and `Auto Pilot`.

|`spec.displayName`
|A public name to identify the Operator.

|`spec.description`
|A short description of the functionality of the Operator.

|`spec.keywords`
|Keywords describing the Operator.

|`spec.maintainers`
|Human or organizational entities maintaining the Operator, with a `name` and `email`.

|`spec.provider`
|The provider of the Operator (usually an organization), with a `name`.

|`spec.labels`
|Key-value pairs to be used by Operator internals.

|`spec.version`
|Semantic version of the Operator, for example `0.1.1`.

|`spec.customresourcedefinitions`
|Any CRDs the Operator uses. This field is populated automatically by the Operator SDK if any CRD YAML files are present in `deploy/`. However, several fields not in the CRD manifest spec require user input:

- `description`: description of the CRD.
- `resources`: any Kubernetes resources leveraged by the CRD, for example `Pod` and `StatefulSet` objects.
- `specDescriptors`: UI hints for inputs and outputs of the Operator.
|===


.Optional CSV fields
[cols="2a,8a",options="header"]
|===
|Field |Description

|`spec.replaces`
|The name of the CSV being replaced by this CSV.

|`spec.links`
|URLs (for example, websites and documentation) pertaining to the Operator or application being managed, each with a `name` and `url`.

|`spec.selector`
|Selectors by which the Operator can pair resources in a cluster.

|`spec.icon`
|A base64-encoded icon unique to the Operator, set in a `base64data` field with a `mediatype`.

|`spec.maturity`
|The level of maturity the software has achieved at this version. Options include `planning`, `pre-alpha`, `alpha`, `beta`, `stable`, `mature`, `inactive`, and `deprecated`.

|`metadata.annotations`
|===

Further details on what data each field above should hold are found in the link:https://github.com/operator-framework/operator-lifecycle-manager/blob/master/doc/design/building-your-csv.md[CSV spec].

[NOTE]
====
Several YAML fields currently requiring user intervention can potentially be parsed from Operator code.
====
