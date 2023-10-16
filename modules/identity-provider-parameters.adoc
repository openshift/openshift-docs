// Module included in the following assemblies:
//
// * authentication/understanding-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-parameters_{context}"]
= Identity provider parameters

The following parameters are common to all identity providers:

[cols="2a,8a",options="header"]
|===
|Parameter     | Description
|`name`      | The provider name is prefixed to provider user names to form an
identity name.

|`mappingMethod`  | Defines how new identities are mapped to users when they log in.
Enter one of the following values:

claim:: The default value. Provisions a user with the identity's preferred
user name. Fails if a user with that user name is already mapped to another
identity.
lookup:: Looks up an existing identity, user identity mapping, and user,
but does not automatically provision users or identities. This allows cluster
administrators to set up identities and users manually, or using an external
process. Using this method requires you to manually provision users.
generate:: Provisions a user with the identity's preferred user name. If a
user with the preferred user name is already mapped to an existing identity, a
unique user name is generated. For example, `myuser2`. This method should not be
used in combination with external processes that require exact matches between
{product-title} user names and identity provider user names, such as LDAP group
sync.
add:: Provisions a user with the identity's preferred user name. If a user
with that user name already exists, the identity is mapped to the existing user,
adding to any existing identity mappings for the user. Required when multiple
identity providers are configured that identify the same set of users and map to
the same user names.
|===

[NOTE]
When adding or changing identity providers, you can map identities from the new
provider to existing users by setting the `mappingMethod` parameter to
`add`.
