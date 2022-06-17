// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/op-tkn-references.adoc

[id="op-tkn-pipeline-management_{context}"]
= Pipelines management commands

== pipeline
Manage pipelines.

.Example: Display help
[source,terminal]
----
$ tkn pipeline --help
----

== pipeline delete

Delete a pipeline.

.Example: Delete the `mypipeline` pipeline from a namespace
[source,terminal]
----
$ tkn pipeline delete mypipeline -n myspace
----

== pipeline describe
Describe a pipeline.

.Example: Describe the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline describe mypipeline
----

== pipeline list
Display a list of pipelines.

.Example: Display a list of pipelines
[source,terminal]
-----
$ tkn pipeline list
-----

== pipeline logs
Display the logs for a specific pipeline.

.Example: Stream the live logs for the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline logs -f mypipeline
----

== pipeline start
Start a pipeline.

.Example: Start the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline start mypipeline
----
