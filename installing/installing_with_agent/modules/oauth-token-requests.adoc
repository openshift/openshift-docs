// Module included in the following assemblies:
//
// * authentication/understanding-authentication.adoc

[id="oauth-token-requests_{context}"]
== OAuth token requests

Every request for an OAuth token must specify the OAuth client that will
receive and use the token. The following OAuth clients are automatically
created when starting the {product-title} API:

[options="header"]
|===

|OAuth client |Usage

|`openshift-browser-client`
|Requests tokens at `<namespace_route>/oauth/token/request` with a user-agent that can handle interactive logins. ^[1]^

|`openshift-challenging-client`
|Requests tokens with a user-agent that can handle `WWW-Authenticate` challenges.

|===
[.small]
--
1. `<namespace_route>` refers to the namespace route. This is found by
running the following command:
+
[source,terminal]
----
$ oc get route oauth-openshift -n openshift-authentication -o json | jq .spec.host
----
--

All requests for OAuth tokens involve a request to
`<namespace_route>/oauth/authorize`. Most authentication integrations place an
authenticating proxy in front of this endpoint, or configure
{product-title} to validate credentials against a backing identity provider.
Requests to `<namespace_route>/oauth/authorize` can come from user-agents that
cannot display interactive login pages, such as the CLI. Therefore,
{product-title} supports authenticating using a `WWW-Authenticate`
challenge in addition to interactive login flows.

If an authenticating proxy is placed in front of the
`<namespace_route>/oauth/authorize` endpoint, it sends unauthenticated,
non-browser user-agents `WWW-Authenticate` challenges rather than
displaying an interactive login page or redirecting to an interactive
login flow.

[NOTE]
====
To prevent cross-site request forgery (CSRF) attacks against browser
clients,  only send Basic authentication challenges with if a
`X-CSRF-Token` header is on the request. Clients that expect
to receive Basic `WWW-Authenticate` challenges must set this header to a
non-empty value.

If the authenticating proxy cannot support `WWW-Authenticate` challenges,
or if {product-title} is configured to use an identity provider that does
not support WWW-Authenticate challenges, you must use a browser to manually
obtain a token from
`<namespace_route>/oauth/token/request`.
====
