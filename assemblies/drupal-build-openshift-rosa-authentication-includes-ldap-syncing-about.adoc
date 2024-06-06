// Module included in the following assemblies:
//
// * authentication/ldap-syncing.adoc

:_mod-docs-content-type: CONCEPT
[id="ldap-syncing-about_{context}"]
= About configuring LDAP sync

Before you can run LDAP sync, you need a sync
configuration file. This file contains the following LDAP client configuration details:

* Configuration for connecting to your LDAP server.
* Sync configuration options that are dependent on the schema used in your LDAP
server.
* An administrator-defined list of name mappings that maps {product-title} group names to groups in your LDAP server.

The format of the configuration file depends upon the schema you are using: RFC 2307, Active Directory, or augmented Active Directory.

[[ldap-client-configuration]]
LDAP client configuration::

The LDAP client configuration section of the configuration defines the connections to your LDAP server.

The LDAP client configuration section of the configuration defines the connections to your LDAP server.

.LDAP client configuration
[source,yaml]
----
url: ldap://10.0.0.0:389 <1>
bindDN: cn=admin,dc=example,dc=com <2>
bindPassword: <password> <3>
insecure: false <4>
ca: my-ldap-ca-bundle.crt <5>
----
<1> The connection protocol, IP address of the LDAP server hosting your
database, and the port to connect to, formatted as `scheme://host:port`.
<2> Optional distinguished name (DN) to use as the Bind DN.
{product-title} uses this if elevated privilege is required to retrieve entries for
the sync operation.
<3> Optional password to use to bind. {product-title} uses this if elevated privilege is
necessary to retrieve entries for the sync operation. This value may also be
provided in an environment variable, external file, or encrypted file.
<4> When `false`, secure
LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are
upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.
<5> The certificate bundle to use for validating server certificates for the
configured URL. If empty, {product-title} uses system-trusted roots. This only applies
if `insecure` is set to `false`.

[[ldap-query-definition]]
LDAP query definition::
Sync configurations consist of LDAP query definitions for the entries that are
required for synchronization. The specific definition of an LDAP query depends
on the schema used to store membership information in the LDAP server.

.LDAP query definition
[source,yaml]
----
baseDN: ou=users,dc=example,dc=com <1>
scope: sub <2>
derefAliases: never <3>
timeout: 0 <4>
filter: (objectClass=person) <5>
pageSize: 0 <6>
----
<1> The distinguished name (DN) of the branch of the directory where all
searches will start from. It is required that you specify the top of your
directory tree, but you can also specify a subtree in the directory.
<2> The scope of the search. Valid values are `base`, `one`, or `sub`. If this
is left undefined, then a scope of `sub` is assumed. Descriptions of the scope
options can be found in the table below.
<3> The behavior of the search with respect to aliases in the LDAP tree. Valid
values are `never`, `search`, `base`, or `always`. If this is left undefined,
then the default is to `always` dereference aliases. Descriptions of the
dereferencing behaviors can be found in the table below.
<4> The time limit allowed for the search by the client, in seconds. A value of
`0` imposes no client-side limit.
<5> A valid LDAP search filter. If this is left undefined, then the default is
`(objectClass=*)`.
<6> The optional maximum size of response pages from the server, measured in LDAP
entries. If set to `0`, no size restrictions will be made on pages of responses.
Setting paging sizes is necessary when queries return more entries than the
client or server allow by default.

[[ldap-search]]
.LDAP search scope options
[cols="2a,8a",options="header"]
|===
|LDAP search scope | Description
.^|`base`          | Only consider the object specified by the base DN given for the query.
.^|`one`           | Consider all of the objects on the same level in the tree as the base DN for
the query.
.^|`sub`           | Consider the entire subtree rooted at the base DN given for the query.
|===

[[deref-aliases]]
.LDAP dereferencing behaviors
[cols="2a,8a",options="header"]
|===
|Dereferencing behavior | Description
.^|`never`              | Never dereference any aliases found in the LDAP tree.
.^|`search`             | Only dereference aliases found while searching.
.^|`base`               | Only dereference aliases while finding the base object.
.^|`always`             | Always dereference all aliases found in the LDAP tree.
|===

[[user-defined-name-mapping]]
User-defined name mapping::
A user-defined name mapping explicitly maps the names of {product-title} groups to
unique identifiers that find groups on your LDAP server. The mapping uses normal
YAML syntax. A user-defined mapping can contain an entry for every group in your
LDAP server or only a subset of those groups. If there are groups on the LDAP
server that do not have a user-defined name mapping, the default behavior during
sync is to use the attribute specified as the {product-title} group's name.

.User-defined name mapping
[source,yaml]
----
groupUIDNameMapping:
  "cn=group1,ou=groups,dc=example,dc=com": firstgroup
  "cn=group2,ou=groups,dc=example,dc=com": secondgroup
  "cn=group3,ou=groups,dc=example,dc=com": thirdgroup
----
