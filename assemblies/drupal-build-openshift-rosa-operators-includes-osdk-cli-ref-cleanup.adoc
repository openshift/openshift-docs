// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

:_mod-docs-content-type: REFERENCE
[id="osdk-cli-ref-cleanup_{context}"]
= cleanup

The `operator-sdk cleanup` command destroys and removes resources that were created for an Operator that was deployed with the `run` command.

.`cleanup` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`-h`, `--help`
|Help output for the `run bundle` subcommand.

|`--kubeconfig` (string)
|Path to the `kubeconfig` file to use for CLI requests.

|`-n`, `--namespace` (string)
|If present, namespace in which to run the CLI request.

|`--timeout <duration>`
|Time to wait for the command to complete before failing. The default value is `2m0s`.

|===
