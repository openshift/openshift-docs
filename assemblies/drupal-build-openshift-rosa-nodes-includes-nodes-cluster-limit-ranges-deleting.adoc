// Module included in the following assemblies:
//
// * nodes/cluster/limit-ranges.adoc

[id="nodes-cluster-limit-ranges-deleting_{context}"]
= Deleting a Limit Range


To remove any active `LimitRange` object to no longer enforce the limits in a project:

* Run the following command:
+
[source,terminal]
----
$ oc delete limits <limit_name>
----
