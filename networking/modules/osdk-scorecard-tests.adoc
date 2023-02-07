// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-scorecard.adoc

[id="osdk-scorecard-tests_{context}"]
= Built-in scorecard tests

The scorecard ships with pre-defined tests that are arranged into suites: the basic test suite and the Operator Lifecycle Manager (OLM) suite.

[id="osdk-scorecard-basic-tests_{context}"]
.Basic test suite
[cols="3,7,3",options="header"]
|===
|Test |Description |Short name

|Spec Block Exists
|This test checks the custom resource (CR) created in the cluster to make sure that all CRs have a `spec` block.
|`basic-check-spec-test`
|===

[id="osdk-scorecard-olm-tests_{context}"]
.OLM test suite

[cols="3,7,3",options="header"]
|===
|Test |Description |Short name

|Bundle Validation
|This test validates the bundle manifests found in the bundle that is passed into scorecard. If the bundle contents contain errors, then the test result output includes the validator log as well as error messages from the validation library.
|`olm-bundle-validation-test`

|Provided APIs Have Validation
|This test verifies that the custom resource definitions (CRDs) for the provided CRs contain a validation section and that there is validation for each `spec` and `status` field detected in the CR.
|`olm-crds-have-validation-test`

|Owned CRDs Have Resources Listed
|This test makes sure that the CRDs for each CR provided via the `cr-manifest` option have a `resources` subsection in the `owned` CRDs section of the ClusterServiceVersion (CSV). If the test detects used resources that are not listed in the resources section, it lists them in the suggestions at the end of the test. Users are required to fill out the resources section after initial code generation for this test to pass.
|`olm-crds-have-resources-test`

|Spec Fields With Descriptors
|This test verifies that every field in the CRs `spec` sections has a corresponding descriptor listed in the CSV.
|`olm-spec-descriptors-test`

|Status Fields With Descriptors
|This test verifies that every field in the CRs `status` sections have a corresponding descriptor listed in the CSV.
|`olm-status-descriptors-test`
|===
