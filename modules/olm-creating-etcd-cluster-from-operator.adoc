:_mod-docs-content-type: PROCEDURE
[id="olm-creating-etcd-cluster-from-operator_{context}"]
= Creating an etcd cluster using an Operator

This procedure walks through creating a new etcd cluster using the etcd Operator, managed by Operator Lifecycle Manager (OLM).

.Prerequisites

ifndef::openshift-dedicated,openshift-rosa[]
* Access to an {product-title} {product-version} cluster.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* Access to an {product-title} cluster.
endif::openshift-dedicated,openshift-rosa[]
* The etcd Operator already installed cluster-wide by an administrator.

.Procedure

. Create a new project in the {product-title} web console for this procedure. This example uses a project called `my-etcd`.

. Navigate to the *Operators -> Installed Operators* page. The Operators that have been installed to the cluster by the
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrator
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
dedicated-admin
endif::openshift-dedicated,openshift-rosa[]
and are available for use are shown here as a list of cluster service versions (CSVs). CSVs are used to launch and manage the software provided by the Operator.
+
[TIP]
====
You can get this list from the CLI using:

[source,terminal]
----
$ oc get csv
----
====

. On the *Installed Operators* page, click the etcd Operator to view more details and available actions.
+
As shown under *Provided APIs*, this Operator makes available three new resource types, including one for an *etcd Cluster* (the `EtcdCluster` resource). These objects work similar to the built-in native Kubernetes ones, such as `Deployment` or `ReplicaSet`, but contain logic specific to managing etcd.

. Create a new etcd cluster:

.. In the *etcd Cluster* API box, click *Create instance*.

.. The next page allows you to make any modifications to the minimal starting template of an `EtcdCluster` object, such as the size of the cluster. For now, click *Create* to finalize. This triggers the Operator to start up the pods, services, and other components of the new etcd cluster.

. Click the *example* etcd cluster, then click the *Resources* tab to see that your project now contains a number of resources created and configured automatically by the Operator.
+
Verify that a Kubernetes service has been created that allows you to access the database from other pods in your project.

. All users with the `edit` role in a given project can create, manage, and delete application instances (an etcd cluster, in this example) managed by Operators that have already been created in the project, in a self-service manner, just like a cloud service. If you want to enable additional users with this ability, project administrators can add the role using the following command:
+
[source,terminal]
----
$ oc policy add-role-to-user edit <user> -n <target_project>
----

You now have an etcd cluster that will react to failures and rebalance data as pods become unhealthy or are migrated between nodes in the cluster. Most importantly,
ifndef::openshift-dedicated,openshift-rosa[]
cluster administrators
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
dedicated-admins
endif::openshift-dedicated,openshift-rosa[]
or developers with proper access can now easily use the database with their applications.
