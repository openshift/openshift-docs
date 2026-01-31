// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-incoming-webhook-with-pipelines-as-code_{context}"]
= Using incoming webhook with {pac}

[role="_abstract"]
Using an incoming webhook URL and a shared secret, you can start a pipeline run in a repository.

To use incoming webhooks, specify the following within the `spec` section of the `Repository` custom resource definition (CRD):

* The incoming webhook URL that {pac} matches.
* The Git provider and the user token. Currently, {pac} supports `github`, `gitlab`, and `bitbucket-cloud`.
+
[NOTE]
====
When using incoming webhook URLs in the context of GitHub app, you must specify the token.
====
* The target branches and a secret for the incoming webhook URL.

.Example: `Repository` CRD with incoming webhook
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: repo
  namespace: ns
spec:
  url: "https://github.com/owner/repo"
  git_provider:
    type: github
    secret:
      name: "owner-token"
  incoming:
    - targets:
      - main
      secret:
        name: repo-incoming-secret
      type: webhook-url
----

.Example: The `repo-incoming-secret` secret for incoming webhook
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: repo-incoming-secret
  namespace: ns
type: Opaque
stringData:
  secret: <very-secure-shared-secret>
----

To trigger a pipeline run located in the `.tekton` directory of a Git repository, use the following command:

[source,terminal]
----
$ curl -X POST 'https://control.pac.url/incoming?secret=very-secure-shared-secret&repository=repo&branch=main&pipelinerun=target_pipelinerun'
----

{pac} matches the incoming URL and treats it as a `push` event. However, {pac} does not report status of the pipeline runs triggered by this command.

To get a report or a notification, add it directly with a `finally` task to your pipeline. Alternatively, you can inspect the `Repository` CRD with the `tkn pac` CLI tool.
