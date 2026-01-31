// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

:_mod-docs-content-type: PROCEDURE
[id="oauth-delete-tokens_{context}"]
= Deleting user-owned OAuth access tokens

The `oc logout` command only invalidates the OAuth token for the active session. You can use the following procedure to delete any user-owned OAuth tokens that are no longer needed.

Deleting an OAuth access token logs out the user from all sessions that use the token.

.Procedure

* Delete the user-owned OAuth access token:
+
[source,terminal]
----
$ oc delete useroauthaccesstokens <token_name>
----
+
.Example output
[source,terminal]
----
useroauthaccesstoken.oauth.openshift.io "<token_name>" deleted
----
