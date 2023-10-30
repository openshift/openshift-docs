// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-bundle-validate.adoc

:_mod-docs-content-type: REFERENCE
[id="osdk-bundle-validate-tests_{context}"]
= Built-in bundle validate tests

The Operator SDK ships with pre-defined validators arranged into suites. If you run the `bundle validate` command without specifying a validator, the default test runs. The default test verifies that a bundle adheres to the specifications defined by the Operator Framework community. For more information, see "Bundle format".

You can run optional validators to test for issues such as OperatorHub compatibility or deprecated Kubernetes APIs. Optional validators always run in addition to the default test.

.`bundle validate` command syntax for optional test suites
[source,terminal]
----
$ operator-sdk bundle validate <bundle_dir_or_image>
  --select-optional <test_label>
----

[id="osdk-bundle-validate-additional-tests_{context}"]
.Addtional `bundle validate` validators
[cols="3,7,3",options="header"]
|===
|Name |Description |Label

|Operator Framework
|This validator tests an Operator bundle against the entire suite of validators provided by the Operator Framework.
|`suite=operatorframework`

|OperatorHub
|This validator tests an Operator bundle for compatibility with OperatorHub.
|`name=operatorhub`

|Good Practices
|This validator tests whether an Operator bundle complies with good practices as defined by the Operator Framework. It checks for issues, such as an empty CRD description or unsupported Operator Lifecycle Manager (OLM) resources.
|`name=good-practices`
|===
