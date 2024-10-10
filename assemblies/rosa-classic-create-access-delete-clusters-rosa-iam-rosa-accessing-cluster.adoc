:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="rosa-accessing-cluster"]
= Accessing a ROSA cluster
:context: rosa-accessing-cluster

toc::[]

As a best practice, access your {product-title} (ROSA) cluster using an identity provider (IDP) account. However, the cluster administrator who created the cluster can access it using the quick access procedure.

This document describes how to access a cluster and set up an IDP using the `rosa` CLI. Alternatively, you can set up an IDP account using {cluster-manager} console.

include::snippets/rosa-sts.adoc[]

include::modules/rosa-accessing-your-cluster-quick.adoc[leveloffset=+1]

include::modules/rosa-accessing-your-cluster.adoc[leveloffset=+1]

include::modules/rosa-create-cluster-admins.adoc[leveloffset=+1]

include::modules/rosa-create-dedicated-cluster-admins.adoc[leveloffset=+1]

[id="additional-resources-cluster-access"]
[role="_additional-resources"]
== Additional resources

* xref:../../rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc#rosa-sts-config-identity-providers[Configuring identity providers]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-getting-started-workflow.adoc#rosa-understanding-the-deployment-workflow[Understanding the ROSA deployment workflow]
