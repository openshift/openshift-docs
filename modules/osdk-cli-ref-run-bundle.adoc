// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

:_mod-docs-content-type: REFERENCE
[id="osdk-cli-ref-run-bundle_{context}"]
= bundle

The `run bundle` subcommand deploys an Operator in the bundle format with Operator Lifecycle Manager (OLM).

.`run bundle` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`--index-image` (string)
|Index image in which to inject a bundle. The default image is `quay.io/operator-framework/upstream-opm-builder:latest`.

|`--install-mode <install_mode_value>`
|Install mode supported by the cluster service version (CSV) of the Operator, for example `AllNamespaces` or `SingleNamespace`.

|`--timeout <duration>`
|Install timeout. The default value is `2m0s`.

|`--kubeconfig` (string)
|Path to the `kubeconfig` file to use for CLI requests.

|`-n`, `--namespace` (string)
|If present, namespace in which to run the CLI request.

|`--security-context-config <security_context>`
|Specifies the security context to use for the catalog pod. Allowed values include `restricted` and `legacy`. The default value is `legacy`. ^[1]^

|`-h`, `--help`
|Help output for the `run bundle` subcommand.

|===
[.small]
--
1. The `restricted` security context is not compatible with the `default` namespace. To configure your Operator's pod security admission in your production environment, see "Complying with pod security admission". For more information about pod security admission, see "Understanding and managing pod security admission".
--
