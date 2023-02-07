// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-generate-kustomize_{context}"]
= kustomize

The `generate kustomize` subcommand contains subcommands that generate link:https://kustomize.io/[Kustomize] data for the Operator.

[id="osdk-cli-ref-generate-kustomize-manifests_{context}"]
== manifests

The `generate kustomize manifests` subcommand generates or regenerates Kustomize bases and a `kustomization.yaml` file in the `config/manifests` directory, which are used to build bundle manifests by other Operator SDK commands. This command interactively asks for UI metadata, an important component of manifest bases, by default unless a base already exists or you set the `--interactive=false` flag.

.`generate kustomize manifests` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`--apis-dir` (string)
|Root directory for API type definitions.

|`-h`, `--help`
|Help for `generate kustomize manifests`.

|`--input-dir` (string)
|Directory containing existing Kustomize files.

|`--interactive`
|When set to `false`, if no Kustomize base exists, an interactive command prompt is presented to accept custom metadata.

|`--output-dir` (string)
|Directory where to write Kustomize files.

|`--package` (string)
|Package name.

|`-q`, `--quiet`
|Run in quiet mode.

|===
