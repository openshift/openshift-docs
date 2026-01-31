// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-repository-crd-with-pipelines-as-code_{context}"]
= Using the Repository custom resource definition (CRD) with {pac}

[role="_abstract"]
The `Repository` custom resource (CR) has the following primary functions:

* Inform {pac} about processing an event from a URL.
* Inform {pac} about the namespace for the pipeline runs.
* Reference an API secret, username, or an API URL necessary for Git provider platforms when using webhook methods.
* Provide the last pipeline run status for a repository.

You can use the `tkn pac` CLI or other alternative methods to create a `Repository` CR inside the target namespace. For example:

[source,terminal]
----
cat <<EOF|kubectl create -n my-pipeline-ci -f- <1>

apiVersion: "pipelinesascode.tekton.dev/v1alpha1"
kind: Repository
metadata:
  name: project-repository
spec:
  url: "https://github.com/<repository>/<project>"
EOF
----
<1> `my-pipeline-ci` is the target namespace.

Whenever there is an event coming from the URL such as `https://github.com/<repository>/<project>`, {pac} matches it and starts checking out the content of the `<repository>/<project>` repository for pipeline run to match the content in the `.tekton/` directory.

[NOTE]
====
* You must create the `Repository` CRD in the same namespace where pipelines associated with the source code repository will be executed; it cannot target a different namespace.

* If multiple `Repository` CRDs match the same event, {pac} will process only the oldest one. If you need to match a specific namespace, add the `pipelinesascode.tekton.dev/target-namespace: "<mynamespace>"` annotation. Such explicit targeting prevents a malicious actor from executing a pipeline run in a namespace to which they do not have access.
====
