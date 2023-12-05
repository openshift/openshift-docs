// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="cleaning-up-pipeline-run-using-pipelines-as-code_{context}"]
= Cleaning up pipeline run using {pac}

[role="_abstract"]

There can be many pipeline runs in a user namespace. By setting the `max-keep-runs` annotation, you can configure {pac} to retain a limited number of pipeline runs that matches an event. For example:

[source,yaml]
----
...
  pipelinesascode.tekton.dev/max-keep-runs: "<max_number>" <1>
...
----
<1> {pac} starts cleaning up right after it finishes a successful execution, retaining only the maximum number of pipeline runs configured using the annotation.
+
[NOTE]
====
* {pac} skips cleaning the running pipelines but cleans up the pipeline runs with an unknown status.
* {pac} skips cleaning a failed pull request.
====

