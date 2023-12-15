// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-scorecard.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-scorecard-select-tests_{context}"]
= Selecting tests

Scorecard tests are selected by setting the `--selector` CLI flag to a set of label strings. If a selector flag is not supplied, then all of the tests within the scorecard configuration file are run.

Tests are run serially with test results being aggregated by the scorecard and written to standard output, or _stdout_.

.Procedure

. To select a single test, for example `basic-check-spec-test`, specify the test by using the `--selector` flag:
+
[source,terminal]
----
$ operator-sdk scorecard <bundle_dir_or_image> \
    -o text \
    --selector=test=basic-check-spec-test
----

. To select a suite of tests, for example `olm`, specify a label that is used by all of the OLM tests:
+
[source,terminal]
----
$ operator-sdk scorecard <bundle_dir_or_image> \
    -o text \
    --selector=suite=olm
----

. To select multiple tests, specify the test names by using the `selector` flag using the following syntax:
+
[source,terminal]
----
$ operator-sdk scorecard <bundle_dir_or_image> \
    -o text \
    --selector='test in (basic-check-spec-test,olm-bundle-validation-test)'
----
