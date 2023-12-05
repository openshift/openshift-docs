// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc

:_mod-docs-content-type: CONCEPT
[id="identity-provider-about-basic-authentication_{context}"]
= About basic authentication

Basic authentication is a generic back-end integration mechanism that allows
users to log in to {product-title} with credentials validated against a remote
identity provider.

Because basic authentication is generic, you can use this identity
provider for advanced authentication configurations.

[IMPORTANT]
====
Basic authentication must use an HTTPS connection to the remote server to
prevent potential snooping of the user ID and password and man-in-the-middle
attacks.
====

With basic authentication configured, users send their user name
and password to {product-title}, which then validates those credentials against
a remote server by making a server-to-server request, passing the credentials as
a basic authentication header. This requires users to send their credentials to
{product-title} during login.

[NOTE]
====
This only works for user name/password login mechanisms, and {product-title} must
be able to make network requests to the remote authentication server.
====

User names and passwords are validated against a remote URL that is protected
by basic authentication and returns JSON.

A `401` response indicates failed authentication.

A non-`200` status, or the presence of a non-empty "error" key, indicates an
error:

[source,terminal]
----
{"error":"Error message"}
----

A `200` status with a `sub` (subject) key indicates success:

[source,terminal]
----
{"sub":"userid"} <1>
----
<1> The subject must be unique to the authenticated user and must not be able to
be modified.

A successful response can optionally provide additional data, such as:

* A display name using the `name` key. For example:
+
[source,terminal]
----
{"sub":"userid", "name": "User Name", ...}
----
+
* An email address using the `email` key. For example:
+
[source,terminal]
----
{"sub":"userid", "email":"user@example.com", ...}
----
+
* A preferred user name using the `preferred_username` key. This is useful when
the unique, unchangeable subject is a database key or UID, and a more
human-readable name exists. This is used as a hint when provisioning the
{product-title} user for the authenticated identity. For example:
+
[source,terminal]
----
{"sub":"014fbff9a07c", "preferred_username":"bob", ...}
----
