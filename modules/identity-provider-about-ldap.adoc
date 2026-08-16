// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc

:_mod-docs-content-type: CONCEPT
[id="identity-provider-about-ldap_{context}"]
= About LDAP authentication

During authentication, the LDAP directory is searched for an entry that matches
the provided user name. If a single unique match is found, a simple bind is
attempted using the distinguished name (DN) of the entry plus the provided
password.

These are the steps taken:

. Generate a search filter by combining the attribute and filter in the
configured `url` with the user-provided user name.
. Search the directory using the generated filter. If the search does not return
exactly one entry, deny access.
. Attempt to bind to the LDAP server using the DN of the entry retrieved from
the search, and the user-provided password.
. If the bind is unsuccessful, deny access.
. If the bind is successful, build an identity using the configured attributes
as the identity, email address, display name, and preferred user name.

The configured `url` is an RFC 2255 URL, which specifies the LDAP host and
search parameters to use. The syntax of the URL is:

----
ldap://host:port/basedn?attribute?scope?filter
----

For this URL:

[cols="2a,8a",options="header"]
|===
|URL component | Description
.^|`ldap`      | For regular LDAP, use the string `ldap`. For secure LDAP
(LDAPS), use `ldaps` instead.
.^|`host:port` | The name and port of the LDAP server. Defaults to
`localhost:389` for ldap and `localhost:636` for LDAPS.
.^|`basedn`    | The DN of the branch of the directory where all searches should
start from. At the very least, this must be the top of your directory tree, but
it could also specify a subtree in the directory.
.^|`attribute` | The attribute to search for. Although RFC 2255 allows a
comma-separated list of attributes, only the first attribute will be used, no
matter how many are provided. If no attributes are provided, the default is to
use `uid`. It is recommended to choose an attribute that will be unique across
all entries in the subtree you will be using.
.^|`scope`     | The scope of the search. Can be either `one` or `sub`.
If the scope is not provided, the default is to use a scope of `sub`.
.^|`filter`    | A valid LDAP search filter. If not provided, defaults to
`(objectClass=*)`
|===

When doing searches, the attribute, filter, and provided user name are combined
to create a search filter that looks like:

----
(&(<filter>)(<attribute>=<username>))
----

For example, consider a URL of:

----
ldap://ldap.example.com/o=Acme?cn?sub?(enabled=true)
----

When a client attempts to connect using a user name of `bob`, the resulting
search filter will be `(&(enabled=true)(cn=bob))`.

If the LDAP directory requires authentication to search, specify a `bindDN` and
`bindPassword` to use to perform the entry search.
