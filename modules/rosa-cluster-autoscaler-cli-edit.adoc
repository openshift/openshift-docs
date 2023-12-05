// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-edit-cluster-autoscale-cli_{context}"]
= Edit autoscaling after cluster creation with the ROSA CLI

You can edit any specific parameters of the cluster autoscaler after creating the autoscaler.

- To edit the cluster autoscaler, run the following command:
+
.Example:
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster>
----
+
.. To edit a specific parameter, run the following command:
+
.Example:
[source,terminal]
----
$ rosa edit autoscaler --cluster=<mycluster> <parameter>
----
