// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-pipelines-as-code-with-gitlab_{context}"]
= Using {pac} with GitLab

[role="_abstract"]
If your organization or project uses GitLab as the preferred platform, you can use {pac} for your repository with a webhook on GitLab.

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* For authorization, generate a personal access token as the manager of the project or organization on GitLab.
+
[NOTE]
====
* If you want to configure the webhook using the `tkn pac` CLI, add the `admin:repo_hook` scope to the token.

* Using a token scoped for a specific project cannot provide API access to a merge request (MR) sent from a forked repository. In such cases, {pac} displays the result of a pipeline as a comment on the MR.
====

[discrete]
.Procedure

. Configure the webhook and create a `Repository` custom resource (CR).

** To configure a webhook and create a `Repository` CR _automatically_ using the `tkn pac` CLI tool, use the following command:
+
[source,terminal]
----
$ tkn pac create repo
----
+
.Sample interactive output
[source,terminal]
----
? Enter the Git repository url (default: https://gitlab.com/owner/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository repositories-project has been created in repo-pipelines namespace
✓ Setting up GitLab Webhook for Repository https://gitlab.com/owner/repo
? Please enter the project ID for the repository you want to be configured,
  project ID refers to an unique ID (e.g. 34405323) shown at the top of your GitLab project : 17103
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: lFjHIEcaGFlF):  lFjHIEcaGFlF
ℹ ️You now need to create a GitLab personal access token with `api` scope
ℹ ️Go to this URL to generate one https://gitlab.com/-/profile/personal_access_tokens, see https://is.gd/rOEo9B for documentation
? Please enter the GitLab access token:  **************************
? Please enter your GitLab API URL::  https://gitlab.com
✓ Webhook has been created on your repository
🔑 Webhook Secret repositories-project has been created in the repo-pipelines namespace.
🔑 Repository CR repositories-project has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ A basic template has been created in /home/Go/src/gitlab.com/repositories/project/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On your GitLab project, perform the following steps:

.... Use the left sidebar to go to *Settings* –> *Webhooks*.

.... Set the *URL* to the {pac} controller public URL.

.... Add a webhook secret and note it in an alternate location. With `openssl` installed on your local machine, generate a random secret.
+
[source,terminal]
----
$ openssl rand -hex 20
----

.... Click *Let me select individual events* and select these events: *Commit comments*, *Issue comments*, *Pull request*, and *Pushes*.

.... Click *Save changes*.

... On your OpenShift cluster, create a `Secret` object with the personal access token and webhook secret.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic gitlab-webhook-config \
  --from-literal provider.token="<GITLAB_PERSONAL_ACCESS_TOKEN>" \
  --from-literal webhook.secret="<WEBHOOK_SECRET>"
----

... Create a `Repository` CR.
+
.Example: `Repository` CR
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
  url: "https://gitlab.com/owner/repo" <1>
  git_provider:
    secret:
      name: "gitlab-webhook-config"
      key: "provider.token" # Set this if you have a different key in your secret
    webhook_secret:
      name: "gitlab-webhook-config"
      key: "webhook.secret" # Set this if you have a different key for your secret
----
<1> Currently, {pac} does not automatically detects private instances for GitLab. In such cases, specify the API URL under the `git_provider.url` spec. In general, you can use the `git_provider.url` spec to manually override the API URL.

+
[NOTE]
====
* {pac} assumes that the OpenShift `Secret` object and the `Repository` CR are in the same namespace.
====

. Optional: For an existing `Repository` CR, add multiple GitLab Webhook secrets or provide a substitute for a deleted secret.

.. Add a webhook using the `tkn pac` CLI tool.
+
.Example: Adding additional webhook using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook add -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
✓ Setting up GitLab Webhook for Repository https://gitlab.com/owner/repo
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: AeHdHTJVfAeH):  AeHdHTJVfAeH
✓ Webhook has been created on repository owner/repo
🔑 Secret owner-repo has been updated with webhook secert in the repo-pipelines namespace.
----

.. Update the `webhook.secret` key in the existing OpenShift `Secret` object.

. Optional: For an existing `Repository` CR, update the personal access token.

** Update the personal access token using the `tkn pac` CLI tool.
+
.Example: Updating personal access token using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook update-token -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
? Please enter your personal access token:  ****************************************
🔑 Secret owner-repo has been updated with new personal access token in the repo-pipelines namespace.
----

** Alternatively, update the personal access token by modifying the `Repository` CR.

... Find the name of the secret in the `Repository` CR.
+
[source,yaml]
----
...
spec:
  git_provider:
    secret:
      name: "gitlab-webhook-config"
...
----

... Use the `oc patch` command to update the values of the `$NEW_TOKEN` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret gitlab-webhook-config -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----

