// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: CONCEPT
[id="ldap-syncing-config-rfc2307_{context}"]
= About the RFC 2307 configuration file

The RFC 2307 schema requires you to provide an LDAP query definition for both user
and group entries, as well as the attributes with which to represent them in the
internal {product-title} records.

For clarity, the group you create in {product-title} should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an {product-title} group by their e-mail, and use the
name of the group as the common name. The following configuration file creates
these relationships:

[NOTE]
====
If using user-defined name mappings, your configuration file will differ.
====

.LDAP sync configuration that uses RFC 2307 schema: `rfc2307_config.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389 <1>
insecure: false <2>
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <3>
    groupNameAttributes: [ cn ] <4>
    groupMembershipAttributes: [ member ] <5>
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn <6>
    userNameAttributes: [ mail ] <7>
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
----
<1> The IP address and host of the LDAP server where this group's record is
stored.
<2> When `false`, secure
LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are
upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.
<3> The attribute that uniquely identifies a group on the LDAP server.
You cannot specify `groupsQuery` filters when using DN for `groupUIDAttribute`.
For fine-grained filtering, use the whitelist / blacklist method.
<4> The attribute to use as the name of the group.
<5> The attribute on the group that stores the membership information.
<6> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.
<7> The attribute to use as the name of the user in the {product-title} group record.
