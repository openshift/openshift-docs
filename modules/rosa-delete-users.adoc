// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa-sts-deleting-access-cluster.adoc


:_mod-docs-content-type: PROCEDURE
[id="rosa-delete-users"]
= Revoking administrator access using {cluster-manager} console
You can revoke the `dedicated-admin` or `cluster-admin` access of users through {cluster-manager} console. Users will be able to access the cluster without administrator privileges.

.Prerequisites

* You have added an Identity Provider (IDP) to your cluster.
* You have the IDP user name for the user whose privileges you are revoking.
* You are logged in to {cluster-manager} console using an {cluster-manager} account that you used to create the cluster, the organization administrator user, or the super administrator user.

.Procedure

. On the *Clusters* tab of {cluster-manager}, select the name of your cluster to view the cluster details.
. Select *Access control* > *Cluster Roles and Access*.
. For the user that you want to remove, click the *Options* menu {kebab} to the right of the user and group combination and click *Delete*.
