:_mod-docs-content-type: ASSEMBLY
[id="rosa-oidc-overview"]
= OpenID Connect Overview
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-oidc-overview

toc::[]

OpenID Connect (OIDC) uses Security Token Service (STS) to allow clients to provide a web identity token to gain access to multiple services. When a client signs into a service using STS, the token is validated against the OIDC identity provider.

The OIDC protocol uses a configuration URL that contains the necessary information to authenticate a client's identity. The protocol responds to the provider with the credentials needed for the provider to validate the client and sign them in.

{product-title} clusters use STS and OIDC to grant the in-cluster operators access to necessary AWS resources.

include::modules/rosa-oidc-understanding.adoc[leveloffset=+1]

include::modules/rosa-oidc-config-overview.adoc[leveloffset=+1]
[discrete]
include::modules/rosa-sts-byo-oidc.adoc[leveloffset=+3]
[discrete]
include::modules/rosa-sts-byo-oidc-options.adoc[leveloffset=+3]

include::modules/rosa-sts-oidc-provider-command.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_rosa-oidc-config"]
== Additional resources

* See xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-byo-odic-overview_rosa-sts-about-iam-resources[Creating an OpenID Connect Configuration] for the ROSA Classic instructions.
* See xref:../rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc#rosa-sts-byo-oidc_rosa-hcp-sts-creating-a-cluster-quickly[Creating an OpenID Connect Configuration] for the {hcp-title} instructions.