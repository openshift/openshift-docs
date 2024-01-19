// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-private-repositories-with-pipelines-as-code_{context}"]
= Using private repositories with {pac}

[role="_abstract"]
{pac} supports private repositories by creating or updating a secret in the target namespace with the user token. The `git-clone` task from {tekton-hub} uses the user token to clone private repositories.

Whenever {pac} creates a new pipeline run in the target namespace, it creates or updates a secret with the  `pac-gitauth-<REPOSITORY_OWNER>-<REPOSITORY_NAME>-<RANDOM_STRING>` format.

You must reference the secret with the `basic-auth` workspace in your pipeline run and pipeline definitions, which is then passed on to the `git-clone` task.

[source,yaml]
----
...
  workspace:
  - name: basic-auth
    secret:
      secretName: "{{ git_auth_secret }}"
...
----

In the pipeline, you can reference the `basic-auth` workspace for the `git-clone` task to reuse:

[source,yaml]
----
...
workspaces:
  - name basic-auth
params:
    - name: repo_url
    - name: revision
...
tasks:
  workspaces:
    - name: basic-auth
      workspace: basic-auth
  ...
  tasks:
  - name: git-clone-from-catalog
      taskRef:
        name: git-clone <1>
      params:
        - name: url
          value: $(params.repo_url)
        - name: revision
          value: $(params.revision)
...
----
<1> The `git-clone` task picks up the `basic-auth` workspace and uses it to clone the private repository.

You can modify this configuration by setting the `secret-auto-create` parameter to either a `false` or `true` value, as required, in the `TektonConfig` custom resource, in the `pipelinesAsCode.settings` spec.
