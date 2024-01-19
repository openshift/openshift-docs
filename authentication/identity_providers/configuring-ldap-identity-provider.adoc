:_mod-docs-content-type: ASSEMBLY
[id="configuring-ldap-identity-provider"]
= Configuring an LDAP identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-ldap-identity-provider

toc::[]

Configure the `ldap` identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication.

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-about-ldap.adoc[leveloffset=+1]

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
include::modules/identity-provider-ldap-secret.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-ldap-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]
endif::[]
