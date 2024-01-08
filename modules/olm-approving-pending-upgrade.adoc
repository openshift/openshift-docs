// Module included in the following assemblies:
//
// * operators/admin/olm-upgrading-operators.adoc
// * virt/updating/upgrading-virt.adoc

:_mod-docs-content-type: PROCEDURE
[id="olm-approving-pending-upgrade_{context}"]
= Manually approving a pending Operator update

If an installed Operator has the approval strategy in its subscription set to *Manual*, when new updates are released in its current update channel, the update must be manually approved before installation can begin.

.Prerequisites

* An Operator previously installed using Operator Lifecycle Manager (OLM).

.Procedure

. In the *Administrator* perspective of the {product-title} web console, navigate to *Operators -> Installed Operators*.

. Operators that have a pending update display a status with *Upgrade available*. Click the name of the Operator you want to update.

. Click the *Subscription* tab. Any updates requiring approval are displayed next to *Upgrade status*. For example, it might display *1 requires approval*.

. Click *1 requires approval*, then click *Preview Install Plan*.

. Review the resources that are listed as available for update. When satisfied, click *Approve*.

. Navigate back to the *Operators -> Installed Operators* page to monitor the progress of the update. When complete, the status changes to *Succeeded* and *Up to date*.
