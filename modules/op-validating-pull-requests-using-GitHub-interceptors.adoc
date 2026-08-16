// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="op-validating-pull-requests-using-GitHub-interceptors_{context}"]
= Validating pull requests using GitHub Interceptors

You can use GitHub Interceptor to validate the processing of pull requests based on the GitHub owners configured for a repository. This validation helps you to prevent unnecessary execution of a `PipelineRun` or `TaskRun` object.
GitHub Interceptor processes a pull request only if the user name is listed as an owner or if a configurable comment is issued by an owner of the repository. For example, when you comment `/ok-to-test` on a pull request as an owner, a `PipelineRun` or `TaskRun` is triggered.

[NOTE]
====
Owners are configured in an `OWNERS` file at the root of the repository.
====

.Prerequisites
* You have installed the {pipelines-title} Operator.

.Procedure
. Create a secret string value.
. Configure the GitHub webhook with that value.
. Create a Kubernetes secret named `secretRef` that contains your secret value.
. Pass the Kubernetes secret as a reference to your GitHub Interceptor.
. Create an `owners` file and add the list of approvers into the `approvers` section.
. Perform one of the following steps:
* For a public GitHub repository, set the value of the `githubOwners` parameter to `true` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-owners-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
            - name: "secretRef"
              value:
                secretName: github-secret
                secretKey: secretToken
            - name: "eventTypes"
              value: ["pull_request", "issue_comment"]
            - name: "githubOwners"
              value:
                enabled: true
                checkType: none
...
----

* For a private GitHub repository, set the value of the `githubOwners` parameter to `true` and provide the access token details, `secretName` and `secretKey` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-owners-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
            - name: "secretRef"
              value:
                secretName: github-secret
                secretKey: secretToken
            - name: "eventTypes"
              value: ["pull_request", "issue_comment"]
            - name: "githubOwners"
              value:
                enabled: true
                personalAccessToken:
                  secretName: github-token
                  secretKey: secretToken
                checkType: all
...
----
+
[NOTE]
====
The `checkType` parameter is used to specify the GitHub owners who need authentication. You can set its value to `orgMembers`, `repoMembers`, or `all`.
====

. Save the configuration file.
