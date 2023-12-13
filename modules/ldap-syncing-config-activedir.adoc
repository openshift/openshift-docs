// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: CONCEPT
[id="ldap-syncing-config-activedir_{context}"]
= About the Active Directory configuration file

The Active Directory schema requires you to provide an LDAP query definition for
user entries, as well as the attributes to represent them with in the internal
{product-title} group records.

For clarity, the group you create in {product-title} should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an {product-title} group by their e-mail, but define
the name of the group by the name of the group on the LDAP server.
The following configuration file creates these relationships:

.LDAP sync configuration that uses Active Directory schema: `active_directory_config.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
activeDirectory:
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ] <1>
    groupMembershipAttributes: [ memberOf ] <2>
----
<1> The attribute to use as the name of the user in the {product-title} group record.
<2> The attribute on the user that stores the membership information.
