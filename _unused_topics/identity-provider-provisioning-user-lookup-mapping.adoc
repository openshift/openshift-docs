// Module included in the following assemblies:
//
// * orphaned

[id="identity-provider-provisioning-user-lookup-mapping_{context}"]
= Manually provisioning a user when using the lookup mapping method

When using the `lookup` mapping method, user provisioning is done by an external system, via the API.
Typically, identities are automatically mapped to users during login. The 'lookup' mapping method automatically
disables this automatic mapping, which requires you to provision users manually.


.Procedure 

If you are using the `lookup` mapping method, use the following steps for each user after configuring
the identity provider:

. Create an {product-title} User, if not created already:
+
----
$ oc create user <username>
----
+
For example, the following command creates an {product-title} User `bob`:
+
----
$ oc create user bob
----

. Create an {product-title} Identity, if not created already. Use the name of the identity provider and
the name that uniquely represents this identity in the scope of the identity provider:
+
----
$ oc create identity <identity-provider>:<user-id-from-identity-provider>
----
+
The `<identity-provider>` is the name of the identity provider in the master configuration,
as shown in the appropriate identity provider section below.
+
For example, the following commands creates an Identity with identity provider `ldap_provider` and the identity provider user name `bob_s`.
+
----
$ oc create identity ldap_provider:bob_s
----

. Create a user/identity mapping for the created user and identity:
+
----
$ oc create useridentitymapping <identity-provider>:<user-id-from-identity-provider> <username>
----
+
For example, the following command maps the identity to the user:
+
----
$ oc create useridentitymapping ldap_provider:bob_s bob
----
