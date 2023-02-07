// Module included in the following assemblies:
//
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc

[id="osdk-helm-existing-chart_{context}"]
= Existing Helm charts

Instead of creating your project with a boilerplate Helm chart, you can alternatively use an existing chart, either from your local file system or a remote chart repository, by using the following flags:

* `--helm-chart`
* `--helm-chart-repo`
* `--helm-chart-version`

If the `--helm-chart` flag is specified, the `--group`, `--version`, and `--kind` flags become optional. If left unset, the following default values are used:

[options="header"]
|===
|Flag |Value

|`--domain`
|`my.domain`

|`--group`
|`charts`

|`--version`
|`v1`

|`--kind`
|Deduced from the specified chart
|===

If the `--helm-chart` flag specifies a local chart archive, for example `example-chart-1.2.0.tgz`, or directory, the chart is validated and unpacked or copied into the project. Otherwise, the Operator SDK attempts to fetch the chart from a remote repository.

If a custom repository URL is not specified by the `--helm-chart-repo` flag, the following chart reference formats are supported:

[cols="1,4",options="header"]
|===
|Format |Description

|`<repo_name>/<chart_name>`
|Fetch the Helm chart named `<chart_name>` from the helm chart repository named `<repo_name>`, as specified in the `$HELM_HOME/repositories/repositories.yaml` file. Use the `helm repo add` command to configure this file.

|`<url>`
|Fetch the Helm chart archive at the specified URL.
|===

If a custom repository URL is specified by `--helm-chart-repo`, the following chart reference format is supported:

[cols="1,4",options="header"]
|===
|Format |Description

|`<chart_name>`
|Fetch the Helm chart named `<chart_name>` in the Helm chart repository specified by the `--helm-chart-repo` URL value.
|===

If the `--helm-chart-version` flag is unset, the Operator SDK fetches the latest available version of the Helm chart. Otherwise, it fetches the specified version. The optional `--helm-chart-version` flag is not used when the chart specified with the `--helm-chart` flag refers to a specific version, for example when it is a local path or a URL.

For more details and examples, run:

[source,terminal]
----
$ operator-sdk init --plugins helm --help
----
