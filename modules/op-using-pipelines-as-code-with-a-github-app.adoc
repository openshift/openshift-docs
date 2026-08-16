// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="using-pipelines-as-code-with-a-github-app_{context}"]
= Using {pac} with a GitHub App

[role="_abstract"]
GitHub Apps act as a point of integration with {pipelines-title} and bring the advantage of Git-based workflows to {pipelines-shortname}. Cluster administrators can configure a single GitHub App for all cluster users. For GitHub Apps to work with {pac}, ensure that the webhook of the GitHub App points to the {pac} event listener route (or ingress endpoint) that listens for GitHub events.

[NOTE]
====
When importing an application using *Import from Git* and the Git repository has a `.tekton` directory, you can configure `pipelines-as-code` for your application.
====


[id="configuring-github-app-for-pac"]
== Configuring a GitHub App

Cluster administrators can create a GitHub App by running the following command:

[source,terminal]
----
$ tkn pac bootstrap github-app
----

If the `tkn pac` CLI plugin is not installed, you can create the GitHub App manually.

.Procedure

To create and configure a GitHub App manually for {pac}, perform the following steps:

. Sign in to your GitHub account.

. Go to **Settings** -> **Developer settings** -> **GitHub Apps**, and click **New GitHub App**.

. Provide the following information in the GitHub App form:

* **GitHub Application Name**: `{pipelines-shortname}`
* **Homepage URL**: OpenShift Console URL
* **Webhook URL**: The {pac} route or ingress URL. You can find it by running the following command:
+
[source,terminal]
----
$ echo https://$(oc get route -n openshift-pipelines pipelines-as-code-controller -o jsonpath='{.spec.host}')
----

* **Webhook secret**: An arbitrary secret. You can generate a secret by running the following command:
+
[source,terminal]
----
$ openssl rand -hex 20
----

. Select the following **Repository permissions**:

* **Checks**: `Read & Write`
* **Contents**: `Read & Write`
* **Issues**: `Read & Write`
* **Metadata**: `Read-only`
* **Pull request**: `Read & Write`

. Select the following **Organization permissions**:

* **Members**: `Readonly`
* **Plan**: `Readonly`

. Select the following **User permissions**:

* **Check run**
* **Issue comment**
* **Pull request**
* **Push**

. Click **Create GitHub App**.

. On the **Details** page of the newly created GitHub App, note the **App ID** displayed at the top.

. In the **Private keys** section, click **Generate Private key** to automatically generate and download a private key for the GitHub app. Securely store the private key for future reference and usage.

. Install the created App on a repository that you want to use with {pac}.


[id="configuring-pac-for-github-app"]
== Configuring {pac} to access a GitHub App

To configure {pac} to access the newly created GitHub App, execute the following command:

[source,terminal]
----
$ oc -n openshift-pipelines create secret generic pipelines-as-code-secret \
        --from-literal github-private-key="$(cat <PATH_PRIVATE_KEY>)" \ <1>
        --from-literal github-application-id="<APP_ID>" \ <2>
        --from-literal webhook.secret="<WEBHOOK_SECRET>" <3>
----
<1> The path to the private key you downloaded while configuring the GitHub App.
<2> The **App ID** of the GitHub App.
<3> The webhook secret provided when you created the GitHub App.


[NOTE]
====
{pac} works automatically with GitHub Enterprise by detecting the header set from GitHub Enterprise and using it for the GitHub Enterprise API authorization URL.
====

