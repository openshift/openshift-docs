:_mod-docs-content-type: ASSEMBLY
[id="dedicated-administrator-role"]
= The dedicated-admin role
include::_attributes/common-attributes.adoc[]
:context: dedicated-administrator

toc::[]

As an administrator of an {product-title} cluster, your account has additional
permissions and access to all user-created projects in your organization's
cluster. While logged in to an account with this role, the basic developer CLI
(the `oc` command) allows you increased visibility and management capabilities
over objects across projects, while the administrator CLI (commands under the
`oc adm` command) allow you to complete additional operations.

[NOTE]
====
While your account does have these increased permissions, the actual cluster
maintenance and host configuration is still performed by the OpenShift
Operations Team. If you would like to request a change to your cluster that you
cannot perform using the administrator CLI, open a support case on the
link:https://access.redhat.com/support/[Red Hat Customer Portal].
====

include::modules/dedicated-logging-in-and-verifying-permissions.adoc[leveloffset=+1]

include::modules/dedicated-managing-dedicated-administrators.adoc[leveloffset=+1]

include::modules/dedicated-admin-granting-permissions.adoc[leveloffset=+1]

include::modules/dedicated-managing-service-accounts.adoc[leveloffset=+1]

include::modules/dedicated-managing-quotas-and-limit-ranges.adoc[leveloffset=+1]

[id="osd-installing-operators-from-operatorhub_{context}"]
== Installing Operators from the OperatorHub

{product-title} administrators can install Operators from a curated list
provided by the OperatorHub. This makes the Operator available to all developers
on your cluster to create Custom Resources and applications using that Operator.

[NOTE]
====
Privileged and custom Operators cannot be installed.
====

Administrators can only install Operators to the default `openshift-operators`
namespace, except for the Red Hat OpenShift Logging Operator, which requires the
`openshift-logging` namespace.

[role="_additional-resources"]
.Additional resources

* xref:../operators/admin/olm-adding-operators-to-cluster.adoc#olm-adding-operators-to-a-cluster[Adding Operators to a cluster]
