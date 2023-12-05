:_mod-docs-content-type: ASSEMBLY
[id="premigration-checklists-mtc"]
= Premigration checklists
include::_attributes/common-attributes.adoc[]
:context: premigration-checklists-mtc

toc::[]

Before you migrate your application workloads with the {mtc-full} ({mtc-short}), review the following checklists.

[id="cluster-health-checklist_{context}"]
== Cluster health checklist

* [ ] The clusters meet the minimum hardware requirements for the specific platform and installation method, for example, on xref:../installing/installing_bare_metal/installing-bare-metal.adoc#minimum-resource-requirements_installing-bare-metal[bare metal].
* [ ] All xref:../migration_toolkit_for_containers/migrating-applications-with-mtc.adoc#migration-prerequisites_migrating-applications-with-mtc[{mtc-short} prerequisites] are met.
* [ ] All nodes have an active {product-title} subscription.
* [ ] You have xref:../support/troubleshooting/verifying-node-health.adoc#verifying-node-health[verified node health].
* [ ] The xref:../authentication/understanding-identity-provider.adoc#supported-identity-providers[identity provider] is working.
* [ ] The migration network has a minimum throughput of 10 Gbps.
* [ ] The clusters have sufficient resources for migration.
+
[NOTE]
====
Clusters require additional memory, CPUs, and storage in order to run a migration on top of normal workloads. Actual resource requirements depend on the number of Kubernetes resources being migrated in a single migration plan. You must test migrations in a non-production environment in order to estimate the resource requirements.
====

* [ ] The link:https://access.redhat.com/solutions/4885641[etcd disk performance] of the clusters has been checked with `fio`.

[id="source-cluster-checklist_{context}"]
== Source cluster checklist

* [ ] You have checked for persistent volumes (PVs) with abnormal configurations  stuck in a *Terminating* state by running the following command:
+
[source,terminal]
----
$ oc get pv
----

* [ ] You have checked for pods whose status is other than *Running* or *Completed* by running the following command:
+
[source,terminal]
----
$ oc get pods --all-namespaces | egrep -v 'Running | Completed'
----

* [ ] You have checked for pods with a high restart count by running the following command:
+
[source,terminal]
----
$ oc get pods --all-namespaces --field-selector=status.phase=Running \
  -o json | jq '.items[]|select(any( .status.containerStatuses[]; \
  .restartCount > 3))|.metadata.name'
----
+
Even if the pods are in a *Running* state, a high restart count might indicate underlying problems.

* [ ] The cluster certificates are valid for the duration of the migration process.
* [ ] You have checked for pending certificate-signing requests by running the following command:
+
[source,terminal]
----
$ oc get csr -A | grep pending -i
----

* [ ] The registry uses a xref:../scalability_and_performance/optimization/optimizing-storage.adoc#optimizing-storage[recommended storage type].
* [ ] You can read and write images to the registry.
* [ ] The link:https://access.redhat.com/articles/3093761[etcd cluster] is healthy.
* [ ] The xref:../post_installation_configuration/node-tasks.adoc#create-a-kubeletconfig-crd-to-edit-kubelet-parameters_post-install-node-tasks[average API server response time] on the source cluster is less than 50 ms.

[id="target-cluster-checklist_{context}"]
== Target cluster checklist

* [ ] The cluster has the correct network configuration and permissions to access external services, for example, databases, source code repositories, container image registries, and CI/CD tools.
* [ ] External applications and services that use services provided by the cluster have the correct network configuration and permissions to access the cluster.
* [ ] Internal container image dependencies are met.
* [ ] The target cluster and the replication repository have sufficient storage space.
