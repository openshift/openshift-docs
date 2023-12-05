// Module included in the following assemblies:
//
// * authentication/using-rbac.adoc
// * post_installation_configuration/preparing-for-users.adoc

ifdef::openshift-enterprise,openshift-webscale,openshift-origin,openshift-dedicated,openshift-rosa[]

[id="cluster-role-binding-commands_{context}"]
= Cluster role binding commands

You can also manage cluster role bindings using the following
operations. The `-n` flag is not used for these operations because
cluster role bindings use non-namespaced resources.

.Cluster role binding operations
[options="header"]
|===

|Command |Description

|`$ oc adm policy add-cluster-role-to-user _<role>_ _<username>_`
|Binds a given role to specified users for all projects in the cluster.

|`$ oc adm policy remove-cluster-role-from-user _<role>_ _<username>_`
|Removes a given role from specified users for all projects in the cluster.

|`$ oc adm policy add-cluster-role-to-group _<role>_ _<groupname>_`
|Binds a given role to specified groups for all projects in the cluster.

|`$ oc adm policy remove-cluster-role-from-group _<role>_ _<groupname>_`
|Removes a given role from specified groups for all projects in the cluster.

|===
endif::[]
