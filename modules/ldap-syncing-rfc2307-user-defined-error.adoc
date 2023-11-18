// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-rfc2307-user-defined-error_{context}"]
= Syncing groups using RFC 2307 with user-defined error tolerances

By default, if the groups being synced contain members whose entries are outside
of the scope defined in the member query, the group sync fails with an error:

----
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with dn="<user-dn>" would search outside of the base dn specified (dn="<base-dn>")".
----

This often indicates a misconfigured `baseDN` in the `usersQuery` field.
However, in cases where the `baseDN` intentionally does not contain some of the
members of the group, setting `tolerateMemberOutOfScopeErrors: true` allows
the group sync to continue. Out of scope members will be ignored.

Similarly, when the group sync process fails to locate a member for a group, it
fails outright with errors:

----
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" refers to a non-existent entry".
Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" and filter "<filter>" did not return any results".
----

This often indicates a misconfigured `usersQuery` field. However, in cases
where the group contains member entries that are known to be missing, setting
`tolerateMemberNotFoundErrors: true` allows the group sync to continue.
Problematic members will be ignored.

[WARNING]
====
Enabling error tolerances for the LDAP group sync causes the sync process to
ignore problematic member entries. If the LDAP group sync is not configured
correctly, this could result in synced {product-title} groups missing members.
====

.LDAP entries that use RFC 2307 schema with problematic group membership: `rfc2307_problematic_users.ldif`
[source,ldif]
----
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
  member: cn=INVALID,ou=users,dc=example,dc=com <1>
  member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com <2>
----
<1> A member that does not exist on the LDAP server.
<2> A member that may exist, but is not under the `baseDN` in the
user query for the sync job.

To tolerate the errors in the above example, the following additions to
your sync configuration file must be made:

.LDAP sync configuration that uses RFC 2307 schema tolerating errors: `rfc2307_config_tolerating.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
    userUIDAttribute: dn <1>
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: true <2>
    tolerateMemberOutOfScopeErrors: true <3>
----
<1> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.
<2> When `true`, the sync job tolerates groups for which some members were not
found, and members whose LDAP entries are not found are ignored. The
default behavior for the sync job is to fail if a member of a group is not
found.
<3> When `true`, the sync job tolerates groups for which some members are outside
the user scope given in the `usersQuery` base DN, and members outside the member
query scope are ignored. The default behavior for the sync job is to fail if a
member of a group is out of scope.

.Prerequisites

* Create the configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Run the sync with the `rfc2307_config_tolerating.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config_tolerating.yaml --confirm
----
+
{product-title} creates the following group record as a result of the above sync
operation:
+
.{product-title} group created by using the `rfc2307_config.yaml` file
[source,yaml]
----
apiVersion: user.openshift.io/v1
kind: Group
metadata:
  annotations:
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
    openshift.io/ldap.url: LDAP_SERVER_IP:389
  creationTimestamp:
  name: admins
users: <1>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The users that are members of the group, as specified by the sync file.
Members for which lookup encountered tolerated errors are absent.
