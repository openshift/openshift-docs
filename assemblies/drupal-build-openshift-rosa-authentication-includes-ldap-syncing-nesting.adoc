// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-nesting_{context}"]
== LDAP nested membership sync example

Groups in {product-title} do not nest. The LDAP server must flatten group
membership before the data can be consumed. Microsoft's Active Directory Server
supports this feature via the
link:https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx[`LDAP_MATCHING_RULE_IN_CHAIN`]
rule, which has the OID `1.2.840.113556.1.4.1941`. Furthermore, only explicitly
whitelisted groups can be synced when using this matching rule.

This section has an example for the augmented Active Directory schema, which
synchronizes a group named `admins` that has one user `Jane` and one group
`otheradmins` as members. The `otheradmins` group has one user member: `Jim`.
This example explains:

* How the group and users are added to the LDAP server.
* What the LDAP sync configuration file looks like.
* What the resulting group record in {product-title} will be after synchronization.

In the augmented Active Directory schema, both users (`Jane` and `Jim`) and
groups exist in the LDAP server as first-class entries, and group membership is
stored in attributes on the user or the group. The following snippet of `ldif`
defines the users and groups for this schema:

.LDAP entries that use augmented Active Directory schema with nested members: `augmented_active_directory_nested.ldif`
[source,ldif]
----
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com <1>

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=otheradmins,ou=groups,dc=example,dc=com <1>

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com <2>
objectClass: group
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=otheradmins,ou=groups,dc=example,dc=com

dn: cn=otheradmins,ou=groups,dc=example,dc=com <2>
objectClass: group
cn: otheradmins
owner: cn=admin,dc=example,dc=com
description: Other System Administrators
memberOf: cn=admins,ou=groups,dc=example,dc=com <1> <3>
member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The user's and group's memberships are listed as attributes on the object.
<2> The groups are first-class entries on the LDAP server.
<3> The `otheradmins` group is a member of the `admins` group.

When syncing nested groups with Active Directory, you must provide an LDAP query
definition for both user entries and group entries, as well as the attributes
with which to represent them in the internal {product-title} group records.
Furthermore, certain changes are required in this configuration:

- The `oc adm groups sync` command must explicitly whitelist groups.
- The user's `groupMembershipAttributes` must include
`"memberOf:1.2.840.113556.1.4.1941:"` to comply with the
https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx[`LDAP_MATCHING_RULE_IN_CHAIN`]
rule.
- The `groupUIDAttribute` must be set to `dn`.
- The `groupsQuery`:
  * Must not set `filter`.
  * Must set a valid `derefAliases`.
  * Should not set `baseDN` as that value is ignored.
  * Should not set `scope` as that value is ignored.

For clarity, the group you create in {product-title} should use attributes other
than the distinguished name whenever possible for user- or administrator-facing
fields. For example, identify the users of an {product-title} group by their e-mail, and use the
name of the group as the common name. The following configuration file creates
these relationships:

.LDAP sync configuration that uses augmented Active Directory schema with nested members: `augmented_active_directory_config_nested.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery: <1>
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <2>
    groupNameAttributes: [ cn ] <3>
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ] <4>
    groupMembershipAttributes: [ "memberOf:1.2.840.113556.1.4.1941:" ] <5>
----
<1> `groupsQuery` filters cannot be specified. The `groupsQuery` base DN and scope
values are ignored. `groupsQuery` must set a valid `derefAliases`.
<2> The attribute that uniquely identifies a group on the LDAP server. It must be set to `dn`.
<3> The attribute to use as the name of the group.
<4> The attribute to use as the name of the user in the {product-title} group
record. `mail` or `sAMAccountName` are preferred choices in most installations.
<5> The attribute on the user that stores the membership information. Note the use
of https://msdn.microsoft.com/en-us/library/aa746475(v=vs.85).aspx[`LDAP_MATCHING_RULE_IN_CHAIN`].

.Prerequisites

* Create the configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Run the sync with the `augmented_active_directory_config_nested.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync \
    'cn=admins,ou=groups,dc=example,dc=com' \
    --sync-config=augmented_active_directory_config_nested.yaml \
    --confirm
----
+
[NOTE]
====
You must explicitly whitelist the `cn=admins,ou=groups,dc=example,dc=com` group.
====
+
{product-title} creates the following group record as a result of the above sync
operation:
+
.{product-title} group created by using the `augmented_active_directory_config_nested.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this {product-title} group was synchronized with the LDAP server, in ISO 6801 format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is stored.
<4> The name of the group as specified by the sync file.
<5> The users that are members of the group, named as specified by the sync file.
Note that members of nested groups are included since the group membership was
flattened by the Microsoft Active Directory Server.
