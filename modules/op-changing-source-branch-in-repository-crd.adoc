// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="changing-source-branch-in-repository-crd_{context}"]
= Changing the source branch for the pipeline definition

[role="_abstract"]
By default, when processing a push event or a pull request event, {pac} fetches the pipeline definition from the branch that triggered the event. You can use the `pipelinerun_provenance` setting in the `Repository` custom resource definition (CRD) to fetch the definition from the default branch configured on the Git repository provider, such as `main`, `master`, or `trunk`.

[source,yaml]
----
apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: my-repo
  namespace: target-namespace
spec:
# ...
  settings:
    pipelinerun_provenance: "default_branch"
# ...
----

[NOTE]
====
You can use this setting as a security precaution. With the default behaviour, {pac} uses the pipeline definition in the submitted pull request. With the `default-branch` setting, the pipeline definition must be merged into the default branch before it is run. This requirement ensures maximum possible verification of any changes during merge review.
====
