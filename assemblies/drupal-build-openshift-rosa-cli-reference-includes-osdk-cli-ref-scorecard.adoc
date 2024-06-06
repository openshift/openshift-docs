// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-scorecard_{context}"]
= scorecard

The `operator-sdk scorecard` command runs the scorecard tool to validate an Operator bundle and provide suggestions for improvements. The command takes one argument, either a bundle image or directory containing manifests and metadata. If the argument holds an image tag, the image must be present remotely.

.`scorecard` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-c`, `--config` (string)
|Path to scorecard configuration file. The default path is `bundle/tests/scorecard/config.yaml`.

|`-h`, `--help`
|Help output for the `scorecard` command.

|`--kubeconfig` (string)
|Path to `kubeconfig` file.

|`-L`, `--list`
|List which tests are available to run.

|`-n`, --namespace (string)
|Namespace in which to run the test images.

|`-o`, `--output` (string)
|Output format for results. Available values are `text`, which is the default, and `json`.

|`--pod-security <security_context>`
|Option to run scorecard with the specified security context. Allowed values include `restricted` and `legacy`. The default value is `legacy`. ^[1]^

|`-l`, `--selector` (string)
|Label selector to determine which tests are run.

|`-s`, `--service-account` (string)
|Service account to use for tests. The default value is `default`.

|`-x`, `--skip-cleanup`
|Disable resource cleanup after tests are run.

|`-w`, `--wait-time <duration>`
|Seconds to wait for tests to complete, for example `35s`. The default value is `30s`.

|===
[.small]
--
1. The `restricted` security context is not compatible with the `default` namespace. To configure your Operator's pod security admission in your production environment, see "Complying with pod security admission". For more information about pod security admission, see "Understanding and managing pod security admission".
--
