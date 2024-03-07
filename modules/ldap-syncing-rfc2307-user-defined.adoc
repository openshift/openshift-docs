// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: PROCEDURE
[id="ldap-syncing-rfc2307-user-defined_{context}"]
= Syncing groups using the RFC2307 schema with user-defined name mappings

When syncing groups with user-defined name mappings, the configuration file
changes to contain these mappings as shown below.

.LDAP sync configuration that uses RFC 2307 schema with user-defined name mappings: `rfc2307_config_user_defined.yaml`
[source,yaml]
----
kind: LDAPSyncConfig
apiVersion: v1
groupUIDNameMapping:
  "cn=admins,ou=groups,dc=example,dc=com": Administrators <1>
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn <2>
    groupNameAttributes: [ cn ] <3>
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn <4>
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
----
<1> The user-defined name mapping.
<2> The unique identifier attribute that is used for the keys in the
user-defined name mapping. You cannot specify `groupsQuery` filters when using
DN for groupUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.
<3> The attribute to name {product-title} groups with if their unique identifier is
not in the user-defined name mapping.
<4> The attribute that uniquely identifies a user on the LDAP server. You
cannot specify `usersQuery` filters when using DN for userUIDAttribute. For
fine-grained  filtering, use the whitelist / blacklist method.

.Prerequisites

* Create the configuration file.
ifndef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-dedicated,openshift-rosa[]

.Procedure

* Run the sync with the `rfc2307_config_user_defined.yaml` file:
+
[source,terminal]
----
$ oc adm groups sync --sync-config=rfc2307_config_user_defined.yaml --confirm
----
+
{product-title} creates the following group record as a result of the above sync
operation:
+
.{product-title} group created by using the `rfc2307_config_user_defined.yaml` file
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
  name: Administrators <1>
users:
- jane.smith@example.com
- jim.adams@example.com
----
<1> The name of the group as specified by the user-defined name mapping.
