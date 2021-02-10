// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-generate-bundle_{context}"]
= bundle

The `generate bundle` subcommand generates a set of bundle manifests, metadata, and a `bundle.Dockerfile` file for your Operator project.

[NOTE]
====
Typically, you run the `generate kustomize manifests` subcommand first to generate the input link:https://kustomize.io/[Kustomize] bases that are used by the `generate bundle` subcommand. However, you can use the `make bundle` command in an initialized project to automate running these commands in sequence.
====

.`generate bundle` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`--channels` (string)
|Comma-separated list of channels to which the bundle belongs. The default value is `alpha`.

|`--crds-dir` (string)
|Root directory for `CustomResoureDefinition` manifests.

|`--default-channel` (string)
|The default channel for the bundle.

|`--deploy-dir` (string)
|Root directory for Operator manifests, such as deployments and RBAC. This directory is different from the directory passed to the `--input-dir` flag.

|`-h`, `--help`
|Help for `generate bundle`

|`--input-dir` (string)
|Directory from which to read an existing bundle. This directory is the parent of your bundle `manifests` directory and is different from the `--deploy-dir` directory.

|`--kustomize-dir` (string)
|Directory containing Kustomize bases and a `kustomization.yaml` file for bundle manifests. The default path is `config/manifests`.

|`--manifests`
|Generate bundle manifests.

|`--metadata`
|Generate bundle metadata and Dockerfile.

|`--output-dir` (string)
|Directory to write the bundle to.

|`--overwrite`
|Overwrite the bundle metadata and Dockerfile if they exist. The default value is `true`.

|`--package` (string)
|Package name for the bundle.

|`-q`, `--quiet`
|Run in quiet mode.

|`--stdout`
|Write bundle manifest to standard out.

|`--version` (string)
|Semantic version of the Operator in the generated bundle. Set only when creating a new bundle or upgrading the Operator.

|===
