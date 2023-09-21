:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="rosa-config-identity-providers"]
= Configuring identity providers
:context: rosa-config-identity-providers

toc::[]

After your {product-title} (ROSA) cluster is created, you must configure identity providers to determine how users log in to access the cluster.

The following topics describe how to configure an identity provider using {cluster-manager} console. Alternatively, you can use the `rosa` CLI to create an identity provider and access the cluster.

include::snippets/rosa-sts.adoc[]

include::modules/understanding-idp.adoc[leveloffset=+1]
include::modules/identity-provider-parameters.adoc[leveloffset=+2]
include::modules/config-github-idp.adoc[leveloffset=+1]
include::modules/config-gitlab-idp.adoc[leveloffset=+1]
include::modules/config-google-idp.adoc[leveloffset=+1]
include::modules/config-ldap-idp.adoc[leveloffset=+1]
include::modules/config-openid-idp.adoc[leveloffset=+1]
include::modules/config-htpasswd-idp.adoc[leveloffset=+1]

[id="additional-resources-idps"]
[role="_additional-resources"]
== Additional resources
* xref:../../rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc#rosa-sts-accessing-cluster[Accessing a cluster]
* xref:../../rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-getting-started-workflow.adoc#rosa-understanding-the-deployment-workflow[Understanding the ROSA deployment workflow]
