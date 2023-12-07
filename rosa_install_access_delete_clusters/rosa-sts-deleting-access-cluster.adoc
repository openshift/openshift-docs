:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="rosa-sts-deleting-access-cluster"]
= Revoking access to a ROSA cluster
:context: rosa-sts-deleting-access-cluster

toc::[]

An identity provider (IDP) controls access to a {product-title} (ROSA) cluster. To revoke access of a user to a cluster, you must configure that within the IDP that was set up for authentication.

[id="rosa-revoke-admin-access"]
== Revoking administrator access using the ROSA CLI
You can revoke the administrator access of users so that they can access the cluster without administrator privileges. To remove the administrator access for a user, you must revoke the `dedicated-admin` or `cluster-admin` privileges. You can revoke the administrator privileges using the {product-title} (ROSA) CLI, `rosa`, or using {cluster-manager} console.

include::modules/rosa-delete-dedicated-admins.adoc[leveloffset=+2]

include::modules/rosa-delete-cluster-admins.adoc[leveloffset=+2]

include::modules/rosa-delete-users.adoc[leveloffset=+1]
