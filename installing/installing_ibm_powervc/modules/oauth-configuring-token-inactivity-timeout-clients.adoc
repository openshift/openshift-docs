// Module included in the following assemblies:
//
// * authentication/configuring-oauth-clients.adoc

:_mod-docs-content-type: PROCEDURE
[id="oauth-token-inactivity-timeout_{context}"]
= Configuring token inactivity timeout for an OAuth client

You can configure OAuth clients to expire OAuth tokens after a set period of inactivity. By default, no token inactivity timeout is set.

[NOTE]
====
If the token inactivity timeout is also configured in the internal OAuth server configuration, the timeout that is set in the OAuth client overrides that value.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have configured an identity provider (IDP).

.Procedure

* Update the `OAuthClient` configuration to set a token inactivity timeout.

.. Edit the `OAuthClient` object:
+
[source,terminal]
----
$ oc edit oauthclient <oauth_client> <1>
----
<1> Replace `<oauth_client>` with the OAuth client to configure, for example, `console`.
+
Add the `accessTokenInactivityTimeoutSeconds` field and set your timeout value:
+
[source,yaml]
----
apiVersion: oauth.openshift.io/v1
grantMethod: auto
kind: OAuthClient
metadata:
...
accessTokenInactivityTimeoutSeconds: 600 <1>
----
<1> The minimum allowed timeout value in seconds is `300`.

.. Save the file to apply the changes.

.Verification

. Log in to the cluster with an identity from your IDP. Be sure to use the OAuth client that you just configured.

. Perform an action and verify that it was successful.

. Wait longer than the configured timeout without using the identity. In this procedure's example, wait longer than 600 seconds.

. Try to perform an action from the same identity's session.
+
This attempt should fail because the token should have expired due to inactivity longer than the configured timeout.
