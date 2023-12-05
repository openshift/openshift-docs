// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="op-filtering-pull-requests-using-GitHub-interceptor_{context}"]
= Filtering pull requests using GitHub Interceptor

You can filter GitHub events based on the files that have been changed for push and pull events. This helps you to execute a pipeline for only relevant changes in your Git repository.
GitHub Interceptor adds a comma delimited list of all files that have been changed and uses the CEL Interceptor to filter incoming events based on the changed files. The list of changed files is added to the `changed_files` property of the event payload in the top-level  `extensions` field.

.Prerequisites
* You have installed the {pipelines-title} Operator.

.Procedure
. Perform one of the following steps:
* For a public GitHub repository, set the value of the `addChangedFiles` parameter to `true` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-add-changed-files-pr-listener
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
            value: ["pull_request", "push"]
          - name: "addChangedFiles"
            value:
              enabled: true
        - ref:
            name: cel
          params:
          - name: filter
            value: extensions.changed_files.matches('controllers/')
...
----

* For a private GitHub repository, set the value of the `addChangedFiles` parameter to `true` and provide the access token details, `secretName` and `secretKey` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-add-changed-files-pr-listener
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
            value: ["pull_request", "push"]
          - name: "addChangedFiles"
            value:
              enabled: true
              personalAccessToken:
                secretName: github-pat
                secretKey: token
        - ref:
            name: cel
          params:
          - name: filter
            value: extensions.changed_files.matches('controllers/')
...
----

. Save the configuration file.
