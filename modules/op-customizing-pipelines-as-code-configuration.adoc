// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="customizing-pipelines-as-code-configuration_{context}"]
= Customizing {pac} configuration

[role="_abstract"]
To customize {pac}, cluster administrators can configure the following parameters in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec:

.Customizing {pac} configuration
[options="header"]
|===

| Parameter | Description | Default

| `application-name` | The name of the application. For example, the name displayed in the GitHub Checks labels. | `"Pipelines as Code CI"`

| `secret-auto-create` | Indicates whether or not a secret should be automatically created using the token generated in the GitHub application. This secret can then be used with private repositories. | `enabled`

| `remote-tasks` | When enabled, allows remote tasks from pipeline run annotations. | `enabled`

| `hub-url` | The base URL for the link:https://api.hub.tekton.dev/v1[Tekton Hub API]. | `https://hub.tekton.dev/`

| `hub-catalog-name` | The Tekton Hub catalog name. | `tekton`

| `tekton-dashboard-url` | The URL of the Tekton Hub dashboard. {pac} uses this URL to generate a `PipelineRun` URL on the Tekton Hub dashboard.  | NA

| `bitbucket-cloud-check-source-ip` | Indicates whether to secure the service requests by querying IP ranges for a public Bitbucket. Changing the parameter's default value might result into a security issue. | `enabled`

| `bitbucket-cloud-additional-source-ip` | Indicates whether to provide an additional set of IP ranges or networks, which are separated by commas. | NA

| `max-keep-run-upper-limit` | A maximum limit for the `max-keep-run` value for a pipeline run. | NA

| `default-max-keep-runs` | A default limit for the `max-keep-run` value for a pipeline run. If defined, the value is applied to all pipeline runs that do not have a `max-keep-run` annotation. | NA

| `auto-configure-new-github-repo` | Configures new GitHub repositories automatically. {pac} sets up a namespace and creates a custom resource for your repository. This parameter is only supported with GitHub applications. | `disabled`

| `auto-configure-repo-namespace-template` | Configures a template to automatically generate the namespace for your new repository, if `auto-configure-new-github-repo` is enabled. | `{repo_name}-pipelines`

| `error-log-snippet` | Enables or disables the view of a log snippet for the failed tasks, with an error in a pipeline. You can disable this parameter in the case of data leakage from your pipeline. | `true`

| `error-detection-from-container-logs` | Enables or disables the inspection of container logs to detect error message and expose them as annotations on the pull request. This setting applies only if you are using the GitHub app. | `true`

| `error-detection-max-number-of-lines` | The maximum number of lines inspected in the container logs to search for error messages. Set to `-1` to inspect an unlimited number of lines. | 50

| `secret-github-app-token-scoped` | If set to `true`, the GitHub access token that {pac} generates using the GitHub app is scoped only to the repository from which {pac} fetches the pipeline definition. If set to `false`, you can use both the `TektonConfig` custom resource and the `Repository` custom resource to scope the token to additional repositories. | `true`

| `secret-github-app-scope-extra-repos` | Additional repositories for scoping the generated GitHub access token. |


|===
