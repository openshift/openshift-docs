// Module included in the following assemblies:
//
// * authentication/configuring-ldap-failover.adoc

[id="sssd-for-ldap-overview_{context}"]

{product-title} provides an authentication
provider for use with Lightweight Directory Access Protocol (LDAP) setups, but
it can connect to only a single LDAP server. During {product-title} installation,
you can configure the System Security
Services Daemon (SSSD) for LDAP failover to ensure access to your cluster if one 
LDAP server fails.

The setup for this configuration is advanced and requires a separate
authentication server, also called an *remote basic authentication server*, for
{product-title} to communicate with. You configure this server
to pass extra attributes, such as email addresses, to {product-title} so it can
display them in the web console.

This topic describes how to complete this set up on a dedicated physical or 
virtual machine (VM), but you can also configure SSSD in containers.

[IMPORTANT]
====
You must complete all sections of this topic.
====
