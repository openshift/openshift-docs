:_mod-docs-content-type: ASSEMBLY
[id="rosa-sts-config-identity-providers"]
= Configuring identity providers for STS
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-sts-config-identity-providers

toc::[]

After your {product-title} (ROSA) cluster is created, you must configure identity providers to determine how users log in to access the cluster.

The following topics describe how to configure an identity provider using {cluster-manager} console. Alternatively, you can use the ROSA CLI (`rosa`) to configure an identity provider and access the cluster.

include::modules/understanding-idp.adoc[leveloffset=+1]
include::modules/identity-provider-parameters.adoc[leveloffset=+2]
include::modules/config-github-idp.adoc[leveloffset=+1]
include::modules/config-gitlab-idp.adoc[leveloffset=+1]
include::modules/config-google-idp.adoc[leveloffset=+1]
include::modules/config-ldap-idp.adoc[leveloffset=+1]
include::modules/config-openid-idp.adoc[leveloffset=+1]
include::modules/config-htpasswd-idp.adoc[leveloffset=+1]

[id="additional-resources-cluster-access-sts"]
[role="_additional-resources"]
== Additional resources
* xref:../rosa_install_access_delete_clusters/rosa-sts-accessing-cluster.adoc#rosa-sts-accessing-cluster[Accessing a cluster]
* xref:../rosa_getting_started/rosa-sts-getting-started-workflow.adoc#rosa-sts-understanding-the-deployment-workflow[Understanding the ROSA with STS deployment workflow]
