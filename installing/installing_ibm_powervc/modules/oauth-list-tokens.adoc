// Module included in the following assemblies:
//
// * authentication/managing-oauth-access-tokens.adoc

:_mod-docs-content-type: PROCEDURE
[id="oauth-list-tokens_{context}"]
= Listing user-owned OAuth access tokens

You can list your user-owned OAuth access tokens. Token names are not sensitive and cannot be used to log in.

.Procedure

* List all user-owned OAuth access tokens:
+
[source,terminal]
----
$ oc get useroauthaccesstokens
----
+
.Example output
[source,terminal]
----
NAME       CLIENT NAME                    CREATED                EXPIRES                         REDIRECT URI                                                       SCOPES
<token1>   openshift-challenging-client   2021-01-11T19:25:35Z   2021-01-12 19:25:35 +0000 UTC   https://oauth-openshift.apps.example.com/oauth/token/implicit      user:full
<token2>   openshift-browser-client       2021-01-11T19:27:06Z   2021-01-12 19:27:06 +0000 UTC   https://oauth-openshift.apps.example.com/oauth/token/display       user:full
<token3>   console                        2021-01-11T19:26:29Z   2021-01-12 19:26:29 +0000 UTC   https://console-openshift-console.apps.example.com/auth/callback   user:full
----

* List user-owned OAuth access tokens for a particular OAuth client:
+
[source,terminal]
----
$ oc get useroauthaccesstokens --field-selector=clientName="console"
----
+
.Example output
[source,terminal]
----
NAME       CLIENT NAME                    CREATED                EXPIRES                         REDIRECT URI                                                       SCOPES
<token3>   console                        2021-01-11T19:26:29Z   2021-01-12 19:26:29 +0000 UTC   https://console-openshift-console.apps.example.com/auth/callback   user:full
----
