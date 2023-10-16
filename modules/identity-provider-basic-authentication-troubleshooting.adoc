// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc

[id="identity-provider-basic-authentication-troubleshooting_{context}"]
= Basic authentication troubleshooting

The most common issue relates to network connectivity to the backend server. For
simple debugging, run `curl` commands on the master. To test for a successful
login, replace the `<user>` and `<password>` in the following example command
with valid credentials. To test an invalid login, replace them with false
credentials.

[source,terminal]
----
$ curl --cacert /path/to/ca.crt --cert /path/to/client.crt --key /path/to/client.key -u <user>:<password> -v https://www.example.com/remote-idp
----

*Successful responses*

A `200` status with a `sub` (subject) key indicates success:

[source,terminal]
----
{"sub":"userid"}
----
The subject must be unique to the authenticated user, and must not be able to
be modified.

A successful response can optionally provide additional data, such as:

* A display name using the `name` key:
+
[source,terminal]
----
{"sub":"userid", "name": "User Name", ...}
----
* An email address using the `email` key:
+
[source,terminal]
----
{"sub":"userid", "email":"user@example.com", ...}
----
* A preferred user name using the `preferred_username` key:
+
[source,terminal]
----
{"sub":"014fbff9a07c", "preferred_username":"bob", ...}
----
+
The `preferred_username` key is useful when
the unique, unchangeable subject is a database key or UID, and a more
human-readable name exists. This is used as a hint when provisioning the
{product-title} user for the authenticated identity.

*Failed responses*

- A `401` response indicates failed authentication.
- A non-`200` status or the presence of a non-empty "error" key indicates an
error: `{"error":"Error message"}`
