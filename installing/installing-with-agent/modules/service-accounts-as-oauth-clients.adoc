// Module included in the following assemblies:
//
// * authentication/using-service-accounts-as-oauth-client.adoc

[id="service-accounts-as-oauth-clients_{context}"]
= Service accounts as OAuth clients

You can use a service account as a constrained form of OAuth client.
Service accounts can request only a subset of scopes that
allow access to some basic user information
and role-based power inside of the service account's own namespace:

* `user:info`
* `user:check-access`
* `role:<any_role>:<service_account_namespace>`
* `role:<any_role>:<service_account_namespace>:!`

When using a service account as an OAuth client:

* `client_id` is `system:serviceaccount:<service_account_namespace>:<service_account_name>`.
* `client_secret` can be any of the API tokens for that service account. For example:
+
[source,terminal]
----
$ oc sa get-token <service_account_name>
----

* To get `WWW-Authenticate` challenges, set an
`serviceaccounts.openshift.io/oauth-want-challenges` annotation on the service
account to `true`.

* `redirect_uri` must match an annotation on the service account.

[id="redirect-uris-for-service-accounts_{context}"]
== Redirect URIs for service accounts as OAuth clients

Annotation keys must have the prefix
`serviceaccounts.openshift.io/oauth-redirecturi.` or
`serviceaccounts.openshift.io/oauth-redirectreference.` such as:

----
serviceaccounts.openshift.io/oauth-redirecturi.<name>
----

In its simplest form, the annotation can be used to directly specify valid
redirect URIs. For example:

----
"serviceaccounts.openshift.io/oauth-redirecturi.first":  "https://example.com"
"serviceaccounts.openshift.io/oauth-redirecturi.second": "https://other.com"
----

The `first` and `second` postfixes in the above example are used to separate the
two valid redirect URIs.

In more complex configurations, static redirect URIs may not be enough. For
example, perhaps you want all Ingresses for a route to be considered valid. This
is where dynamic redirect URIs via the
`serviceaccounts.openshift.io/oauth-redirectreference.` prefix come into play.

For example:

----
"serviceaccounts.openshift.io/oauth-redirectreference.first": "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"jenkins\"}}"
----

Since the value for this annotation contains serialized JSON data, it is easier
to see in an expanded format:

[source,json]
----

{
  "kind": "OAuthRedirectReference",
  "apiVersion": "v1",
  "reference": {
    "kind": "Route",
    "name": "jenkins"
  }
}

----

Now you can see that an `OAuthRedirectReference` allows us to reference the
route named `jenkins`. Thus, all Ingresses for that route will now be considered
valid.  The full specification for an `OAuthRedirectReference` is:

[source,json]
----

{
  "kind": "OAuthRedirectReference",
  "apiVersion": "v1",
  "reference": {
    "kind": ..., <1>
    "name": ..., <2>
    "group": ... <3>
  }
}

----

<1> `kind` refers to the type of the object being referenced. Currently, only `route` is supported.
<2> `name` refers to the name of the object. The object must be in the same namespace as the service account.
<3> `group` refers to the group of the object. Leave this blank, as the group for a route is the empty string.

Both annotation prefixes can be combined to override the data provided by the
reference object. For example:

----
"serviceaccounts.openshift.io/oauth-redirecturi.first":  "custompath"
"serviceaccounts.openshift.io/oauth-redirectreference.first": "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"jenkins\"}}"
----

The `first` postfix is used to tie the annotations together. Assuming that the
`jenkins` route had an Ingress of `\https://example.com`, now
`\https://example.com/custompath` is considered valid, but
`\https://example.com` is not.  The format for partially supplying override
data is as follows:

[cols="4a,8a",options="header"]
|===
|Type | Syntax
|Scheme| "https://"
|Hostname| "//website.com"
|Port| "//:8000"
|Path| "examplepath"
|===

[NOTE]
====
Specifying a hostname override will replace the hostname data from the
referenced object, which is not likely to be desired behavior.
====

Any combination of the above syntax can be combined using the following format:

`<scheme:>//<hostname><:port>/<path>`

The same object can be referenced more than once for more flexibility:

----
"serviceaccounts.openshift.io/oauth-redirecturi.first":  "custompath"
"serviceaccounts.openshift.io/oauth-redirectreference.first": "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"jenkins\"}}"
"serviceaccounts.openshift.io/oauth-redirecturi.second":  "//:8000"
"serviceaccounts.openshift.io/oauth-redirectreference.second": "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"jenkins\"}}"
----

Assuming that the route named `jenkins` has an Ingress of
`\https://example.com`, then both `\https://example.com:8000` and
`\https://example.com/custompath` are considered valid.

Static and dynamic annotations can be used at the same time to achieve the
desired behavior:

----
"serviceaccounts.openshift.io/oauth-redirectreference.first": "{\"kind\":\"OAuthRedirectReference\",\"apiVersion\":\"v1\",\"reference\":{\"kind\":\"Route\",\"name\":\"jenkins\"}}"
"serviceaccounts.openshift.io/oauth-redirecturi.second": "https://other.com"
----
