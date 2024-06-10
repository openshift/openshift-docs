// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-delete-cluster-autoscale-cli_{context}"]
= Delete autoscaling using the ROSA CLI

You can delete the cluster autoscaler if you no longer want to use it.

- To delete the cluster autoscaler, run the following command:
+
.Example:
[source,terminal]
----
$ rosa delete autoscaler --cluster=<mycluster>
----
