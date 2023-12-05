// Module included in the following assemblies:
//
// * virt/install/uninstalling-virt.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-deleting-virt-crds-web_{context}"]
= Deleting {VirtProductName} custom resource definitions

You can delete the {VirtProductName} custom resource definitions (CRDs) by using the web console.

.Prerequisites

* You have access to an {product-title} cluster using an account with `cluster-admin` permissions.

.Procedure

. Navigate to *Administration* -> *CustomResourceDefinitions*.

. Select the *Label* filter and enter `operators.coreos.com/kubevirt-hyperconverged.openshift-cnv` in the *Search* field to display the {VirtProductName} CRDs.

. Click the Options menu {kebab} beside each CRD and select *Delete CustomResourceDefinition*.