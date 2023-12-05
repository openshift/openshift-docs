// Module included in the following assemblies:
//
// * nodes/nodes-nodes-viewing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-nodes-viewing-memory_{context}"]
= Viewing memory and CPU usage statistics on your nodes

You can display usage statistics about nodes, which provide the runtime
environments for containers. These usage statistics include CPU, memory, and
storage consumption.

.Prerequisites

* You must have `cluster-reader` permission to view the usage statistics.

* Metrics must be installed to view the usage statistics.

.Procedure

* To view the usage statistics:
+
[source,terminal]
----
$ oc adm top nodes
----
+
.Example output
[source,terminal]
----
NAME                                   CPU(cores)   CPU%      MEMORY(bytes)   MEMORY%
ip-10-0-12-143.ec2.compute.internal    1503m        100%      4533Mi          61%
ip-10-0-132-16.ec2.compute.internal    76m          5%        1391Mi          18%
ip-10-0-140-137.ec2.compute.internal   398m         26%       2473Mi          33%
ip-10-0-142-44.ec2.compute.internal    656m         43%       6119Mi          82%
ip-10-0-146-165.ec2.compute.internal   188m         12%       3367Mi          45%
ip-10-0-19-62.ec2.compute.internal     896m         59%       5754Mi          77%
ip-10-0-44-193.ec2.compute.internal    632m         42%       5349Mi          72%
----

* To view the usage statistics for nodes with labels:
+
[source,terminal]
----
$ oc adm top node --selector=''
----
+
You must choose the selector (label query) to filter on. Supports `=`, `==`, and `!=`.
