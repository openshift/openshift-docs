// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc
// * networking/route-configuration.adoc

:_mod-docs-content-type: CONCEPT
[id="nw-http-header-configuration_{context}"]
= HTTP header configuration

{product-title} provides different methods for working with HTTP headers. When setting or deleting headers, you can use specific fields in the Ingress Controller or an individual route to modify request and response headers. You can also set certain headers by using route annotations. The various ways of configuring headers can present challenges when working together.

[NOTE]
====
You can only set or delete headers within an `IngressController` or `Route` CR, you cannot append them. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.
====

[id="nw-http-header-configuration-order_{context}"]
== Order of precedence

When the same HTTP header is modified both in the Ingress Controller and in a route, HAProxy prioritizes the actions in certain ways depending on whether it is a request or response header.

* For HTTP response headers, actions specified in the Ingress Controller are executed after the actions specified in a route. This means that the actions specified in the Ingress Controller take precedence.

* For HTTP request headers, actions specified in a route are executed after the actions specified in the Ingress Controller. This means that the actions specified in the route take precedence.

For example, a cluster administrator sets the X-Frame-Options response header with the value `DENY` in the Ingress Controller using the following configuration:

.Example `IngressController` spec
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: DENY
----

A route owner sets the same response header that the cluster administrator set in the Ingress Controller, but with the value `SAMEORIGIN` using the following configuration:

.Example `Route` spec
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: SAMEORIGIN
----

When both the `IngressController` spec and `Route` spec are configuring the X-Frame-Options header, then the value set for this header at the global level in the Ingress Controller will take precedence, even if a specific route allows frames.

This prioritzation occurs because the `haproxy.config` file uses the following logic, where the Ingress Controller is considered the front end and individual routes are considered the back end. The header value `DENY` applied to the front end configurations overrides the same header with the value `SAMEORIGIN` that is set in the back end:

[source,text]
----
frontend public
  http-response set-header X-Frame-Options 'DENY'

frontend fe_sni
  http-response set-header X-Frame-Options 'DENY'

frontend fe_no_sni
  http-response set-header X-Frame-Options 'DENY'

backend be_secure:openshift-monitoring:alertmanager-main
  http-response set-header X-Frame-Options 'SAMEORIGIN'
----

Additionally, any actions defined in either the Ingress Controller or a route override values set using route annotations.

[id="nw-http-header-configuration-special-cases_{context}"]
== Special case headers

The following headers are either prevented entirely from being set or deleted, or allowed under specific circumstances:

.Special case header configuration options
[cols="5*a",options="header"]
|===
|Header name |Configurable using `IngressController` spec |Configurable using `Route` spec |Reason for disallowment |Configurable using another method

|`proxy`
|No
|No
|The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.
|No

|`host`
|No
|Yes
|When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.
|No

|`strict-transport-security`
|No
|No
|The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.
|Yes: the `haproxy.router.openshift.io/hsts_header` route annotation

|`cookie` and `set-cookie`
|No
|No
|The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy's session affinity and restrict HAProxy's ownership of a cookie.
|Yes:

* the `haproxy.router.openshift.io/disable_cookie` route annotation
* the `haproxy.router.openshift.io/cookie_name` route annotation

|===
