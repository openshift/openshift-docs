// Module included in the following assemblies:
//
// * assemblies/adding-service.adoc

:_mod-docs-content-type: PROCEDURE
[id="deleting-service_{context}"]
= Deleting an add-on service using {cluster-manager-first}

You can delete an add-on service from your {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
cluster by using {cluster-manager-first}.

.Procedure

. Navigate to the *Clusters* page in {cluster-manager-url}.

. Click the cluster with the installed service that you want to delete.

. Navigate to the *Add-ons* tab, and locate the installed service that you want to delete.

. From the installed service option, click the menu and select *Uninstall add-on* from the drop-down menu.

. You must type the name of the service that you want to delete in the confirmation message that appears.

. Click *Uninstall*. You are returned to the *Add-ons* tab and an uninstalling state icon is present on the service option you deleted.
