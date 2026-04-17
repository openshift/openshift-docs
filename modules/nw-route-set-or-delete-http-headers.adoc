// Module included in the following assemblies:
//
// * networking/route-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-route-set-or-delete-http-headers_{context}"]
= Setting or deleting HTTP request and response headers in a route

You can set or delete certain HTTP request and response headers for compliance purposes or other reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for specific routes.

For example, you might want to enable a web application to serve content in alternate locations for specific routes if that content is written in multiple languages, even if there is a default global location specified by the Ingress Controller serving the routes.

The following procedure creates a route that sets the Content-Location HTTP request header so that the URL associated with the application, `\https://app.example.com`, directs to the location `\https://app.example.com/lang/en-us`. Directing application traffic to this location means that anyone using that specific route is accessing web content written in American English.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).
* You are logged into an {product-title} cluster as a project administrator.
* You have a web application that exposes a port and an HTTP or TLS endpoint listening for traffic on the port.

.Procedure
. Create a route definition and save it in a file called `app-example-route.yaml`:
+
.YAML definition of the created route with HTTP header directives
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  host: app.example.com
  tls:
    termination: edge
  to:
    kind: Service
    name: app-example
  httpHeaders:
    actions: <1>
      response: <2>
      - name: Content-Location <3>
        action:
          type: Set <4>
          set:
            value: /lang/en-us <5>
----
<1> The list of actions you want to perform on the HTTP headers.
<2> The type of header you want to change. In this case, a response header.
<3> The name of the header you want to change. For a list of available headers you can set or delete, see _HTTP header configuration_.
<4> The type of action being taken on the header. This field can have the value `Set` or `Delete`.
<5> When setting HTTP headers, you must provide a `value`. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy's dynamic value syntax. In this case, the value is set to the relative location of the content.

. Create a route to your existing web application using the newly created route definition:
+
[source,terminal]
----
$ oc -n app-example create -f app-example-route.yaml
----

For HTTP request headers, the actions specified in the route definitions are executed after any actions performed on HTTP request headers in the Ingress Controller. This means that any values set for those request headers in a route will take precedence over the ones set in the Ingress Controller. For more information on the processing order of HTTP headers, see _HTTP header configuration_.
