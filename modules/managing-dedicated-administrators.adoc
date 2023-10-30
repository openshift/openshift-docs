// Module included in the following assemblies:
//
// * osd_cluster_admin/osd-admin-roles.adoc

:_mod-docs-content-type: PROCEDURE
[id="managing-dedicated-administrators_{context}"]
=  Managing {product-title} administrators

Administrator roles are managed using a `cluster-admin` or `dedicated-admin` group on the cluster. Existing members of this group can edit membership through {cluster-manager-url}.

// TODO: These two procedures should be separated and created as proper procedure modules.

[id="dedicated-administrators-adding-user_{context}"]
== Adding a user

.Procedure

. Navigate to the *Cluster Details* page and *Access Control* tab.
. Select the *Cluster Roles and Access* tab and click *Add user*.
. Enter the user name and select the group.
. Click *Add user*.


[NOTE]
====
Adding a user to the `cluster-admin` group can take several minutes to complete.
====

[id="dedicated-administrators-removing-user_{context}"]
== Removing a user

.Procedure

. Navigate to the *Cluster Details* page and *Access Control* tab.
. Click the Options menu {kebab} to the right of the user and group combination and click *Delete*.
