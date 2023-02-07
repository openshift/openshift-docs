// Module included in the following assemblies:
//
// * operators/understanding/olm/olm-understanding-olm.adoc

[id="olm-resources_{context}"]
= OLM resources

The following custom resource definitions (CRDs) are defined and managed by Operator Lifecycle Manager (OLM):

.CRDs managed by OLM and Catalog Operators
[cols="2a,2a,8a",options="header"]
|===
|Resource |Short name |Description

|`ClusterServiceVersion` (CSV)
|`csv`
|Application metadata. For example: name, version, icon, required resources.

|`CatalogSource`
|`catsrc`
|A repository of CSVs, CRDs, and packages that define an application.

|`Subscription`
|`sub`
|Keeps CSVs up to date by tracking a channel in a package.

|`InstallPlan`
|`ip`
|Calculated list of resources to be created to automatically install or upgrade a CSV.

|`OperatorGroup`
|`og`
|Configures all Operators deployed in the same namespace as the `OperatorGroup` object to watch for their custom resource (CR) in a list of namespaces or cluster-wide.

|`OperatorConditions`
|-
|Creates a communication channel between OLM and an Operator it manages. Operators can write to the `Status.Conditions` array to communicate complex states to OLM.
|===
