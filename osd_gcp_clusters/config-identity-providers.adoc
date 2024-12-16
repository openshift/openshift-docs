:_mod-docs-content-type: ASSEMBLY
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="config-identity-providers"]
= Configuring identity providers
:context: config-identity-providers

toc::[]

After your {product-title} cluster is created, you must configure identity providers to determine how users log in to access the cluster.

include::modules/understanding-idp.adoc[leveloffset=+1]
include::modules/identity-provider-parameters.adoc[leveloffset=+2]
include::modules/config-github-idp.adoc[leveloffset=+1]
include::modules/config-gitlab-idp.adoc[leveloffset=+1]
include::modules/config-google-idp.adoc[leveloffset=+1]
include::modules/config-ldap-idp.adoc[leveloffset=+1]
include::modules/config-openid-idp.adoc[leveloffset=+1]
include::modules/config-htpasswd-idp.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources

* xref:../osd_architecture/osd_policy/osd-service-definition.adoc#cluster-admin-user_osd-service-definition[Customer administrator user]

include::modules/access-cluster.adoc[leveloffset=+1]
