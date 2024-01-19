:_mod-docs-content-type: ASSEMBLY
[id="security-platform"]
= Securing the container platform
include::_attributes/common-attributes.adoc[]
:context: security-platform

toc::[]

{product-title} and Kubernetes APIs are key to automating container management at scale. APIs are used to:

* Validate and configure the data for pods, services, and replication controllers.
* Perform project validation on incoming requests and invoke triggers on other
major system components.

Security-related features in {product-title} that are based on Kubernetes include:

* Multitenancy, which combines Role-Based Access Controls and network policies
to isolate containers at multiple levels.
* Admission plugins, which form boundaries between an API and those
making requests to the API.

{product-title} uses Operators to automate and simplify the management of
Kubernetes-level security features.

// Multitenancy
include::modules/security-platform-multi-tenancy.adoc[leveloffset=+1]

// Admission plugins
include::modules/security-platform-admission.adoc[leveloffset=+1]

// Authentication and authorization
include::modules/security-platform-authentication.adoc[leveloffset=+1]

// Managing certificates for the platform
include::modules/security-platform-certificates.adoc[leveloffset=+1]

[role="_additional-resources"]
.Additional resources
* xref:../../architecture/architecture.adoc#architecture-platform-introduction_architecture[Introduction to {product-title}]
* xref:../../authentication/using-rbac.adoc#using-rbac[Using RBAC to define and apply permissions]

ifndef::openshift-origin[]
* xref:../../architecture/admission-plug-ins.adoc#admission-plug-ins[About admission plugins]
endif::[]

* xref:../../authentication/managing-security-context-constraints.adoc#managing-pod-security-policies[Managing security context constraints]
* xref:../../authentication/managing-security-context-constraints.adoc#security-context-constraints-command-reference_configuring-internal-oauth[SCC reference commands]
* xref:../../authentication/understanding-and-creating-service-accounts.adoc#service-accounts-granting-roles_understanding-service-accounts[Examples of granting roles to service accounts]
* xref:../../authentication/configuring-internal-oauth.adoc#configuring-internal-oauth[Configuring the internal OAuth server]
* xref:../../authentication/understanding-identity-provider.adoc#understanding-identity-provider[Understanding identity provider configuration]
* xref:../../security/certificate_types_descriptions/user-provided-certificates-for-api-server.adoc#cert-types-user-provided-certificates-for-the-api-server[Certificate types and descriptions]
* xref:../../security/certificate_types_descriptions/proxy-certificates.adoc#cert-types-proxy-certificates[Proxy certificates]
