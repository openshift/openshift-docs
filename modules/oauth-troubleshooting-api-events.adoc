// Module included in the following assemblies:
//
// * authentication/configuring-internal-oauth.adoc

[id="oauth-troubleshooting-api-events_{context}"]
= Troubleshooting OAuth API events

In some cases the API server returns an `unexpected condition` error message
that is difficult to debug without direct access to the API master log.
The underlying reason for the error is purposely obscured in order
to avoid providing an unauthenticated user with information about the server's state.

A subset of these errors is related to service account OAuth configuration issues.
These issues are captured in events that can be viewed by non-administrator users. When encountering
an `unexpected condition` server error during OAuth, run `oc get events` to view these events under `ServiceAccount`.

The following example warns of a service account that is missing a proper OAuth redirect URI:

[source,terminal]
----
$ oc get events | grep ServiceAccount
----

.Example output
[source,terminal]
----
1m         1m          1         proxy                    ServiceAccount                                  Warning   NoSAOAuthRedirectURIs   service-account-oauth-client-getter   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
----

Running `oc describe sa/<service_account_name>` reports any OAuth events associated with the given service account name.

[source,terminal]
----
$ oc describe sa/proxy | grep -A5 Events
----

.Example output
[source,terminal]
----
Events:
  FirstSeen     LastSeen        Count   From                                    SubObjectPath   Type            Reason                  Message
  ---------     --------        -----   ----                                    -------------   --------        ------                  -------
  3m            3m              1       service-account-oauth-client-getter                     Warning         NoSAOAuthRedirectURIs   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
----

The following is a list of the possible event errors:

**No redirect URI annotations or an invalid URI is specified**

[source,terminal]
----
Reason                  Message
NoSAOAuthRedirectURIs   system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>
----

**Invalid route specified**

[source,terminal]
----
Reason                  Message
NoSAOAuthRedirectURIs   [routes.route.openshift.io "<name>" not found, system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>]
----

**Invalid reference type specified**

[source,terminal]
----
Reason                  Message
NoSAOAuthRedirectURIs   [no kind "<name>" is registered for version "v1", system:serviceaccount:myproject:proxy has no redirectURIs; set serviceaccounts.openshift.io/oauth-redirecturi.<some-value>=<redirect> or create a dynamic URI using serviceaccounts.openshift.io/oauth-redirectreference.<some-value>=<reference>]
----

**Missing SA tokens**

[source,terminal]
----
Reason                  Message
NoSAOAuthTokens         system:serviceaccount:myproject:proxy has no tokens
----
