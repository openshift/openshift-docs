// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/exposing-binding-data-from-a-service.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-rbac-requirements_{context}"]
= RBAC requirements

[role="_abstract"]
To expose the backing service binding data using the {servicebinding-title}, you require certain Role-based access control (RBAC) permissions. Specify certain verbs under the `rules` field of the `ClusterRole` resource to grant the RBAC permissions for the backing service resources. When you define these `rules`, you allow the {servicebinding-title} to read the binding data of the backing service resources throughout the cluster. If the users do not have permissions to read binding data or modify application resource, the {servicebinding-title} prevents such users to bind services to application. Adhering to the RBAC requirements avoids unnecessary permission elevation for the user and prevents access to unauthorized services or applications.

The {servicebinding-title} performs requests against the Kubernetes API using a dedicated service account. By default, this account has permissions to bind services to workloads, both represented by the following standard Kubernetes or OpenShift objects:

* `Deployments`
* `DaemonSets`
* `ReplicaSets`
* `StatefulSets`
* `DeploymentConfigs`

The Operator service account is bound to an aggregated cluster role, allowing Operator providers or cluster administrators to enable binding custom service resources to workloads. To grant the required permissions within a `ClusterRole`, label it with the `servicebinding.io/controller` flag and set the flag value to `true`. The following example shows how to allow the {servicebinding-title} to `get`, `watch`, and `list` the custom resources (CRs) of Crunchy PostgreSQL Operator:

.Example: Enable binding to PostgreSQL database instances provisioned by Crunchy PostgreSQL Operator
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: postgrescluster-reader
  labels:
     servicebinding.io/controller: "true"
rules:
- apiGroups:
    - postgres-operator.crunchydata.com
  resources:
    - postgresclusters
  verbs:
    - get
    - watch
    - list
  ...
----

This cluster role can be deployed during the installation of the backing service Operator.