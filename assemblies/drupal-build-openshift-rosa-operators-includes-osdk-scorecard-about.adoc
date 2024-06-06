// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-scorecard.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-about-scorecard_{context}"]
= About the scorecard tool

While the Operator SDK `bundle validate` subcommand can validate local bundle directories and remote bundle images for content and structure, you can use the `scorecard` command to run tests on your Operator based on a configuration file and test images. These tests are implemented within test images that are configured and constructed to be executed by the scorecard.

The scorecard assumes it is run with access to a configured Kubernetes cluster, such as {product-title}. The scorecard runs each test within a pod, from which pod logs are aggregated and test results are sent to the console. The scorecard has built-in basic and Operator Lifecycle Manager (OLM) tests and also provides a means to execute custom test definitions.

.Scorecard workflow
. Create all resources required by any related custom resources (CRs) and the Operator
. Create a proxy container in the deployment of the Operator to record calls to the API server and run tests
. Examine parameters in the CRs

The scorecard tests make no assumptions as to the state of the Operator being tested. Creating Operators and CRs for an Operators are beyond the scope of the scorecard itself. Scorecard tests can, however, create whatever resources they require if the tests are designed for resource creation.

.`scorecard` command syntax
[source,terminal]
----
$ operator-sdk scorecard <bundle_dir_or_image> [flags]
----

The scorecard requires a positional argument for either the on-disk path to
your Operator bundle or the name of a bundle image.

For further information about the flags, run:

[source,terminal]
----
$ operator-sdk scorecard -h
----
