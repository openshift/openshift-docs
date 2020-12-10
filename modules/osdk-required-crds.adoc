// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-crds-required_{context}"]
= Required CRDs

Relying on other required CRDs is completely optional and only exists to reduce the scope of individual Operators and provide a way to compose multiple Operators together to solve an end-to-end use case.

An example of this is an Operator that might set up an application and install an etcd cluster (from an etcd Operator) to use for distributed locking and a Postgres database (from a Postgres Operator) for data storage.

Operator Lifecycle Manager (OLM) checks against the available CRDs and Operators in the cluster to fulfill these requirements. If suitable versions are found, the Operators are started within the desired namespace and a service account created for each Operator to create, watch, and modify the Kubernetes resources required.

.Required CRD fields
[cols="2a,5a,2",options="header"]
|===
|Field |Description |Required/optional

|`Name`
|The full name of the CRD you require.
|Required

|`Version`
|The version of that object API.
|Required

|`Kind`
|The Kubernetes object kind.
|Required

|`DisplayName`
|A human readable version of the CRD.
|Required

|`Description`
|A summary of how the component fits in your larger architecture.
|Required
|===

.Example required CRD
[source,yaml]
----
    required:
    - name: etcdclusters.etcd.database.coreos.com
      version: v1beta2
      kind: EtcdCluster
      displayName: etcd Cluster
      description: Represents a cluster of etcd nodes.
----
