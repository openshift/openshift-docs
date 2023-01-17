// Module included in the following assemblies:
//
// * cli_reference/osdk/cli-osdk-ref.adoc
// * operators/operator_sdk/osdk-cli-ref.adoc

[id="osdk-cli-ref-init_{context}"]
= init

The `operator-sdk init` command initializes an Operator project and generates, or _scaffolds_, a default project directory layout for the given plugin.

This command writes the following files:

* Boilerplate license file
* `PROJECT` file with the domain and repository
* `Makefile` to build the project
* `go.mod` file with project dependencies
* `kustomization.yaml` file for customizing manifests
* Patch file for customizing images for manager manifests
* Patch file for enabling Prometheus metrics
* `main.go` file to run

.`init` flags
[options="header",cols="1,3"]
|===
|Flag |Description

|`--help, -h`
|Help output for the `init` command.

|`--plugins` (string)
|Name and optionally version of the plugin to initialize the project with. Available plugins are `ansible.sdk.operatorframework.io/v1`, `go.kubebuilder.io/v2`, `go.kubebuilder.io/v3`, and `helm.sdk.operatorframework.io/v1`.

|`--project-version`
|Project version. Available values are `2` and `3-alpha`, which is the default.
|===
