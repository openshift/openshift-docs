// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="creating-pipeline-run-using-pipelines-as-code_{context}"]
= Creating a pipeline run using {pac}

[role="_abstract"]
To run pipelines using {pac}, you can create pipelines definitions or templates as YAML files in the `.tekton/` directory of the repository. You can reference YAML files in other repositories using remote URLs, but pipeline runs are only triggered by events in the repository containing the `.tekton/` directory.

The {pac} resolver bundles the pipeline runs with all tasks as a single pipeline run without external dependencies.

[NOTE]
====
* For pipelines, use at least one pipeline run with a spec, or a separated `Pipeline` object.
* For tasks, embed task spec inside a pipeline, or define it separately as a Task object.
====

[discrete]
.Parameterizing commits and URLs

You can specify the parameters of your commit and URL by using dynamic, expandable variables with the {{<var>}} format. Currently, you can use the following variables:

* `{{repo_owner}}`: The repository owner.
* `{{repo_name}}`: The repository name.
* `{{repo_url}}`: The repository full URL.
* `{{revision}}`: Full SHA revision of a commit.
* `{{sender}}`: The username or account id of the sender of the commit.
* `{{source_branch}}`: The branch name where the event originated.
* `{{target_branch}}`: The branch name that the event targets. For push events, it's the same as the `source_branch`.
* `{{pull_request_number}}`: The pull or merge request number, defined only for a `pull_request` event type.
* `{{git_auth_secret}}`: The secret name that is generated automatically with Git provider's token for checking out private repos.

[discrete]
.Matching an event to a pipeline run

You can match different Git provider events with each pipeline by using special annotations on the pipeline run. If there are multiple pipeline runs matching an event, {pac} runs them in parallel and posts the results to the Git provider as soon a pipeline run finishes.

[discrete]
.Matching a pull event to a pipeline run

You can use the following example to match the `pipeline-pr-main` pipeline with a `pull_request` event that targets the `main` branch:

[source,yaml]
----
...
  metadata:
    name: pipeline-pr-main
  annotations:
    pipelinesascode.tekton.dev/on-target-branch: "[main]" <1>
    pipelinesascode.tekton.dev/on-event: "[pull_request]"
...
----
<1> You can specify multiple branches by adding comma-separated entries. For example, `"[main, release-nightly]"`. In addition, you can specify the following:
* Full references to branches such as `"refs/heads/main"`
* Globs with pattern matching such as `"refs/heads/\*"`
* Tags such as `"refs/tags/1.\*"`

[discrete]
.Matching a push event to a pipeline run

You can use the following example to match the `pipeline-push-on-main` pipeline with a `push` event targeting the `refs/heads/main` branch:

[source,yaml]
----
...
  metadata:
    name: pipeline-push-on-main
  annotations:
    pipelinesascode.tekton.dev/on-target-branch: "[refs/heads/main]" <1>
    pipelinesascode.tekton.dev/on-event: "[push]"
...
----
<1> You can specifiy multiple branches by adding comma-separated entries. For example, `"[main, release-nightly]"`. In addition, you can specify the following:
* Full references to branches such as `"refs/heads/main"`
* Globs with pattern matching such as `"refs/heads/\*"`
* Tags such as `"refs/tags/1.\*"`

[discrete]
.Advanced event matching

{pac} supports using Common Expression Language (CEL) based filtering for advanced event matching. If you have the `pipelinesascode.tekton.dev/on-cel-expression` annotation in your pipeline run, {pac} uses the CEL expression and skips the `on-target-branch` annotation. Compared to the simple `on-target-branch` annotation matching, the CEL expressions allow complex filtering and negation.

To use CEL-based filtering with {pac}, consider the following examples of annotations:

* To match a `pull_request` event targeting the `main` branch and coming from the `wip` branch:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && target_branch == "main" && source_branch == "wip"
...
----

* To run a pipeline only if a path has changed, you can use the `.pathChanged` suffix function with a glob pattern:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && "docs/\*.md".pathChanged() <1>
...
----
<1> Matches all markdown files in the `docs` directory.

* To match all pull requests starting with the title `[DOWNSTREAM]`:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request && event_title.startsWith("[DOWNSTREAM]")
...
----

* To run a pipeline on a `pull_request` event, but skip the `experimental` branch:
+
[source,yaml]
----
...
  pipelinesascode.tekton.dev/on-cel-expression: |
    event == "pull_request" && target_branch != experimental"
...
----

For advanced CEL-based filtering while using {pac}, you can use the following fields and suffix functions:

* `event`: A `push` or `pull_request` event.
* `target_branch`: The target branch.
* `source_branch`: The branch of origin of a `pull_request` event. For `push` events, it is same as the `target_branch`.
* `event_title`: Matches the title of the event, such as the commit title for a `push` event, and the title of a pull or merge request for a `pull_request` event. Currently, only GitHub, Gitlab, and Bitbucket Cloud are the supported providers.
* `.pathChanged`: A suffix function to a string. The string can be a glob of a path to check if the path has changed. Currently, only GitHub and Gitlab are supported as providers.

[discrete]
.Using the temporary GitHub App token for Github API operations

You can use the temporary installation token generated by {pac} from GitHub App to access the GitHub API. The token value is stored in the temporary `{{git_auth_secret}}` dynamic variable generated for private repositories in the `git-provider-token` key.

For example, to add a comment to a pull request, you can use the `github-add-comment` task from {tekton-hub} using a {pac} annotation:

[source,yaml]
----
...
  pipelinesascode.tekton.dev/task: "github-add-comment"
...
----

You can then add a task to the `tasks` section or `finally` tasks in the pipeline run definition:

[source,yaml]
----
[...]
tasks:
  - name:
      taskRef:
        name: github-add-comment
      params:
        - name: REQUEST_URL
          value: "{{ repo_url }}/pull/{{ pull_request_number }}" <1>
        - name: COMMENT_OR_FILE
          value: "Pipelines as Code IS GREAT!"
        - name: GITHUB_TOKEN_SECRET_NAME
          value: "{{ git_auth_secret }}"
        - name: GITHUB_TOKEN_SECRET_KEY
          value: "git-provider-token"
...
----
<1> By using the dynamic variables, you can reuse this snippet template for any pull request from any repository.

[NOTE]
====
On GitHub Apps, the generated installation token is available for 8 hours and scoped to the repository from where the events originate unless configured differently on the cluster.
====

