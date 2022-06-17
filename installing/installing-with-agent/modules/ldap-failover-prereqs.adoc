// Module included in the following assemblies:
//
// * authentication/configuring-ldap-failover.adoc

[id="sssd-for-ldap-prereqs_{context}"]
= Prerequisites for configuring basic remote authentication

* Before starting setup, you must know the following information about your
LDAP server:
** Whether the directory server is powered by
http://www.freeipa.org/page/Main_Page[FreeIPA], Active Directory, or another
LDAP solution.
** The Uniform Resource Identifier (URI) for the LDAP server, for example,
`ldap.example.com`.
** The location of the CA certificate for the LDAP server.
** Whether the LDAP server corresponds to RFC 2307 or RFC2307bis for user groups.
* Prepare the servers:
** `remote-basic.example.com`: A VM to use as the remote basic authentication server.
*** Select an operating system that includes SSSD version 1.12.0 for this server
such as Red Hat Enterprise Linux 7.0 or later.
ifeval::["{context}" == "sssd-ldap-failover-extend"]
*** Install mod_lookup_identity version 0.9.4 or later. You can obtain this
package link:https://github.com/adelton/mod_lookup_identity/releases[from
upstream].
endif::[]
** `openshift.example.com`: A new installation of {product-title}.
*** You must not
have an authentication method configured for this cluster.
*** Do not start {product-title} on this cluster.
