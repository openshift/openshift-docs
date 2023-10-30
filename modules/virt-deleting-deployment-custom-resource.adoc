// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt-web.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-deployment-custom-resource_{context}"]
= Deleting the HyperConverged custom resource

To uninstall {VirtProductName}, you first delete the `HyperConverged` custom resource (CR).

.Prerequisites

* You have access to an {product-title} cluster using an account with `cluster-admin` permissions.

.Procedure

. Navigate to the *Operators* -> *Installed Operators* page.

. Select the {VirtProductName} Operator.

. Click the *{VirtProductName} Deployment* tab.

. Click the Options menu {kebab} beside `kubevirt-hyperconverged` and select *Delete HyperConverged*.

. Click *Delete* in the confirmation window.