// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-pipelines-as-code-with-github-webhook_{context}"]
= Using {pac} with GitHub Webhook

[role="_abstract"]
Use {pac} with GitHub Webhook on your repository if you cannot create a GitHub App. However, using {pac} with GitHub Webhook does not give you access to the GitHub Check Runs API. The status of the tasks is added as comments on the pull request and is unavailable under the *Checks* tab.

[NOTE]
====
{pac} with GitHub Webhook does not support GitOps comments such as `/retest` and `/ok-to-test`. To restart the continuous integration (CI), create a new commit to the repository. For example, to create a new commit without any changes, you can use the following command:

[source,terminal]
----
$ git --amend -a --no-edit && git push --force-with-lease <origin> <branchname>
----
====

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* For authorization, create a personal access token on GitHub.

** To generate a secure and fine-grained token, restrict its scope to a specific repository and grant the following permissions:
+
.Permissions for fine-grained tokens
[options="header"]
|===

| Name | Access

| Administration | Read-only

| Metadata | Read-only

| Content | Read-only

| Commit statuses | Read and Write

| Pull request | Read and Write

| Webhooks | Read and Write

|===

** To use classic tokens, set the scope as `public_repo` for public repositories and `repo` for private repositories. In addition, provide a short token expiration period and note the token in an alternate location.
+
[NOTE]
====
If you want to configure the webhook using the `tkn pac` CLI, add the `admin:repo_hook` scope.
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
? Enter the Git repository url (default: https://github.com/owner/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository owner-repo has been created in repo-pipelines namespace
✓ Setting up GitHub Webhook for Repository https://github.com/owner/repo
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
? Please enter the secret to configure the webhook for payload validation (default: sJNwdmTifHTs):  sJNwdmTifHTs
ℹ ️You now need to create a GitHub personal access token, please checkout the docs at https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token for the required scopes
? Please enter the GitHub access token:  ****************************************
✓ Webhook has been created on repository owner/repo
🔑 Webhook Secret owner-repo has been created in the repo-pipelines namespace.
🔑 Repository CR owner-repo has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ We have detected your repository using the programming language Go.
✓ A basic template has been created in /home/Go/src/github.com/owner/repo/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On your GitHub repository or organization, perform the following steps:

.... Go to *Settings* –> *Webhooks* and click *Add webhook*.

.... Set the *Payload URL* to the {pac} controller public URL.

.... Select the content type as *application/json*.

.... Add a webhook secret and note it in an alternate location. With `openssl` installed on your local machine, generate a random secret.
+
[source,terminal]
----
$ openssl rand -hex 20
----

.... Click *Let me select individual events* and select these events: *Commit comments*, *Issue comments*, *Pull request*, and *Pushes*.

.... Click *Add webhook*.

... On your OpenShift cluster, create a `Secret` object with the personal access token and webhook secret.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic github-webhook-config \
  --from-literal provider.token="<GITHUB_PERSONAL_ACCESS_TOKEN>" \
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
  url: "https://github.com/owner/repo"
  git_provider:
    secret:
      name: "github-webhook-config"
      key: "provider.token" # Set this if you have a different key in your secret
    webhook_secret:
      name: "github-webhook-config"
      key: "webhook.secret" # Set this if you have a different key for your secret
----
+
[NOTE]
====
{pac} assumes that the OpenShift `Secret` object and the `Repository` CR are in the same namespace.
====

. Optional: For an existing `Repository` CR, add multiple GitHub Webhook secrets or provide a substitute for a deleted secret.

.. Add a webhook using the `tkn pac` CLI tool.
+
.Example: Additional webhook using the `tkn pac` CLI
[source,terminal]
----
$ tkn pac webhook add -n repo-pipelines
----
+
.Sample interactive output
[source,terminal]
----
✓ Setting up GitHub Webhook for Repository https://github.com/owner/repo
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
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
# ...
  git_provider:
    secret:
      name: "github-webhook-config"
# ...
----

... Use the `oc patch` command to update the values of the `$NEW_TOKEN` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret github-webhook-config -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----
