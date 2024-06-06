:_mod-docs-content-type: ASSEMBLY
[id="metallb-upgrading-operator"]
= Upgrading the MetalLB
include::_attributes/common-attributes.adoc[]
:context: metallb-upgrading-operator

toc::[]

If you are currently running version 4.10 or an earlier version of the MetalLB Operator, please note that automatic updates to any version later than 4.10 do not work. Upgrading to a newer version from any version of the MetalLB Operator that is 4.11 or later is successful. For example, upgrading from version 4.12 to version 4.13 will occur smoothly.

A summary of the upgrade procedure for the MetalLB Operator from 4.10 and earlier is as follows:

. Delete the installed MetalLB Operator version for example 4.10. Ensure that the namespace and the `metallb` custom resource are not removed.

. Using the CLI, install the MetalLB Operator {product-version} in the same namespace where the previous version of the MetalLB Operator was installed.

[NOTE]
====
This procedure does not apply to automatic z-stream updates of the MetalLB Operator, which follow the standard straightforward method.
====

For detailed steps to upgrade the MetalLB Operator from 4.10 and earlier, see the guidance that follows. As a cluster administrator, start the upgrade process by deleting the MetalLB Operator by using the OpenShift CLI (`oc`) or the web console.

//Delete metallb using web console
include::modules/olm-deleting-metallb-operators-from-a-cluster-using-web-console.adoc[leveloffset=+1]

//Delete metallb using cli
include::modules/olm-deleting-metallb-operators-from-a-cluster-using-cli.adoc[leveloffset=+1]

//Delete targetNamespace
include::modules/olm-updating-metallb-operatorgroup.adoc[leveloffset=+1]

//Upgrade the MetalLB
include::modules/nw-metalLB-basic-upgrade-operator.adoc[leveloffset=+1]

[id="additional-resources"]
== Additional resources

* xref:../../operators/admin/olm-deleting-operators-from-cluster.adoc#olm-deleting-operators-from-a-cluster[Deleting Operators from a cluster]

* xref:../../networking/metallb/metallb-operator-install.adoc#metallb-operator-install[Installing the MetalLB Operator]

