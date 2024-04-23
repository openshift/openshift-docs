:_mod-docs-content-type: ASSEMBLY
[id="using-pipelines-as-code"]
= Using {pac}
include::_attributes/common-attributes.adoc[]
:context: using-pipelines-as-code

toc::[]


// :FeatureName: Pipelines as Code
[role="_abstract"]
With {pac}, cluster administrators and users with the required privileges can define pipeline templates as part of source code Git repositories. When triggered by a source code push or a pull request for the configured Git repository, {pac} runs the pipeline and reports the status.

[id="pac-key-features"]
== Key features
{pac} supports the following features:

* Pull request status and control on the platform hosting the Git repository.
* GitHub Checks API to set the status of a pipeline run, including rechecks.
* GitHub pull request and commit events.
* Pull request actions in comments, such as `/retest`.
* Git events filtering and a separate pipeline for each event.
* Automatic task resolution in {pipelines-shortname}, including local tasks, Tekton Hub, and remote URLs.
* Retrieval of configurations using GitHub blobs and objects API.
* Access Control List (ACL) over a GitHub organization, or using a Prow style `OWNER` file.
* The `tkn pac` CLI plugin for managing bootstrapping and {pac} repositories.
* Support for GitHub App, GitHub Webhook, Bitbucket Server, and Bitbucket Cloud.

include::modules/op-installing-pipelines-as-code-on-an-openshift-cluster.adoc[leveloffset=+1]

include::modules/op-installing-pipelines-as-code-cli.adoc[leveloffset=+1]

[id="using-pipelines-as-code-with-a-git-repository-hosting-service-provider"]
== Using {pac} with a Git repository hosting service provider

[role="_abstract"]
After installing {pac}, cluster administrators can configure a Git repository hosting service provider. Currently, the following services are supported:

* GitHub App
* GitHub Webhook
* GitLab
* Bitbucket Server
* Bitbucket Cloud

[NOTE]
====
GitHub App is the recommended service for using with {pac}.
====

include::modules/op-using-pipelines-as-code-with-a-github-app.adoc[leveloffset=+1]

include::modules/op-creating-a-github-application-in-administrator-perspective.adoc[leveloffset=+2]

include::modules/op-scoping-github-token.adoc[leveloffset=+2]

include::modules/op-using-pipelines-as-code-with-github-webhook.adoc[leveloffset=+1]

.Additional resources

* link:https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks[GitHub Webhook documentation on GitHub]
* link:https://docs.github.com/en/rest/guides/getting-started-with-the-checks-api[GitHub Check Runs documentation on GitHub]
* link:https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token[Creating a personal access token on GitHub]
* link:https://github.com/settings/tokens/new?description=pipelines-as-code-token&scopes=repo[Classic tokens with pre-filled permissions]

include::modules/op-using-pipelines-as-code-with-gitlab.adoc[leveloffset=+1]

.Additional resources

* link:https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html[GitLab Webhook documentation on GitLab]

include::modules/op-using-pipelines-as-code-with-bitbucket-cloud.adoc[leveloffset=+1]

.Additional resources

* link:https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/[Creating app password on Bitbucket Cloud]
* link:https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#introducing-atlassian-account-id-and-nicknames[Introducing Altassian Account ID and Nicknames]

include::modules/op-using-pipelines-as-code-with-bitbucket-server.adoc[leveloffset=+1]

.Additional resources

* link:https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html[Creating personal tokens on Bitbucket Server]
* link:https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/#Create-webhooks[Creating webhooks on Bitbucket server]

include::modules/op-interfacing-pipelines-as-code-with-custom-certificates.adoc[leveloffset=+1]

.Additional resources

* xref:../../networking/enable-cluster-wide-proxy.adoc#nw-proxy-configure-object[Enabling the cluster-wide proxy]

include::modules/op-using-repository-crd-with-pipelines-as-code.adoc[leveloffset=+1]

include::modules/op-setting-concurrency-limits-in-repository-crd.adoc[leveloffset=+2]

include::modules/op-changing-source-branch-in-repository-crd.adoc[leveloffset=+2]

include::modules/op-custom-parameter-expansion.adoc[leveloffset=+2]

include::modules/op-using-pipelines-as-code-resolver.adoc[leveloffset=+1]

include::modules/op-using-remote-task-annotations-with-pipelines-as-code.adoc[leveloffset=+2]

include::modules/op-using-remote-pipeline-annotations-with-pipelines-as-code.adoc[leveloffset=+2]

include::modules/op-creating-pipeline-run-using-pipelines-as-code.adoc[leveloffset=+1]

.Additional resources

* link:https://github.com/google/cel-spec/blob/master/doc/langdef.md[CEL language specification]

include::modules/op-running-pipeline-run-using-pipelines-as-code.adoc[leveloffset=+1]

include::modules/op-monitoring-pipeline-run-status-using-pipelines-as-code.adoc[leveloffset=+1]

.Additional resources

* link:https://github.com/chmouel/tekton-slack-task-status[An example task to send Slack messages on success or failure]
* link:https://github.com/openshift-pipelines/pipelines-as-code/blob/7b41cc3f769af40a84b7ead41c6f037637e95070/.tekton/push.yaml[An example of a pipeline run with `finally` tasks triggered on push events]

include::modules/op-using-private-repositories-with-pipelines-as-code.adoc[leveloffset=+1]

.Additional resources

* link:https://github.com/openshift-pipelines/pipelines-as-code/blob/main/test/testdata/pipelinerun_git_clone_private.yaml[An example of the `git-clone` task used for cloning private repositories]

include::modules/op-cleaning-up-pipeline-run-using-pipelines-as-code.adoc[leveloffset=+1]

include::modules/op-using-incoming-webhook-with-pipelines-as-code.adoc[leveloffset=+1]

include::modules/op-customizing-pipelines-as-code-configuration.adoc[leveloffset=+1]

include::modules/op-pipelines-as-code-command-reference.adoc[leveloffset=+1]

include::modules/op-splitting-pipelines-as-code-logs-by-namespace.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources-pac"]
== Additional resources

* link:https://github.com/openshift-pipelines/pipelines-as-code/tree/main/.tekton[An example of the `.tekton/` directory in the Pipelines as Code repository]

* xref:../../cicd/pipelines/installing-pipelines.adoc#installing-pipelines[Installing {pipelines-shortname}]

* xref:../../cli_reference/tkn_cli/installing-tkn.adoc#installing-tkn[Installing tkn]

* xref:../../cicd/pipelines/op-release-notes.adoc#op-release-notes[{pipelines-title} release notes]

* xref:../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-creating-applications-using-the-developer-perspective[Creating applications using the Developer perspective]
