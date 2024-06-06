// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-set-or-delete-http-headers_{context}"]
= Setting or deleting HTTP request and response headers in an Ingress Controller

You can set or delete certain HTTP request and response headers for compliance purposes or other reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for specific routes.

For example, you might want to migrate an application running on your cluster to use mutual TLS, which requires that your application checks for an X-Forwarded-Client-Cert request header, but the {product-title} default Ingress Controller provides an X-SSL-Client-Der request header.

The following procedure modifies the Ingress Controller to set the X-Forwarded-Client-Cert request header, and delete the X-SSL-Client-Der request header.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).
* You have access to an {product-title} cluster as a user with the `cluster-admin` role.

.Procedure
. Edit the Ingress Controller resource:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator edit ingresscontroller/default
----

. Replace the X-SSL-Client-Der HTTP request header with the X-Forwarded-Client-Cert HTTP request header:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    actions: <1>
      request: <2>
      - name: X-Forwarded-Client-Cert <3>
        action:
          type: Set <4>
          set:
           value: "%{+Q}[ssl_c_der,base64]" <5>
      - name: X-SSL-Client-Der
        action:
          type: Delete
----
<1> The list of actions you want to perform on the HTTP headers.
<2> The type of header you want to change. In this case, a request header.
<3> The name of the header you want to change. For a list of available headers you can set or delete, see _HTTP header configuration_.
<4> The type of action being taken on the header. This field can have the value `Set` or `Delete`.
<5> When setting HTTP headers, you must provide a `value`. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy's dynamic value syntax. In this case, a dynamic value is added.
+
[NOTE]
====
For setting dynamic header values for HTTP responses, allowed sample fetchers are `res.hdr` and `ssl_c_der`. For setting dynamic header values for HTTP requests, allowed sample fetchers are `req.hdr` and `ssl_c_der`. Both request and response dynamic values can use the `lower` and `base64` converters.
====

. Save the file to apply the changes.
