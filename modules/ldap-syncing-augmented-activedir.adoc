// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-augmented-activedir_{context}"]
= Syncing groups using the augmented Active Directory schema

In the augmented Active Directory schema, both users (Jane and Jim) and groups
exist in the LDAP server as first-class entries, and group membership is stored
in attributes on the user. The following snippet of `ldif` defines the users and
group for this schema:

.LDAP entries that use augmented Active Directory schema: `augmented_active_directory.ldif`
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
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com <2>
objectClass: groupOfNames
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
----
<1> The user's group memberships are listed as attributes on the user.
<2> The group is a first-class entry on the LDAP server.

.Prerequisites

* Create the configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Run the sync with the `augmented_active_directory_config.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=augmented_active_directory_config.yaml --confirm
----
+
{product-title} creates the following group record as a result of the above sync
operation:
+
.{product-title} group created by using the `augmented_active_directory_config.yaml` file

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
