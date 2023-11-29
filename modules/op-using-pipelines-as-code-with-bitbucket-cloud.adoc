// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-pipelines-as-code-with-bitbucket-cloud_{context}"]
= Using {pac} with Bitbucket Cloud

[role="_abstract"]
If your organization or project uses Bitbucket Cloud as the preferred platform, you can use {pac} for your repository with a webhook on Bitbucket Cloud.

[discrete]
.Prerequisites

* Ensure that {pac} is installed on the cluster.

* Create an app password on Bitbucket Cloud.

** Check the following boxes to add appropriate permissions to the token:
*** Account: `Email`, `Read`
*** Workspace membership: `Read`, `Write`
*** Projects: `Read`, `Write`
*** Issues: `Read`, `Write`
*** Pull requests: `Read`, `Write`
+
[NOTE]
====
* If you want to configure the webhook using the `tkn pac` CLI, add the `Webhooks`: `Read` and `Write` permission to the token.

* Once generated, save a copy of the password or token in an alternate location.
====

[discrete]
.Procedure

. Configure the webhook and create a `Repository` CR.

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
? Enter the Git repository url (default: https://bitbucket.org/workspace/repo):
? Please enter the namespace where the pipeline should run (default: repo-pipelines):
! Namespace repo-pipelines is not found
? Would you like me to create the namespace repo-pipelines? Yes
✓ Repository workspace-repo has been created in repo-pipelines namespace
✓ Setting up Bitbucket Webhook for Repository https://bitbucket.org/workspace/repo
? Please enter your bitbucket cloud username:  <username>
ℹ ️You now need to create a Bitbucket Cloud app password, please checkout the docs at https://is.gd/fqMHiJ for the required permissions
? Please enter the Bitbucket Cloud app password:  ************************************
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
✓ Webhook has been created on repository workspace/repo
🔑 Webhook Secret workspace-repo has been created in the repo-pipelines namespace.
🔑 Repository CR workspace-repo has been updated with webhook secret in the repo-pipelines namespace
ℹ Directory .tekton has been created.
✓ A basic template has been created in /home/Go/src/bitbucket/repo/.tekton/pipelinerun.yaml, feel free to customize it.
----

** To configure a webhook and create a `Repository` CR _manually_, perform the following steps:

... On your OpenShift cluster, extract the public URL of the {pac} controller.
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

... On Bitbucket Cloud, perform the following steps:

.... Use the left navigation pane of your Bitbucket Cloud repository to go to *Repository settings* –> *Webhooks* and click *Add webhook*.

.... Set a *Title*. For example, "Pipelines as Code".

.... Set the *URL* to the {pac} controller public URL.

.... Select these events: *Repository: Push*, *Pull Request: Created*, *Pull Request: Updated*, and *Pull Request: Comment created*.

.... Click *Save*.

... On your OpenShift cluster, create a `Secret` object with the app password in the target namespace.
+
[source,terminal]
----
$ oc -n target-namespace create secret generic bitbucket-cloud-token \
  --from-literal provider.token="<BITBUCKET_APP_PASSWORD>"
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
  url: "https://bitbucket.com/workspace/repo"
  branch: "main"
  git_provider:
    user: "<BITBUCKET_USERNAME>" <1>
    secret:
      name: "bitbucket-cloud-token" <2>
      key: "provider.token" # Set this if you have a different key in your secret
----
<1> You can only reference a user by the `ACCOUNT_ID` in an owner file.
<2> {pac} assumes that the secret referred in the `git_provider.secret` spec and the `Repository` CR is in the same namespace.

+
[NOTE]
====
* The `tkn pac create` and `tkn pac bootstrap` commands are not supported on Bitbucket Cloud.

* Bitbucket Cloud does not support webhook secrets. To secure the payload and prevent hijacking of the CI, {pac} fetches the list of Bitbucket Cloud IP addresses and ensures that the webhook receptions come only from those IP addresses.
** To disable the default behavior, set the `bitbucket-cloud-check-source-ip` parameter to `false` in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.
** To allow additional safe IP addresses or networks, add them as comma separated values to the `bitbucket-cloud-additional-source-ip` parameter in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.
====

. Optional: For an existing `Repository` CR, add multiple Bitbucket Cloud Webhook secrets or provide a substitute for a deleted secret.

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
✓ Setting up Bitbucket Webhook for Repository https://bitbucket.org/workspace/repo
? Please enter your bitbucket cloud username:  <username>
👀 I have detected a controller url: https://pipelines-as-code-controller-openshift-pipelines.apps.example.com
? Do you want me to use it? Yes
✓ Webhook has been created on repository workspace/repo
🔑 Secret workspace-repo has been updated with webhook secret in the repo-pipelines namespace.
----
+
[NOTE]
====
Use the `[-n <namespace>]` option with the `tkn pac webhook add` command only when the `Repository` CR exists in a namespace other than the default namespace.
====

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
+
[NOTE]
====
Use the `[-n <namespace>]` option with the `tkn pac webhook update-token` command only when the `Repository` CR exists in a namespace other than the default namespace.
====

** Alternatively, update the personal access token by modifying the `Repository` CR.

... Find the name of the secret in the `Repository` CR.
+
[source,yaml]
----
...
spec:
  git_provider:
    user: "<BITBUCKET_USERNAME>"
    secret:
      name: "bitbucket-cloud-token"
      key: "provider.token"
...
----

... Use the `oc patch` command to update the values of the `$password` in the `$target_namespace` namespace.
+
[source,terminal]
----
$ oc -n $target_namespace patch secret bitbucket-cloud-token -p "{\"data\": {\"provider.token\": \"$(echo -n $NEW_TOKEN|base64 -w0)\"}}"
----
