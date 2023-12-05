:_mod-docs-content-type: ASSEMBLY
[id="configuring-gitlab-identity-provider"]
= Configuring a GitLab identity provider
include::_attributes/common-attributes.adoc[]
:context: configuring-gitlab-identity-provider

toc::[]

Configure the `gitlab` identity provider using link:https://gitlab.com/[GitLab.com] or any other GitLab instance as an identity provider.

ifdef::openshift-origin,openshift-enterprise,openshift-webscale[]
include::modules/identity-provider-overview.adoc[leveloffset=+1]
endif::openshift-origin,openshift-enterprise,openshift-webscale[]

include::modules/identity-provider-gitlab-about.adoc[leveloffset=+1]

include::modules/identity-provider-secret.adoc[leveloffset=+1]

include::modules/identity-provider-config-map.adoc[leveloffset=+1]

include::modules/identity-provider-gitlab-CR.adoc[leveloffset=+1]

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See xref:../../authentication/understanding-identity-provider.adoc#identity-provider-parameters_understanding-identity-provider[Identity provider parameters] for information on parameters, such as `mappingMethod`, that are common to all identity providers.

include::modules/identity-provider-add.adoc[leveloffset=+1]
