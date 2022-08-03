// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc
// * operators/operator-reference.adoc

[id="olm-architecture_{context}"]
ifeval::["{context}" != "cluster-operators-ref"]
= Component responsibilities
endif::[]
ifeval::["{context}" == "cluster-operators-ref"]
= CRDs
endif::[]

Operator Lifecycle Manager (OLM) is composed of two Operators: the OLM Operator and the Catalog Operator.

Each of these Operators is responsible for managing the custom resource definitions (CRDs) that are the basis for the OLM framework:

.CRDs managed by OLM and Catalog Operators
[cols="2a,1a,1a,8a",options="header"]
|===
|Resource |Short name |Owner |Description

|`ClusterServiceVersion` (CSV)
|`csv`
|OLM
|Application metadata: name, version, icon, required resources, installation, and so on.

|`InstallPlan`
|`ip`
|Catalog
|Calculated list of resources to be created to automatically install or upgrade a CSV.

|`CatalogSource`
|`catsrc`
|Catalog
|A repository of CSVs, CRDs, and packages that define an application.

|`Subscription`
|`sub`
|Catalog
|Keeps CSVs up to date by tracking a channel in a package.

|`OperatorGroup`
|`og`
|OLM
|Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.
|===

Each of these Operators is also responsible for creating the following resources:

.Resources created by OLM and Catalog Operators
[options="header"]
|===
|Resource |Owner

|`Deployments`
.4+.^|OLM

|`ServiceAccounts`
|`(Cluster)Roles`
|`(Cluster)RoleBindings`

|`CustomResourceDefinitions` (CRDs)
.2+.^|Catalog
|`ClusterServiceVersions`
|===
