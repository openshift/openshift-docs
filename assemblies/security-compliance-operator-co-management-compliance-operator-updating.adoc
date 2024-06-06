:_mod-docs-content-type: ASSEMBLY
[id="compliance-operator-updating"]
= Updating the Compliance Operator
include::_attributes/common-attributes.adoc[]
:context: compliance-operator-updating

toc::[]

As a cluster administrator, you can update the Compliance Operator on your {product-title} cluster.
//
// This will be un-commented for OCP 4.11-4.14 releases. Commented out in the main branch.
//
// [IMPORTANT]
// ====
// It is recommended to update the Compliance Operator to version 1.3.1 or later before updating your {product-title} cluster to version 4.14 or later.
// ====

include::modules/olm-preparing-upgrade.adoc[leveloffset=+1]
include::modules/olm-changing-update-channel.adoc[leveloffset=+1]
include::modules/olm-approving-pending-upgrade.adoc[leveloffset=+1]

// [id="additional-resources-updating-the-compliance-operator"]
// [role="_additional-resources"]
// == Additional resources
//
// * For more information, see xref:../../../operators/admin/