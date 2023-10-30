// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-cluster-autoscaling.adoc

:_mod-docs-content-type: PROCEDURE
[id="rosa-enable-cluster-autoscale-cli-after_{context}"]
= Enable autoscaling after cluster creation with the ROSA CLI

You can use the ROSA CLI (`rosa`) to set cluster-wide autoscaling after cluster creation.

.Procedure

- After you have created a cluster, create the autoscaler:
+
.Example:
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster>
----
+
.. You can also create the autoscaler with specific parameters using the following command:
+
.Example:
[source,terminal]
----
$ rosa create autoscaler --cluster=<mycluster> <parameter>
----
