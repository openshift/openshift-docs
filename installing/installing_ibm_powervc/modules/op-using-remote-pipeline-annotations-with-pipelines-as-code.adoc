// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="using-remote-pipeline-annotations-with-pipelines-as-code_{context}"]
= Using remote pipeline annotations with {pac}

[role="_abstract"]
You can share a pipeline definition across multiple repositories by using the remote pipeline annotation.

[source,yaml]
----
...
    pipelinesascode.tekton.dev/pipeline: "<https://git.provider/raw/pipeline.yaml>" <1>
...
----
<1> URL to the remote pipeline definition. You can also provide locations for files inside the same repository.

[NOTE]
====
You can reference only one pipeline definition using the annotation.
====

