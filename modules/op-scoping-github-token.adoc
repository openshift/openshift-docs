// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: PROCEDURE
[id="scoping-github-token_{context}"]
= Scoping the GitHub token to additional repositories

{pac} uses the GitHub app to generate a GitHub access token. {pac} uses this token to retrieve the pipeline payload from the repository and to enable the CI/CD processes to interact with GitHub repositories.

By default, the access token is scoped only to the repository from which {pac} retrieves the pipeline definition. In some cases, you might want the token to have access to additional repositories. For example, there might be a CI repository where the `.tekton/pr.yaml` file and source payload are located, but the build process defined in `pr.yaml` fetches tasks from a separate private CD repository.

You can extend the scope of the GitHub token in two ways:

* _Global configuration_: You can extend the GitHub token to a list of repositories in different namespaces. You must have administrative permissions to set this configuration.
* _Repository level configuration_: You can extend the GitHub token to a list of repositories that exist in the same namespace as the original repository. You do not need administrative permissions to set this configuration.

.Procedure

. In the `TektonConfig` custom resource (CR), in the `pipelinesAsCode.settings` spec, set the `secret-github-app-token-scoped` parameter to `false`. This setting enables scoping the GitHub token to private and public repositories listed in the global and repository level configuration.

. To set global configuration for scoping the GitHub token, in the `TektonConfig` CR, in the `pipelinesAsCode.settings` spec, specify the additional repositories in the `secret-github-app-scope-extra-repos` parameter, as in the following example:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          secret-github-app-token-scoped: false
          secret-github-app-scope-extra-repos: "owner2/project2, owner3/project3"
----
+
. To set repository level configuration for scoping the GitHub token, specify the additional repositories in the `github_app_token_scope_repos` parameter of the `Repository` CR, as in the following example:
+
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: test
  namespace: test-repo
spec:
  url: "https://github.com/linda/project"
  settings:
    github_app_token_scope_repos:
    - "owner/project"
    - "owner1/project1"
----
+
In this example, the `Repository` custom resource is associated with the `linda/project` repository in the `test-repo` namespace. The scope of the generated GitHub token is extended to the `owner/project` and `owner1/project1` repositories, as well as the `linda/project` repository. These repositories must exist under the `test-repo` namespace.
+
[NOTE]
====
The additional repositories can be public or private, but must reside in the same namespace as the repository with which the `Repository` resource is associated.

If any of the repositories do not exist in the namespace, the scoping of the GitHub token fails with an error message:

[source,terminal]
----
failed to scope GitHub token as repo owner1/project1 does not exist in namespace test-repo
----
====

.Result

The generated GitHub token enables access to the additional repositories that you configured in the global and repository level configuration, as well as the original repository where the {pac} payload files are located.

If you provide both global configuration and repository level configuration, the token is scoped to all the repositories from both configurations, as in the following example.

.`TektonConfig` custom resource
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  platforms:
    openshift:
      pipelinesAsCode:
        enable: true
        settings:
          secret-github-app-token-scoped: false
          secret-github-app-scope-extra-repos: "owner2/project2, owner3/project3"
----

.`Repository` custom resource
[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
 name: test
 namespace: test-repo
spec:
 url: "https://github.com/linda/project"
 settings:
   github_app_token_scope_repos:
   - "owner/project"
   - "owner1/project1"
----

The GitHub token is scoped to the `owner/project`, `owner1/project1`, `owner2/project2`, `owner3/project3`, and `linda/project` respositories.
