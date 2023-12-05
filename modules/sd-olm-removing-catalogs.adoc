// Module included in the following assemblies:
//
// * operators/admin/olm-managing-custom-catalogs.adoc

// The OCP version of this procedure is olm-removing-catalogs.adoc.

:_mod-docs-content-type: PROCEDURE
[id="sd-olm-removing-catalogs_{context}"]
= Removing custom catalogs

As an administrator with the `dedicated-admin` role, you can remove custom Operator catalogs that have been previously added to your cluster by deleting the related catalog source.

.Prerequisites
* You have access to the cluster as a user with the `dedicated-admin` role.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Home* -> *Search*.

. Select a project from the *Project:* list.

. Select *CatalogSource* from the *Resources* list.

. Select the *Options* menu {kebab} for the catalog that you want to remove, and then click *Delete CatalogSource*.
