// Module included in the following assemblies:
//
// * nodes/nodes-pods-viewing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-viewing-usage_{context}"]
= Viewing pod usage statistics

You can display usage statistics about pods, which provide the runtime
environments for containers. These usage statistics include CPU, memory, and
storage consumption.

.Prerequisites

* You must have `cluster-reader` permission to view the usage statistics.

* Metrics must be installed to view the usage statistics.

.Procedure

To view the usage statistics:

. Run the following command:
+
[source,terminal]
----
$ oc adm top pods
----
+
For example:
+
[source,terminal]
----
$ oc adm top pods -n openshift-console
----
+
.Example output
[source,terminal]
----
NAME                         CPU(cores)   MEMORY(bytes)
console-7f58c69899-q8c8k     0m           22Mi
console-7f58c69899-xhbgg     0m           25Mi
downloads-594fcccf94-bcxk8   3m           18Mi
downloads-594fcccf94-kv4p6   2m           15Mi
----

. Run the following command to view the usage statistics for pods with labels:
+
[source,terminal]
----
$ oc adm top pod --selector=''
----
+
You must choose the selector (label query) to filter on. Supports `=`, `==`, and `!=`.
+
For example:
+
[source,terminal]
----
$ oc adm top pod --selector='name=my-pod'
----
