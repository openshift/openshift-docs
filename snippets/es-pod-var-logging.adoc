// Snippet included in the following assemblies:
//
//
// Snippet included in the following modules:
//
// * es-node-disk-low-watermark-reached.adoc
// * es-node-disk-high-watermark-reached.adoc
// * es-node-disk-flood-watermark-reached.adoc

:_mod-docs-content-type: SNIPPET

[TIP]
====
Some commands in this documentation reference an Elasticsearch pod by using a `$ES_POD_NAME` shell variable. If you want to copy and paste the commands directly from this documentation, you must set this variable to a value that is valid for your Elasticsearch cluster.

You can list the available Elasticsearch pods by running the following command:

[source,terminal]
----
$ oc -n openshift-logging get pods -l component=elasticsearch
----

Choose one of the pods listed and set the `$ES_POD_NAME` variable, by running the following command:

[source,terminal]
----
$ export ES_POD_NAME=<elasticsearch_pod_name>
----

You can now use the `$ES_POD_NAME` variable in commands.
====
