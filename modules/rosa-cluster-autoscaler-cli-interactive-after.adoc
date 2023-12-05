// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-enable-cluster-autoscale-cli-interactive_after_{context}"]
= Enable autoscaling after cluster creation by using the interactive mode with the ROSA CLI

You can use the interactive mode of your terminal, if available, to set cluster-wide autoscaling behavior after cluster creation.

.Procedure

- After you have created a cluster, type the following command:
+
.Example:
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster> --interactive
----
+
You can then set all available autoscaling parameters.
