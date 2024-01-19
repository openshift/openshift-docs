// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-rfc2307_{context}"]
= Syncing groups using the RFC 2307 schema

For the RFC 2307 schema, the following examples synchronize a group named `admins` that has two
members: `Jane` and `Jim`. The examples explain:

* How the group and users are added to the LDAP server.
* What the resulting group record in {product-title} will be after synchronization.

[NOTE]
====
These examples assume that all users are direct members of their respective
groups. Specifically, no groups have other groups as members. See
the Nested Membership Sync Example for information on
how to sync nested groups.
====

In the RFC 2307 schema, both users (Jane and Jim) and groups exist on the LDAP
server as first-class entries, and group membership is stored in attributes on
the group. The following snippet of `ldif` defines the users and group for this
schema:

.LDAP entries that use RFC 2307 schema: `rfc2307.ldif`
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
  dn: cn=admins,ou=groups,dc=example,dc=com <1>
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com <2>
  member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The group is a first-class entry in the LDAP server.
<2> Members of a group are listed with an identifying reference as attributes on
the group.

.Prerequisites

* Create the configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Run the sync with the `rfc2307_config.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config.yaml --confirm
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
    openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400 <1>
    openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com <2>
    openshift.io/ldap.url: LDAP_SERVER_IP:389 <3>
  creationTimestamp:
  name: admins <4>
users: <5>
- jane.smith@example.com
- jim.adams@example.com
----
<1> The last time this {product-title} group was synchronized with the LDAP server, in ISO 6801
format.
<2> The unique identifier for the group on the LDAP server.
<3> The IP address and host of the LDAP server where this group's record is
stored.
<4> The name of the group as specified by the sync file.
<5> The users that are members of the group, named as specified by the sync file.
