// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-instances-of-services-managed-by-the-operators.adoc

[id="listing-available-services-from-the-operators-installed-on-the-cluster_{context}"]

= Listing available services from the Operators installed on the cluster

With `{odo-title}`, you can display the list of the Operators installed on your cluster, and the services they provide.

* To list the Operators installed in current project, run:
+
[source,terminal]
----
$ odo catalog list services
----
+
The command lists Operators and the CRDs.
The output of the command shows the Operators installed on your cluster. For example:
+
[source,terminal]
----
Operators available in the cluster
NAME                          CRDs
etcdoperator.v0.9.4           EtcdCluster, EtcdBackup, EtcdRestore
mongodb-enterprise.v1.4.5     MongoDB, MongoDBUser, MongoDBOpsManager
----
+
`etcdoperator.v0.9.4` is the Operator, `EtcdCluster`, `EtcdBackup` and `EtcdRestore` are the CRDs provided by the Operator.
